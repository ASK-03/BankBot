import ollama


def get_context(text):
    prompt_template = """
Carefully analyze the user's query and choose the most relevant intent from the options below, assigning its corresponding number.
Options:
    1. Get User Details
    2. Get account details
    3. Transfer money to another user
    4. Normal Chit-Chat

Example:
    If the query is a general chit-chat, like "Hey, how are you?" then the response should be 4
    If the query is specifically about user details, such as "What is my account number?" then the response should be 1
    If the query involves account details provided with an account number, like "My name is abhishek and password is '12345', give me the account details," then the response should be 2
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


def extract_args(query, type):
    json_object_keys = ""
    if type == 1:
        json_object_keys = '"auth_code"'
    elif type == 2:
        json_object_keys = '"name", "password"'
    elif type == 3:
        json_object_keys = '"sender", "reciever", "amount", "password"'

    prompt_template = """
    Carefully analyze the user's query and extract the arguments. Arguments that are best suited for the 
    json object keys {json_object_keys}. Return a json object only.

    EXAMPLE 1: 
        if the query is "Give me user details, auth code is 123" then the auth code should be 123
        if the query is "Tell me my account details, my name is Abhishek and password is 123", then the name is Abhishek and password is 123
        if the query is "Transfer 100 dollars to Abhishek from Sourabh, my password is 123", then senders is Sourabh, reciever is Abhishek, amount is 100 and password is 123 

    Stick to the keys name. donot change it strictly.
    Query: {query}

    Response: 
    """
    try:
        prompt = prompt_template.format(json_object_keys=json_object_keys, query=query)
        print(prompt)
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}],
        )

    except Exception as e:
        print(e)

    return response["message"]["content"]


if __name__ == "__main__":
    print(get_context("Hey how are you"))
