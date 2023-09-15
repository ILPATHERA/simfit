from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

# Diese Variable wird verwendet, um den Nachrichtentext auf der Bestätigungsseite festzulegen
confirmation_message = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # E-Mail-Versand
    smtp_server = "smtp.office365.com"  # Beispiel: smtp.gmail.com für Gmail
    smtp_port = 587  # Beispielport für TLS
    smtp_user = "patheracoaching@outlook.com"
    smtp_password = "Coaching2023!"

    subject = f"Neue Nachricht von {name}"
    body = f"Name: {name}\nE-Mail: {email}\n\nNachricht:\n{message}"

    try:
        # Verbindung zum SMTP-Server herstellen
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Anmeldung am SMTP-Server
        server.login(smtp_user, smtp_password)
        
        # E-Mail senden
        server.sendmail(smtp_user, ['patheracoaching@outlook.com'], body)
        
        # Verbindung schließen
        server.quit()
        
        # Wenn die Nachricht erfolgreich gesendet wurde
        global confirmation_message
        confirmation_message = 'Deine Nachricht wurde erfolgreich gesendet!'
        return redirect(url_for('confirmation'))
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {str(e)}")
        return redirect(url_for('error'))

@app.route('/confirmation')
def confirmation():
    global confirmation_message
    message = confirmation_message
    confirmation_message = None  # Zurücksetzen der Nachricht nach der Anzeige
    return render_template('confirmation.html', message=message)

@app.route('/error')
def error():
    message = 'Oops, da ist etwas schief gelaufen!'
    return render_template('confirmation.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
