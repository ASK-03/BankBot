def transfer_money(auth_code):
    user_details = {
        "123": {
            "username": "Abhishek Singh Kushwaha",
            "account_number": "1234567890",
            "mobile_number": "7428368001",
        },
        "234": {
            "username": "Sourabh Dadore",
            "account_number": "2345678901",
            "mobile_number": "7428368002",
        },
    }
    try:
        response_template = "The username of the requested user is {username}, account number is {account_number} and mobile number is {mobile_number}"
        response = f"User with auth code: {auth_code} doesnot exist"
        if user_details.get(auth_code, -1) != -1:
            res = user_details[auth_code]
            username = res["username"]
            account_number = res["account_number"]
            mobile_number = res["mobile_number"]
            response = response_template.format(
                username=username,
                account_number=account_number,
                mobile_number=mobile_number,
            )
    except Exception as e:
        print(e)

    return response
