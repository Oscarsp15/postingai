from flask import Flask, render_template,redirect

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
    return redirect("static", "tiktokfc9Ny9rYK9nFRmkUXOJRNBZwiIph0YXc.txt",code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
