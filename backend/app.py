from flask import Flask, request, jsonify
from flask_cors import CORS
from gtts import gTTS
from gtts.lang import tts_langs
from googletrans import Translator
import os
import fitz  # PyMuPDF
from datetime import datetime

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads", "pdf_audio_output")
SUPPORTED_LANGS = tts_langs()

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get("file")
    language = request.form.get("language", "en")

    if not file:
        return jsonify({"status": "error", "message": "No file uploaded."})

    if language not in SUPPORTED_LANGS:
        return jsonify({"status": "error", "message": f"Language '{language}' not supported by gTTS."})

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()

        if not text.strip():
            return jsonify({"status": "error", "message": "PDF has no readable text."})

        if language != "en":
            translator = Translator()
            translated = translator.translate(text, dest=language)
            text = translated.text

        tts = gTTS(text, lang=language)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        audio_filename = f"output_{timestamp}.mp3"
        audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
        tts.save(audio_path)

        return jsonify({
            "status": "success",
            "message": "Audio converted successfully.",
            "audioPath": audio_path.replace("\\", "/")
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000)
