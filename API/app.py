import os
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from middlewares.process_audio import process_audio
from middlewares.speech_to_text import speech_to_text
from middlewares.text_to_speech import text_to_speech
from middlewares.chatbot import get_context

app = Flask(__name__)
CORS(app)

# Specify the folder to save audio files
directory=os.path.dirname(__file__)
directory= "/".join(directory.split("/")[:-1])
audio_folder = os.path.join(directory, "audio_files")
model_path= os.path.join(directory, "API", "vosk-model-small-en-in-0.4")

# Ensure the audio folder exists
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

@app.route('/api/v1/chatbot', methods=['POST'])
@cross_origin()
def chatbot():
    try:
        audio_file_path = process_audio(request, audio_folder)
        transcript_text = speech_to_text(input_file=audio_file_path, model_path=model_path)

        print("Transcript: ")
        print(transcript_text)

        ## some api calls to chatbot
        context = get_context(transcript_text)
        if context == 1:
            chatbot_response = "User Details"
        elif context == 2:
            chatbot_response = "Account Details"
        elif context == 3:
            chatbot_response = "Transfer Money"
        else:
            chatbot_response = "Normal Chit-Chat"
        ##
        output_file_path = os.path.join(audio_folder, "text2speech", "text2speech.wav")
        text_to_speech(chatbot_response, output_file_path)

        return send_file(output_file_path, mimetype="audio/wav"), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
