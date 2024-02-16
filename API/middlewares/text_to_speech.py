import subprocess
import os


def text_to_speech(input_text, output_file):
    directory = os.path.dirname(__file__)
    directory = "/".join(directory.split("/")[:-1])
    piper_path = os.path.join(directory, "piper", "piper", "piper")
    model_path = os.path.join(directory, "piper", "en_US-kathleen-low.onnx")
    output_file = os.path.join(directory, output_file)
    command = f'echo "{input_text}" |  {piper_path} --model {model_path} --output_file {output_file}'
    print(command)
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    input_file = "hello sourabh this is kathleen"
    output_file = "output.wav"

    text_to_speech(input_file, output_file)
