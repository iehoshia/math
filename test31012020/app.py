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
   return render_template('phones.html',
    phone='5550000')

@app.route('/for')
def cyclefor():
    datas = []
    for i in range(2,100):
        is_prime = True
        for j in range (2, i-1):
            tmp = i % j
            if tmp == 0:
                is_prime = False
                break
        if is_prime:
            datas.append([i, "IS PRIME"])
        t = 5
        potencia = 1
        for i in range(1,50):
            print(potencia, t)
            potencia = potencia * t

    return render_template('ciclofor.html',
        datas=datas,
        potencia=potencia)

if __name__ == '__main__':
    app.run(port=8002, host='0.0.0.0', debug=True)

