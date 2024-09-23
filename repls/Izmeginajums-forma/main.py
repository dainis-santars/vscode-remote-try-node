from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_numbers():
    error = ''
    result = None
    try:
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = a + b
    except ValueError:
        error = 'Please provide two integers.'

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
