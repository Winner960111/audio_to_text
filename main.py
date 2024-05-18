# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
import json
import assemblyai as aai

aai.settings.api_key = "c06f79aec5ac4a008bd6ec0492b852a5"
transcriber = aai.Transcriber()
with open("output.json", "r") as file:
    data = json.load(file)
for index, item in enumerate(data):
    title = item['music_name']
    link = item['music_link']

    transcript = transcriber.transcribe(link)
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")
    text = f"{title}\n\n" + transcript.text
    with open(f"script{index}.txt", "w") as file:
        file.write(text)