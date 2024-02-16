def transfer_money(sender, reciever, amount, password):
    try:
        response_template = "{amount} dollars successfully transfered from {sender}'s to {reciever}'s account"
        response = response_template.format(
            amount=amount,
            sender=sender,
            reciever=reciever,
        )
    except Exception as e:
        response = f"Cannot send money to {reciever} from your account. Check balance or try speaking clearly again"
        print(e)

    return response
