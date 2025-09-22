from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

CSV_FILE = "data.csv"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-data")
def get_data():
    df = pd.read_csv(CSV_FILE)
    return df.to_json(orient="records")

@app.route("/save-data", methods=["POST"])
def save_data():
    data = request.json
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
