import os
from middlewares.save_audio import save_audio
from middlewares.mp3_to_wav import mp3_to_wav

def process_audio(request, audio_folder):
    try:
        audio_data = request.get_data()

        audio_folder_mp3 = os.path.join(audio_folder, "mp3", "audio_file.mp3")
        audio_folder_wav = os.path.join(audio_folder, "wav", "audio_file.wav")

        file_path = save_audio(audio_data, audio_folder_mp3)   
        file_path_wav = mp3_to_wav(file_path, audio_folder_wav)

        return file_path_wav

    except Exception as e:
        return f"Error processing audio: {str(e)}", 500