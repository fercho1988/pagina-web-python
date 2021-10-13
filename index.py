from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguaje')
def lenguaje():
    mislenguajes = ("PHP","PYTHON", "JAVA", "C#", "JAVASCRIPT", "PERL", "RUBY", "RUST")  
    return render_template('lenguaje.html', lenguaje=mislenguajes)
    
if __name__ == '__main__':
  app.run(debug=True, port=5017)
