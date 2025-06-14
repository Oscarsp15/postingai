from flask import Flask, render_template,redirect,request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_webhook():
    if request.method == "POST":
        data = request.get_json()
        print("📩 Webhook recibido:", data)
        return jsonify({"status": "Webhook recibido"}), 200
    return "Webhook activo", 200

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
