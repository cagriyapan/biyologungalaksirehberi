from flask import Flask
from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route ('/deneme1')
def deneme1():
    return 'başarılı'
@app.route('/content/<topic>')
def content(topic):
    return render_template('page.html',topic=topic)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0 ')

