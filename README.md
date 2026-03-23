🎧 PDF-to-Audio Converter App

A cross-platform desktop application built with Electron.js + Flask + gTTS

This project converts selected pages of any PDF into high-quality audio using Google Text-to-Speech (gTTS).
It uses Electron.js for the desktop UI and Python Flask as the backend API.

✨ Features

✔️ Upload any PDF file
✔️ Select page numbers to convert
✔️ Convert PDF → Text → Audio (MP3)
✔️ Multi-language voice support using gTTS
✔️ Clean and modern Electron interface
✔️ Fast and lightweight backend using Flask

🚀 Tech Stack
| Technology              | Purpose                         |
| ----------------------- | ------------------------------- |
| **Electron.js**         | Desktop UI & rendering          |
| **Python Flask**        | Backend API server              |
| **gTTS**                | Google Text-to-Speech for audio |
| **PyPDF2 / pdfplumber** | PDF text extraction             |
| **HTML / CSS / JS**     | Frontend design                 |
| **Node.js**             | Electron runtime                |


📁 Project Structure
pdf-to-audio-app/
│
├── backend/
│   ├── app.py
│   ├── venv/
│   ├── requirements.txt
│
├── frontend/
│   ├── main.js
│   ├── index.html
│   ├── style.css
│
├── output/           # generated audio files
├── uploads/          # uploaded PDFs
├── package.json
├── README.md
├── .gitignore



🛠️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/yourusername/pdf-to-audio-app.git
cd pdf-to-audio-app

2️⃣ Backend Setup (Flask)
Create virtual environment
python -m venv venv
Activate environment
Windows:
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run the backend
python app.py

3️⃣ Start the Electron App
Install packages:
npm install
Start the desktop app:
npm start

🎙️ How It Works

User uploads a PDF

Flask extracts text from selected pages

Sends text to gTTS

Generates .mp3 file

