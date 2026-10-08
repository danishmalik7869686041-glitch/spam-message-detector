from flask import Flask, render_template, request, jsonify
import pickle
import webbrowser
from threading import Timer

app = Flask(__name__)

with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid request."}), 400

    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    prediction = model.predict([message])[0]

    if prediction == 1:
        result = "Spam"
        confidence = model.predict_proba([message])[0][1] * 100
    else:
        result = "Not Spam"
        confidence = model.predict_proba([message])[0][0] * 100

    return jsonify({
        "result": result,
        "confidence": round(confidence, 2)
    })


def open_browser():
    webbrowser.open("http://127.0.0.1:5001")


if __name__ == "__main__":
    Timer(2, open_browser).start()
    app.run(debug=True, port=5001, use_reloader=False)