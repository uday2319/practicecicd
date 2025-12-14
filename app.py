from flask import Flask,jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return jsonify(message="Heeey there CI/CD working through github actions!")
if __name__=="__main__":
    app.run(debug=True)
    