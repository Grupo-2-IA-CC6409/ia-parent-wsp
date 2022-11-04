from app import app, model
from flask import jsonify, request


@app.route("/predict", methods=["POST"])
def predict():
    json = request.get_json()
    if json is None:
        return jsonify({"error": "message not provided"})
    message = json["message"]
    prediction = model(message)[0]
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(port=5001)
