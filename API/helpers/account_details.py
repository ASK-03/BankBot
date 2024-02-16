def get_account_details(name, password):
    user_details = {
        ("Jake", "one two three"): {
            "username": "Abhishek Singh Kushwaha",
            "account_number": "1234567890",
            "balance": "10000000000"
        },
        ("Sourabh", "two three four"): {
            "username": "Sourabh Dadore",
            "account_number": "2345678901",
            "balance": "1000000"
        },
    }
    try:
        response_template = "The username of the requested user is {username}, account number is {account_number} and balance is {balance}"
        response = f"User with name {name} and same password doesnot exist"
        if user_details.get((name, password), -1) != -1:
            res = user_details[(name, password)]
            username = res["username"]
            account_number = res["account_number"]
            balance = res["balance"]
            response = response_template.format(
                username=username,
                account_number=account_number,
                balance=balance,
            )
    except Exception as e:
        print(e)

    return response
