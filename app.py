from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)

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
def registration():
    if request.method == 'POST':
        # Informationen aus dem ersten Formular erfassen
        first_name = request.form['textField1']
        gender = request.form['genderselect']
        height = request.form['textField4']
        job_and_daily_activity = request.form['textField5']
        daily_schedule = request.form['textField6']
        favorite_foods = request.form['textField7']
        metabolism_type = request.form['abnehmenOderZunehmen']
        favorite_foods_2 = request.form['textField8']
        well_being = request.form['textField14']
        special_requests = request.form['textField16']

        # Informationen aus dem zweiten Formular erfassen
        last_name = request.form['lastname']
        weight = request.form['textField3']
        goal = request.form['abnehmenOderZunehmen']
        goal_description = request.form['textField10']
        image = request.files['image']  # Beachte das "files" Objekt für Datei-Uploads
        training_frequency = request.form['textField9']
        supplements = request.form['textField11']
        eating_habits = request.form['vielesseroderwenigesser']
        current_diet_habits = request.form['textField12']
        allergies_intolerances = request.form['textField13']
        other_comments = request.form['textField15']

        # Kombinierte Daten aus beiden Formularen
        combined_data = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'height': height,
            'job_and_daily_activity': job_and_daily_activity,
            'daily_schedule': daily_schedule,
            'favorite_foods': favorite_foods,
            'metabolism_type': metabolism_type,
            'favorite_foods_2': favorite_foods_2,
            'well_being': well_being,
            'special_requests': special_requests,
            'weight': weight,
            'goal': goal,
            'goal_description': goal_description,
            'image': image.filename if image else None,
            'training_frequency': training_frequency,
            'supplements': supplements,
            'eating_habits': eating_habits,
            'current_diet_habits': current_diet_habits,
            'allergies_intolerances': allergies_intolerances,
            'other_comments': other_comments
        }

            # Kombinierte Daten aus beiden Formularen
        combined_data = f"""Vorname: {first_name}
            Nachname: {last_name}
            Geschlecht: {gender}
            Größe (cm): {height}
            Beruf und Bewegung im Alltag:
            {job_and_daily_activity}
            Grober Tagesablauf:
            {daily_schedule}
            Was isst du gerne?
            {favorite_foods}
            Stoffwechseltyp: {metabolism_type}
            Was isst du gerne?
            {favorite_foods_2}
            Aktuelles Wohlbefinden:
            {well_being}
            Spezielle Wünsche oder Anmerkungen:
            {special_requests}
            Aktuelles Gewicht (kg): {weight}
            Ziel: {goal}
            Dein Ziel und optional ein Bild deines Ziels:
            {goal_description}
            Trainingshäufigkeit (Sportart, Wochentage, Dauer):
            {training_frequency}
            Supplements:
            {supplements}
            Essverhalten: {eating_habits}
            Aktuelle Ernährungsgewohnheiten:
            {current_diet_habits}
            Allergien/Unverträglichkeiten:
            {allergies_intolerances}
            Sonstiges/Bemerkungen:
            {other_comments}
            """

# Jetzt enthält "combined_data" den kombinierten Text mit allen Formulardaten
# Du kannst diesen Text dann entsprechend verwenden, z.B. für eine E-Mail oder andere Verarbeitungen.


        # Betreff für die E-Mail
        subject = "Neue Anmeldung"

        # Rest des E-Mail-Texts und Verarbeitung der Daten...

        return redirect(url_for('confirmation'))



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
