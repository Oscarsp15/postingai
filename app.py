from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AnimePostAI</h1><p>Bienvenido a la app de pruebas.</p>"

@app.route("/terms.html")
def terms():
    return render_template("terms.html")

@app.route("/privacy.html")
def privacy():
    return render_template("privacy.html")

@app.route("/tiktok-verification.html")
def tiktok_verification():
    return render_template("tiktok-verification.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
