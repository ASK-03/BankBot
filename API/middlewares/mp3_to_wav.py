from pydub import AudioSegment
import os

def mp3_to_wav(source, output_path, skip=0, excerpt=False):

    sound = AudioSegment.from_mp3(source) 
    sound =  sound.split_to_mono()[0] 
    sound = sound.set_frame_rate(16000) 

    if excerpt:
        excrept = sound[skip*1000:skip*1000+30000] 
        excrept.export(output_path, format="wav")
    else:
        audio = sound[skip*1000:]
        audio.export(output_path, format="wav")

    return output_path



if __name__ == "__main__":
    directory=os.path.dirname(__file__)
    directory = "/".join(directory.split("/")[:-1])
    input_path = os.path.join(directory, "audio_files","audio_file.mp3")
    wave_file = mp3_to_wav(input_path,0,False)