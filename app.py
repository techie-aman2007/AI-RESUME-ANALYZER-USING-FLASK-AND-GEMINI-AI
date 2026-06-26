from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    resume = data["resume"]

    prompt = f"""
Analyze this resume.

Tell:

1. Summary

2. Strengths

3. Weaknesses

4. Missing Skills

5. Suggestions

Resume:

{resume}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({
        "result": response.text
    })

if __name__ == "__main__":
    app.run(debug=True)