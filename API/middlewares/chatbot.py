import ollama


def get_context(text):
    prompt_template = """
Carefully analyze the user's query and choose the most relevant intent from the options below, assigning its corresponding number.
Options:
    1. Get User Details
    2. Get account details given account number
    3. Transfer money to another user
    4. Normal Chit-Chat

Example:
    If the query is a general chit-chat, like "Hey, how are you?" then the response should be 4
    If the query is specifically about user details, such as "What is my account number?" then the response should be 1
    If the query involves account details provided with an account number, like "My account number is '12345', give me the account details," then the response should be 2
    If the query indicates a money transfer, such as "I want to transfer 1000 Rupees from my account to ABC user," then the response should be 3

Provide the response in a JSON object format with the key as "number" and the value as the corresponding number you think.
Ensure the response adheres to the specified pattern.

Query: {}

Response:
    """
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt_template.format(text)}],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    print(get_context("Hey how are you"))
