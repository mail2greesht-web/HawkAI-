from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 HawkAI Server is Running</h1>
    <h2>AI CCTV Monitoring System</h2>
    <p>Render deployment successful.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)