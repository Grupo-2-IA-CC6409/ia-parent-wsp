from flask import Flask
from transformers import pipeline

MODEL_PATH = "pretrained-model"

app = Flask(__name__)
model = pipeline("text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH)
