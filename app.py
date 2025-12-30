from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Doctor Duha thank you so much for instructing me to show you my potential DevOps CI/CD Project - GitHub Actions + Docker + EC2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
