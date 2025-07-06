import whisper

def transcribe_video(video_path, output_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    with open(output_path, "w") as f:
        f.write(result['text'])
    return result['text']