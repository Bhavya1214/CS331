from email_dal import save_email, get_emails_by_category


# Save emails
save_email("user1@gmail.com", "You win lottery now")
save_email("user2@gmail.com", "I have a complaint")
save_email("user3@gmail.com", "Project meeting tomorrow")

# Fetch spam emails
emails = get_emails_by_category("Spam")

print("Spam Emails:")
for e in emails:
    print(e)