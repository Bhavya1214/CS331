CORE EMAIL PROCESSING USE CASES

1. Receive Email:<br> 
   The system receives incoming emails from the email server.<br>
2. Pre-process Email Content:<br> 
   Clean and prepare email data (remove noise, formatting, stopwords).<br>
3. Analyse Email Content:<br> 
   Understand the subject and body of the email.<br>
4. Detect Email Content:<br> 
   Identify keywords, intent, and patterns.<br>
5. Classify Emails:<br> 
   Categorize emails (inquiry, complaint, request, spam, etc.).<br>
6. Assign Priority:<br>
   Assign high, medium, or low priority based on urgency.<br>
7. Detect Spam:<br>
   Identify spam emails.<br>
8. Block Malicious Emails:<br>
   Prevent harmful or suspicious emails.<br>
9. Generate Automated Response:<br>
   Create predefined or intelligent responses.<br>
10. Send Automated Reply:<br>
    Send a reply to the email sender.<br>

EXCEPTION AND ERROR HANDLING USE CASES

1. Handle Email Fetch Failure:<br>
   Manage failure while fetching emails.<br>
2. Retry Email Delivery:<br>
   Retry sending the email if delivery fails.<br>
3. Forward Email to Admin:<br>
   Escalate unhandled or critical emails.<br>
4. Notify Admin on System Error:<br>
   Inform the admin when system errors occur.<br>

ADMINISTRATIVE AND MANAGEMENT USE CASES

1. Manage Responses:<br>
   Create/update automated response templates.<br>
2. Update Classification Rules:<br>
   Modify rule-based email classification.<br>
3. Train / Update ML Model:<br>
   Train or improve ML-based classifier.<br>
4. View System Reports:<br>
   View logs, analytics, and processing reports.<br>
5. Review Escalated Reports:<br>
   Review emails forwarded to the admin.<br>
6. Configure Email Server:<br>
   Configure IMAP/SMTP settings.<br>
7. Secure Email Access:<br>
   Ensure secure access to the email server.<br>
8. Log Email Activity:<br>
   Maintain logs of all email operations.<br

ACTOR <---> USE CASE RELATIONSHIPS (Associations)

USER (Email Sender)
1. Receive Emails
2. Send Automated Reply (receives reply from system)

ADMIN
1. Manage Responses
2. Update Classification Rules
3. Train / Update ML Model
4. View System Reports
5. Review Escalated Reports
6. Configure Email Server
7. Secure Email Access
8. Notify Admin on System Error

EMAIL SERVER(IMAP/SMTP)
1. Send Automated Reply
2. Retry Email Delivery
3. Handle Email Fetch Failure
4. Receive Emails

USE CASE <---> USE CASE RELATIONSHIPS<br>

1. Analyse Email Content       << include >>       Pre-process Email Content.<br>
2. Analyse Email Content       << include >>       Detect Email Content.<br>
3. Analyse Email Content       << include >>       Classify Emails.<br>
4. Analyse Email Content       << include >>       Assign Priority.<br>
5. Classify Emails             << include >>       Detect Spam.<br>
6. Generate Automated Response << include >>       Send Automated Reply.<br>
7. Send Automated Reply        << include >>       Log Email Activity.<br>



