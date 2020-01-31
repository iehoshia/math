from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html',
   	name='JOSIAS')

@app.route('/city')
def city():
   return render_template('city.html',
   	city='Xela')

@app.route('/phone')
def phone():
   return render_template('phone.html',
   	phone='5550000')

if __name__ == '__main__':
   app.run(port=8002, host='0.0.0.0', debug=True)