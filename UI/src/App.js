import React from "react";
import "./App.css";
import MicRecorder from "mic-recorder-to-mp3";
import axios from "axios";

const Mp3Recorder = new MicRecorder({ bitRate: 128 });

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isRecording: false,
      blobURL: "",
      responseBlobURL: "",
      isBlocked: false,
    };
  }

  start = () => {
    if (this.state.isBlocked) {
      console.log("Permission Denied");
    } else {
      Mp3Recorder.start()
        .then(() => {
          this.setState({ isRecording: true });
        })
        .catch((e) => console.error(e));
    }
  };

  stop = () => {
    Mp3Recorder.stop()
      .getMp3()
      .then(([buffer, blob]) => {
        const blobURL = URL.createObjectURL(blob);
        this.setState({ blobURL, isRecording: false });

        const formData = new FormData();
        formData.append("audio", blob, "filename");

        axios
          .post("http://127.0.0.1:5000/api/v1/chatbot", formData)
          .then((response) => {
            console.log("Audio uploaded successfully:", response.data.message);
            var responseBlobURL = URL.createObjectURL(response.data);
            this.setState({ responseBlobURL: responseBlobURL });
          })
          .catch((error) => {
            console.error("Error uploading audio:", error);
          });
      })
      .catch((e) => console.log(e));
  };

  componentDidMount() {
    navigator.getUserMedia(
      { audio: true },
      () => {
        console.log("Permission Granted");
        this.setState({ isBlocked: false });
      },
      () => {
        console.log("Permission Denied");
        this.setState({ isBlocked: true });
      }
    );
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <button onClick={this.start} disabled={this.state.isRecording}>
            Record
          </button>
          <button onClick={this.stop} disabled={!this.state.isRecording}>
            Stop
          </button>
          <audio src={this.state.blobURL} controls="controls" />
          {this.state.responseBlobURL && (
            <audio src={this.state.responseBlobURL} controls="controls" />
          )}
        </header>
      </div>
    );
  }
}

export default App;
