from business.preprocessor import clean_text
from business.spam_detector import detect_spam
from business.ml_model import predict_category
from business.priority_classifier import assign_priority
from business.response_generator import generate_response
from data.db import get_connection
from business.email_sender import send_email


def process_email(content, sender_email=None):

    cleaned_text = clean_text(content)

    if detect_spam(cleaned_text):
        category = "Spam"
        priority = "Low"
        response = "This email has been marked as spam."
        send_reply = False
        send_to_admin = False

    else:
        category = predict_category(cleaned_text)
        priority = assign_priority(category)
        response = generate_response(category, cleaned_text)

        
        if category == "Complaint" or priority == "High":
            send_reply = False
            send_to_admin = True
        else:
            send_reply = True
            send_to_admin = False

    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO emails(content, cleaned_text, category, priority, response) VALUES (%s,%s,%s,%s,%s)",
        (content, cleaned_text, category, priority, response)
    )

    conn.commit()
    conn.close()

    
    if send_reply and sender_email:
        send_email(sender_email, response)

    
    if send_to_admin:
        admin_email = "puikatrovath@gmail.com"
        send_email(
         admin_email,
         "ADMIN ALERT: New Complaint",
          f"From: {sender_email}\n\nMessage:\n{content}"
   )

    return {
        "cleaned_text": cleaned_text,
        "category": category,
        "priority": priority,
        "response": response,
        "sent_to_admin": send_to_admin
    }