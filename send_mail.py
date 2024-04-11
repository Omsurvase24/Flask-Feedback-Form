import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login = '21f8307f55a32f'
    password = 'e1372a0d53a23b'
    message = f'''<h3>New Feedback Submission</h3><ul><li>Customer: {
        customer}</li> <li>Customer: {dealer}</li> <li>Customer: {rating}</li> <li>Customer: {comments}</li> </ul>'''

    sender_email = 'example1@example.com'
    receiver_email = 'example2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
