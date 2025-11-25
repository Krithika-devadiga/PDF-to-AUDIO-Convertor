const { shell } = require("electron");

document.getElementById("convertBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("fileInput");
  const language = document.getElementById("language").value;
  const status = document.getElementById("status");
  const audioPlayer = document.getElementById("audioPlayer");
  const downloadLink = document.getElementById("downloadLink");

  audioPlayer.style.display = "none";
  downloadLink.style.display = "none";
  audioPlayer.src = "";

  if (!fileInput.files[0]) {
    status.innerText = "❌ Please select a PDF file.";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("language", language);

  status.innerText = "⏳ Converting... Please wait...";

  try {
    const response = await fetch("http://localhost:5000/convert", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.status === "success") {
      const audioPath = data.audioPath;

      status.innerHTML = `
        ✅ Conversion successful!<br>
        📂 Saved at: ${audioPath}<br>
      `;

      // Show and set audio player
      audioPlayer.src = `file://${audioPath}`;
      audioPlayer.style.display = "block";
      audioPlayer.play();

      // Show and set download link
      downloadLink.href = `file://${audioPath}`;
      downloadLink.download = "converted_audio.mp3";
      downloadLink.style.display = "inline-block";

      // Button to open folder
      const openBtn = document.createElement("button");
      openBtn.innerText = "📁 Open Folder";
      openBtn.addEventListener("click", () => {
        const folderPath = audioPath.substring(0, audioPath.lastIndexOf("/"));
        shell.openPath(folderPath);
      });
      status.appendChild(openBtn);

    } else {
      status.innerText = `❌ Error: ${data.message}`;
    }

  } catch (error) {
    console.error(error);
    status.innerText = "❌ Something went wrong!";
  }
});
