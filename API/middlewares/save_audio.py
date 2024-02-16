import os


def save_audio(audio_data, file_path):
    try:
        with open(file_path, "wb") as file:
            file.write(audio_data)
        return file_path
    except Exception as e:
        return "error saving audio: " + str(e)
