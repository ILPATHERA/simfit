from flask import Flask, render_template, request, redirect, url_for, session
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64
import os

app = Flask(__name__)

# Generiere eine zufällige Zeichenfolge mit ausreichender Länge (z.B. 24 Zeichen)
secret_key = os.urandom(24)

# Konvertiere die Bytes in eine hexadezimale Zeichenfolge
secret_key_hex = secret_key.hex()

print("Generierte secret_key:", secret_key_hex)

# Aktiviere die Flask-Session
app.secret_key = secret_key_hex

# Diese Variable wird verwendet, um den Nachrichtentext auf der Bestätigungsseite festzulegen
confirmation_message = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def contact():
    global confirmation_message  # Zugriff auf die globale Variable

    if request.method == 'POST':
        # Informationen aus dem Formular erfassen
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # E-Mail-Versand
        smtp_server = "smtp.office365.com"  # Beispiel: smtp.gmail.com für Gmail
        smtp_port = 587  # Beispielport für TLS
        smtp_user = "patheracoaching@outlook.com"  # Deine E-Mail-Adresse
        smtp_password = "Coaching2023!"  # Dein E-Mail-Passwort

        subject = f"Neue Nachricht von {name}"
        body = f"Name: {name}\nE-Mail: {email}\n\nNachricht:\n{message}"

        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))

        msg['From'] = smtp_user
        msg['To'] = "patheracoaching@outlook.com"  # Empfänger-E-Mail-Adresse
        msg['Subject'] = subject

        try:
            # Verbindung zum SMTP-Server herstellen
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            # Anmeldung am SMTP-Server
            server.login(smtp_user, smtp_password)

            # E-Mail senden
            server.sendmail(smtp_user, ['patheracoaching@outlook.com'], msg.as_string())

            # Verbindung schließen
            server.quit()

            # Setze die Bestätigungsnachricht entsprechend
            confirmation_message = 'Deine Nachricht wurde erfolgreich gesendet!'
            return redirect(url_for('confirmation'))
        except Exception as e:
            print(f"Fehler beim Senden der E-Mail: {str(e)}")
            confirmation_message = 'Oops, da ist etwas schief gelaufen!'
            return redirect(url_for('error'))
        
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    if request.method == 'POST':
        # Informationen aus dem Formular erfassen
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        emailreg = request.form['emailreg']
        genderselect = request.form['genderselect']
        alter = request.form['alter']
        groesse = request.form['groesse']
        gewicht = request.form['gewicht']
        beruf = request.form['beruf']
        tagesablauf = request.form['tagesablauf']
        wasessen = request.form['wasessen']
        wasessenzeit = request.form['wasessenzeit']
        vielesseroderwenigesser = request.form['vielesseroderwenigesser']
        supps = request.form['supps']
        gewohnheitessen = request.form['gewohnheitessen']
        allergie = request.form['allergie']
        abnehmenOderZunehmen = request.form['abnehmenOderZunehmen']
        trainingshaufigkeit = request.form['trainingshaufigkeit']
        wohlbefinden = request.form['wohlbefinden']
        wunsche = request.form['wunsche']
        ziel = request.form['ziel']
        zielart = request.form['zielart']
        bemerkung = request.form['bemerkung']
        #images = request.files.getlist('imageidol')

        # E-Mail-Versand
        smtp_server = "smtp.office365.com"
        smtp_port = 587
        smtp_user = "patheracoaching@outlook.com"  # Deine E-Mail-Adresse
        smtp_password = "Coaching2023!"  # Dein E-Mail-Passwort

##        image_tags = ""
##        for image in images:
##            if image.filename != '':
#                image_data = image.read()
#                image_mime_type = image.content_type
##                image_name = image.filename
##                
##                # Bild in Base64 kodieren
##                image_data_base64 = base64.b64encode(image_data).decode('utf-8')
##                
##                # HTML-Tags für das Bild erstellen
##                image_tags += f'<p><strong>{image_name}</strong></p>'
#                image_tags += f'<img src="data:{image_mime_type};base64,{image_data_base64}" />'

        subject = f"Neue Registrierung von {vorname} {nachname}"
        body = f"Vorname: {vorname}\n" \
            f"Nachname: {nachname}\n" \
            f"Email: {emailreg}\n" \
            f"Geschlecht: {genderselect}\n" \
            f"Alter: {alter}\n" \
            f"Größe (cm): {groesse}\n" \
            f"Aktuelles Gewicht (kg): {gewicht}\n" \
            f"Beruf und Bewegung im Alltag:\n{beruf}\n" \
            f"Grober Tagesablauf:\n{tagesablauf}\n" \
            f"Was isst du gerne?\n{wasessen}\n" \
            f"Was isst du zurzeit?\n{wasessenzeit}\n" \
            f"Essverhalten: {vielesseroderwenigesser}\n" \
            f"Supplements:\n{supps}\n" \
            f"Aktuelle Ernährungsgewohnheiten:\n{gewohnheitessen}\n" \
            f"Allergien/Unverträglichkeiten:\n{allergie}\n" \
            f"Stoffwechseltyp: {abnehmenOderZunehmen}\n" \
            f"Trainingshäufigkeit (Sportart, Wochentage, Dauer):\n{trainingshaufigkeit}\n" \
            f"Aktuelles Wohlbefinden:\n{wohlbefinden}\n" \
            f"Spezielle Wünsche oder Anmerkungen:\n{wunsche}\n" \
            f"Ziel:\n{ziel}\n" \
            f"Zielart: {zielart}\n" \
            f"Sonstiges/Bemerkungen:\n{bemerkung}"

        body += "\nBilder:\n" + image_tags

        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))

        msg['From'] = smtp_user
        msg['To'] = smtp_user  # Empfänger-E-Mail-Adresse ist dieselbe wie Absender
        msg['Subject'] = subject

        try:
            # Verbindung zum SMTP-Server herstellen
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            # Anmeldung am SMTP-Server
            server.login(smtp_user, smtp_password)

            # E-Mail senden
            server.sendmail(smtp_user, [smtp_user], msg.as_string())

            # Verbindung schließen
            server.quit()

            return "Deine Registrierung wurde erfolgreich versendet!"
        except Exception as e:
            print(f"Fehler beim Senden der E-Mail: {str(e)}")
            return "Oops, da ist etwas schief gelaufen!"
        
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
