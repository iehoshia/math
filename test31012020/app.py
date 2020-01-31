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
    for i in range(0,100):
        for j in range (2, i-1):
            tmp = i % j
            is_prime = True
            if tmp == 0:
                is_prime = False
                datas.append([i, "IS NOT PRIME"])
                break
            if is_prime:
                datas.append([i, "IS PRIME"])

        #datas.append(i)
    return render_template('ciclofor.html',
        datas=datas)

if __name__ == '__main__':
    app.run(port=8002, host='0.0.0.0', debug=True)

