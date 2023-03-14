from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your-email-address',
    MAIL_PASSWORD='your-email-password'
)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # send an email with the form data
    msg = Message('New contact form submission', sender=email, recipients=['your-email-address'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)
    
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)