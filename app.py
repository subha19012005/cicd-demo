from flask import Flask, jsonify, request

def add(a, b):
  return a + b

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify({
"message": "CI/CD Demo Application",
"result": add(2, 3)
})

@app.route("/add")
def addition():
  a = int(request.args.get("a", 0))
  b = int(request.args.get("b", 0))
  return jsonify({"result": add(a, b)})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
