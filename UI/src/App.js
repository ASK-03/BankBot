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
      <>
        <div className="App">
          <div className="robot">
            <h1>Welcome to S.O.M.U Bankbot!</h1>
            <Lottie
              animationData={animationData}
              loop
              autoplay
              style={{ width: 600, height: 600 }}
            />
          </div>
          <div className="Getting-started">
            <div>
              <p>
                Introducing SOMU, your friendly neighborhood banker-bot with a
                twist! Ever felt like your rural banking experience needed a
                little extra pizzazz 🍕? Well, say hello to SOMU – the Socially
                Oriented Monetary Assistance Bankbot!
              </p>
              <p>
                Imagine this: You're strolling through the lush greenery of your
                village, pondering life's mysteries, when suddenly you remember
                you need to transfer some funds. But wait, there's no need to
                embark on a journey to the nearest bank, because SOMU is here to
                save the day! With SOMU, banking becomes a breeze and a barrel
                of laughs. Just strike up a conversation, spill the beans about
                your account details (don't worry, SOMU's got top-notch
                security🔐), toss in a pinch of authorization code, and voila!
                Your money's on the move faster than you can say 💸"cash me if
                you can."💸 So, whether you're chatting about crops, cows, or
                even the occasional cosmic conundrum, SOMU is your trusty
                sidekick, ready to make banking as easy as pie <span>🥧</span>
                (and twice as fun)!
              </p>
            </div>
            <div>
              <button onClick={Scroll} className="scrolldown">
                Getting Started
              </button>
            </div>
          </div>
        </div>
        <div className="App-header" id="App-header">
          <div className="instructions" id="inst">
            <h2>How to interact with Somu?</h2>
            <ul>
              <li>Click on the Speak button to interact.</li>
              <li>Once Done Click on the Stop button.</li>
              <li>Wait for the response from the Server.</li>
            </ul>
          </div>

          <div className="voicechat">
            <div className="header">
              Socially Oriented Monetary Assistance Bot
            </div>
            <div className="mainbody">
              <div className="Me">
                <span className="metxt">User</span>
                <audio src={this.state.blobURL} controls="controls" />
              </div>
              <div className="Bot">
                {this.state.responseBlobURL && (
                  <>
                    {" "}
                    <span className="bottxt">Bot</span>
                    <audio
                      src={this.state.responseBlobURL}
                      controls="controls"
                    />
                  </>
                )}
              </div>
            </div>
            <div className="footer">
              <button
                onClick={this.start}
                disabled={this.state.isRecording}
                className="start"
              >
                Speak
              </button>
              <button
                onClick={this.stop}
                disabled={!this.state.isRecording}
                className="stop"
              >
                Stop
              </button>
            </div>
          </div>
        </div>
      </>
    );
  }
}
export default App;

function Scroll() {
  var divElement = document.getElementById("App-header");
  divElement.scrollIntoView({ behavior: "smooth" });
}
