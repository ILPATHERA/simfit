from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diese Variable wird verwendet, um den Nachrichtentext auf der Bestätigungsseite festzulegen
confirmation_message = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def contact():
    # Hier würde Ihre E-Mail-Versand-Logik sein
    # ...

    # Wenn die Nachricht erfolgreich gesendet wurde
    global confirmation_message
    confirmation_message = 'Deine Nachricht wurde erfolgreich gesendet!'
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
    app.run(app.debug=True)
