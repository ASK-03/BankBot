import React from "react";
import "./App.css";
import MicRecorder from "mic-recorder-to-mp3";
import axios from "axios";
import Lottie from "lottie-react";
import animationData from "./assets/robot.json";

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
          .post("http://127.0.0.1:5000/api/v1/chatbot", formData, {
            responseType: "blob",
          })
          .then((response) => {
            const blob = new Blob([response.data], { type: "audio/wav" });
            console.log(response);
            var responseBlobURL = URL.createObjectURL(blob);
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
        <div className="robot">
          <h1>Welcome to Somu Bankbot!</h1>
          <Lottie
            animationData={animationData}
            loop
            autoplay
            style={{ width: 600, height: 600 }}
          />
        </div>
        <div className="App-header">
          <div className="buttons">
            <button onClick={this.start} disabled={this.state.isRecording}>
              Speak
            </button>
            <button onClick={this.stop} disabled={!this.state.isRecording}>
              Stop
            </button>
            <audio src={this.state.blobURL} controls="controls" />
            {this.state.responseBlobURL && (
              <audio src={this.state.responseBlobURL} controls="controls" />
            )}
          </div>

          <div className="instructions">
            <h2>How to interact with Somu?</h2>
            <ul>
              <li>Click on the Speak button to interact.</li>
              <li>Once Done Click on the Stop button.</li>
              <li>Wait for the response from the Server.</li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
