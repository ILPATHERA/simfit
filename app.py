from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # E-Mail-Versand für Outlook
        smtp_server = "smtp.office365.com"  # SMTP-Server für Outlook
        smtp_port = 587  # Port für TLS-Verschlüsselung
        smtp_user = "itssimfit@outlook.com"  # Deine Outlook-E-Mail-Adresse
        smtp_password = "Coaching2023!"  # Dein Outlook-Passwort

        subject = f"Neue Nachricht von {name}"
        body = f"Name: {name}\nE-Mail: {email}\n\nNachricht:\n{message}"

        try:
            # E-Mail erfolgreich gesendet
            message = f"Nachricht von {name} wurde erfolgreich gesendet!"
        except Exception as e:
            # Fehler beim Senden der Nachricht
            message = f"Fehler beim Senden der Nachricht: {str(e)}"

        return render_template('index.html', message=message)

    return redirect(url_for('index'))

# Starte die Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True)
