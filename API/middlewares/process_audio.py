# middlewares/process_audio.py
from pydub import AudioSegment
import io

def process_audio(request):
    try:
        # Get the raw binary data from the request
        audio_data = request.files["audio"]

        audio_data = audio_data.read()

        print(audio_data)

        return audio_data
    except Exception as e:
        return f"Error processing audio: {str(e)}", 500