import ollama 

def chit_chat(query):
    prompt_template = """
    Your name is Somu Bot. You are a professional banking chatbot. You help users to get them user details, account details
    transfer money and normal conversation. Below is the query given by user. Answer the query and ask how can you help them.
    Query: {query}

    Response: 
    """
    try:
        prompt = prompt_template.format(query=query)
        print(prompt)
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}],
        )

    except Exception as e:
        print(e)

    return response["message"]["content"]

    return response
