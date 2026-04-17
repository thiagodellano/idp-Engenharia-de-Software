from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# carregar modelo
model = pickle.load(open("modelo.pkl", "rb"))

@app.route("/")
def home():
    return "API rodando!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = [
        data["PT08.S1(CO)"],
        data["NMHC(GT)"], 
        data["C6H6(GT)"],
        data["PT08.S2(NMHC)"],
        data["NOx(GT)"],
        data["PT08.S3(NOx)"],
        data["NO2(GT)"],
        data["PT08.S4(NO2)"],
        data["PT08.S5(O3)"],
        data["T"],
        data["RH"],
        data["AH"]
    ]

    prediction = model.predict([features])[0]

    if prediction <= 4:
        classificacao = "bom"
    elif prediction <= 9:
        classificacao = "medio"
    else:
        classificacao = "ruim"

    return jsonify({
        "predicted_CO": float(prediction),
        "classificacao": classificacao
    })


if __name__ == "__main__":
    app.run(debug=True)