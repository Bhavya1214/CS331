def detect_spam(text):

    spam_keywords = [
        "win",
        "won",
        "lottery",
        "prize",
        "money",
        "click",
        "link",
        "free",
        "offer",
        "reward",
        "earn",
        "bonus",
        "congratulations"
    ]

    text = text.lower()

    for word in spam_keywords:
        if word in text:
            return True

    return False