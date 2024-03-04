import requests
from flask import Flask, render_template,request as req

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = req.form["data"]
        maxL = int(req.form["maxL"])
        minL = maxL // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "min_length": minL,
            "max_length": maxL
        })

        return render_template("index.html", result=output[0]["summary_text"])
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.debug = True
    app.run()
