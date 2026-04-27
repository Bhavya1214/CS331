def generate_response(category, text):

    text = text.lower()

    if category == "Complaint":

        if "delay" in text or "late" in text:
            return "We sincerely apologize for the delay. We are working to resolve this issue as quickly as possible."

        elif "damaged" in text or "broken" in text:
            return "We are sorry to hear that your product was damaged. We will arrange a replacement or refund immediately."

        elif "bad" in text or "poor" in text:
            return "We regret your experience. Your feedback is important and we will improve our service."

        else:
            return "We apologize for the inconvenience. Our team will resolve your issue soon."


    elif category == "Request":

        if "refund" in text:
            return "Your refund request has been received and will be processed shortly."

        elif "password" in text:
            return "You can reset your password using the account recovery option."

        else:
            return "Your request has been received and our team will assist you soon."


    elif category == "Inquiry":

        if "price" in text or "cost" in text:
            return "Our pricing details are available on our website. Please check for more information."

        elif "details" in text:
            return "We will provide you with detailed information shortly."

        else:
            return "Thank you for your inquiry. We will get back to you soon."


    else:
        return "This email has been marked as spam."