from app import app
from utils import get_prediction
from flask import Flask, jsonify, request


@app.route("/predict", methods=["POST"])
def predict():
    message = request.
    class_id, class_name = get_prediction(message)
    return jsonify({"class_id": class_id, "class_name": class_name})


if __name__ == "__main__":
    app.run(port=5001)
