def chit_chat(auth_code):
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

    return response
