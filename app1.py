from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Server web - codice per restituire la homepage
@app.route("/")
def homepage():
    return render_template("homepage_get.html")

# Server API per calcoli
@app.route("/calcola", methods=["GET"])
def calcola():
    # Prendo le informazioni dal front end
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operazione = request.args.get('operazione')
    
    # Verifico che i dati siano presenti e validi
    if num1 is not None and num2 is not None and operazione:
        if operazione == 'addizione':
            risultato = num1 + num2
        elif operazione == 'sottrazione':
            risultato = num1 - num2
        elif operazione == 'moltiplicazione':
            risultato = num1 * num2
        elif operazione == 'divisione':
            if num2 != 0:
                risultato = num1 / num2
            else:
                return jsonify(risultato="Errore: divisione per zero")
        else:
            return jsonify(risultato="Operazione non valida")
        
        # Restituisco il risultato al front end
        return jsonify(risultato=risultato)
    else:
        return jsonify(risultato="Mancano i dati")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)