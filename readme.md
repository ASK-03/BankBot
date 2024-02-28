## Group Members

- Abhishek Singh Kushwaha (12140050)
- Kriti Gupta (12140940)
- Sourabh Dadore (12141580)

## LLM

- To start the Ollama LLM, use commands below:

  ```
  docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
  ```

  use this link (https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image) for reference

  Note: Make sure port 11434 is not in use by any other service

## API

To start API, use the following command:

- Change the directory to the API folder
  ```
      cd API
  ```
- First install the required packages using the following command:
  ```
      pip install -r requirements.txt
  ```
- Then run the following command:
  ```
      python app.py
  ```
- The API will be running on port 5000

## UI

To start the UI, use the following command:

- Change the directory to the UI folder
  ```
      cd UI
  ```
- Make sure to use npm version 12.11.1
- First install the required packages using the following command:
  ```
      npm install
  ```
- Then run the following command:
  ```
      npm start
  ```
- The UI will be running on port 3000

## Usage

- The chatbot can be used for normal chit-chat, asking the account details, to ask user details or to transfer money.

## Example

- General chit-chat - "Hey, how are you?"

- User details - "What is my account number?"

- Account details - "My name is abhishek and password is '12345', give me the account details,"

- Money transfer - "I want to transfer 1000 Rupees from my account to ABC user,"
