

def get_responses(msg: str) -> str:
    user_msg = msg.lower()

    if user_msg == 'hi':
        return 'yahallo'

    return 'wako is a fraud'