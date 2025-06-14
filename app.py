from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AnimePostAI</h1><p>Bienvenido a la app de pruebas.</p>"

@app.route("/terms")
def terms():
    return render_template("terms")

@app.route("/privacy")
def privacy():
    return render_template("privacy")


@app.route("/tiktok-verification/")
def serve_verification_file():
    return send_from_directory("static", "tiktokrA8F27gchm0l2pg42SdnB00Cd2ZZP75cg.txt")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
