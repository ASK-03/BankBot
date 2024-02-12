import os
from flask import Flask, request
from middlewares.process_audio import process_audio

app = Flask(__name__)

# Specify the folder to save audio files
audio_folder = "audio_files"

# Ensure the audio folder exists
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

@app.route('/audio/save', methods=['POST'])
def save_audio():
    try:
        audio_data = process_audio(request=request)

        filename = os.path.join(audio_folder, "audio_file.mp3")
        with open(filename, 'wb') as file:
            file.write(audio_data)
        
        result = f"Received and saved audio data to {filename}."

        return result, 200
        
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
