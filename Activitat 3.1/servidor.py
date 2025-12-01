from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!!!"

@app.route('/suma', method = ['GET'])
def suma():
    numero1 = request.args.get('a')
    print(numero1)
    numero2 = request.args.get('b')
    print(numero2)
    suma = int(numero1) + int(numero2)
    
    return "la suma de " +numero1, "+" +numero2 + "es = ", str(suma)

if __name__ == '__main__':
    app.run(debug=True)


