def detect_spam(text):
    spam_keywords = ["win", "free", "prize", "click"]
    return any(word in text for word in spam_keywords)