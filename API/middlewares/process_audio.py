# middlewares/audio_processing.py
def process_audio(request):
    try:
        # Get the raw binary data from the request
        audio_data = request.get_data()
        return audio_data
    except Exception as e:
        return f"Error processing audio: {str(e)}", 500