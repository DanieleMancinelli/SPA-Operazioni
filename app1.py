from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Server web-codice per restituire la homepage 
@app.route("/")
def homepage():
    return render_template("homepage_get.html")

# Server API - Modifica per usare GET
@app.route("/calcola", methods=["GET"])
def calcola():
    # Recupero i dati dalla query string
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operazione = request.args.get('operazione')

    # Verifica se i dati sono presenti
    if num1 is None or num2 is None or operazione is None:
        return jsonify(risultato="Mancano i dati"), 400  # Ritorna un errore se mancano i dati

    # Elaborazione delle informazioni
    if operazione == 'addizione':
        risultato = num1 + num2
    elif operazione == 'sottrazione':
        risultato = num1 - num2
    elif operazione == 'moltiplicazione':
        risultato = num1 * num2
    elif operazione == 'divisione':
        if num2 == 0:
            return jsonify(risultato="Errore: divisione per zero"), 400
        risultato = num1 / num2
    else:
        return jsonify(risultato="Operazione non valida"), 400

    # Restituisco il risultato al frontend
    return jsonify(risultato=risultato)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)
