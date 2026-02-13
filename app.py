from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# 🔐 API key will come from Render environment variable
SCALEDOWN_API_KEY = os.environ.get("SCALEDOWN_API_KEY")


def compress_text(context_text, user_prompt, level):
    url = "https://api.scaledown.xyz/compress/raw/"

    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    # Creative prompt engineering
    if level == "low":
        modified_prompt = user_prompt + " Provide a detailed and longer summary."
    elif level == "high":
        modified_prompt = user_prompt + " Provide a very short 2-3 line summary only."
    else:
        modified_prompt = user_prompt + " Provide a concise summary."

    data = {
        "prompt": modified_prompt,
        "context": context_text
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["results"]["compressed_prompt"]
    except Exception as e:
        return f"Error: {e}"


@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""

    if request.method == "POST":
        user_query = request.form["query"]
        level = request.form.get("level", "medium")

        with open("admissions_data.txt", "r", encoding="utf-8") as file:
            full_text = file.read()

        compressed_text = compress_text(full_text, user_query, level)
        response_text = compressed_text

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
