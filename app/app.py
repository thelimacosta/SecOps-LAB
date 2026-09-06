from flask import Flask, jsonify

app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=()'
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    response.headers.pop('Server', None)
    return response


@app.route("/")
def home():
    return jsonify({"message": "SecOps-LAB API rodando com sucesso!"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)