# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
import json
import assemblyai as aai

aai.settings.api_key = "9dedf671889f46fd9ac04f1276f5a9ad"
transcriber = aai.Transcriber()
with open("output.json", "r") as file:
    data = json.load(file)
for item in range(0,400):
    title = data[item]['music_name']
    link = data[item]['music_link']
    try:

        transcript = transcriber.transcribe(link)
        if transcript.status == aai.TranscriptStatus.error:
            print(transcript.error)
        else:
            print("success")
    except Exception as e:
        print(e)

    text = f"{title}\n\n" + transcript.text
    with open(f"script{item}.txt", "w", encoding='utf-8') as file:
        file.write(text)