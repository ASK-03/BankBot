from vosk import Model, KaldiRecognizer, SetLogLevel
from tqdm.notebook import tqdm
import wave
import os
import json

def transcript_file(input_file, model_path):

    # Check if file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(os.path.basename(input_file) + " not found")

    # Check if model path exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(os.path.basename(model_path) + " not found")

    # open audio file
    wf = wave.open(input_file, "rb")

    # check if wave file has the right properties
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise TypeError("Audio file must be WAV format mono PCM.")

    # Initialize model
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())

    # Get file size (to calculate progress bar)
    file_size = os.path.getsize(input_file)

    # Run transcription
    pbar = tqdm(total=file_size)

    # To store our results
    transcription = []

    while True:
        data = wf.readframes(4000) # use buffer of 4000
        pbar.update(len(data))
        if len(data) == 0:
            pbar.set_description("Transcription finished")
            break
        if rec.AcceptWaveform(data):
            # Convert json output to dict
            result_dict = json.loads(rec.Result())
            # Extract text values and append them to transcription list
            transcription.append(result_dict.get("text", ""))

    # Get final bits of audio and flush the pipeline
    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    transcription_text = ' '.join(transcription)

    return transcription_text


if __name__ == "__main__":
    
    directory=os.path.dirname(__file__)
    directory= "/".join(directory.split("/")[:-1])
    
    #model_path
    model_path= os.path.join(directory,"vosk-model-small-en-in-0.4")
    
    #input_path_wav
    input_path_wav= os.path.join(directory,"audio_files","audio_file.wav")
    
    hypothesis = transcript_file(input_path_wav, model_path)
    print(hypothesis)

