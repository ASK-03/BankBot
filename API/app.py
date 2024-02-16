import os
import json
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from middlewares.process_audio import process_audio
from middlewares.speech_to_text import speech_to_text
from middlewares.text_to_speech import text_to_speech
from middlewares.chatbot import get_context, extract_args
from helpers.user_details import get_user_details
from helpers.account_details import get_account_details
from helpers.transfer_money import transfer_money
from helpers.normal_chit_chat import chit_chat

app = Flask(__name__)
CORS(app)

# Specify the folder to save audio files
directory = os.path.dirname(__file__)
directory = "/".join(directory.split("/")[:-1])
audio_folder = os.path.join(directory, "audio_files")
model_path = os.path.join(directory, "API", "vosk-model-small-en-in-0.4")

# Ensure the audio folder exists
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)


@app.route("/api/v1/chatbot", methods=["POST"])
@cross_origin()
def chatbot():
    try:
        audio_file_path = process_audio(request, audio_folder)
        transcript_text = speech_to_text(
            input_file=audio_file_path, model_path=model_path
        )

        print("Transcript: ")
        print(transcript_text)

        ## some api calls to chatbot
        context = get_context(transcript_text)
        _context = json.loads(context)["number"]
        print(_context)

        if _context < 4:
            args = extract_args(transcript_text, _context)
            args = json.loads(args)

        if _context == 1:
            try:
                auth_code = args["auth_code"]
                chatbot_response = get_user_details(auth_code)
            except Exception as e:
                print(e)
                chatbot_response = "Cannot extract auth code from the voice, try speaking clearly" 
        elif _context == 2:
            try:
                name = args["name"]
                password = args["password"]
                chatbot_response = get_account_details(name, password)
            except Exception as e:
                print(e)
                chatbot_response = "Cannot fetch account details. Try speaking clearly"
        elif _context == 3:
            try: 
                sender = args["sender"]
                reciever = args["reciever"]
                amount = args["amount"]
                password = args["password"]
                chatbot_response = transfer_money(sender, reciever, amount, password)
            except Exception as e:
                print(e)
                chatbot_response = "Cannot transfer money! Try speaking clearly."
        else:
            try:
                chatbot_response = chit_chat(transcript_text)
            except Exception as e:
                print(e)
                chatbot_response = "Cannot reach the server now"
        ##
        try:
            output_file_path = os.path.join(audio_folder, "text2speech", "text2speech.wav")
            text_to_speech(chatbot_response, output_file_path)
        except Exception as e:
            print(e)

        return send_file(output_file_path, mimetype="audio/wav"), 200
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
