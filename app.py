from flask import Flask, render_template, request, jsonify
import joblib



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == "POST":
        MESSAGE = request.form.get("message")
        model = joblib.load("spam_model.pkl")
     
        pred = model.predict([MESSAGE])
        prob = model.predict_proba([MESSAGE])

        ham  = f"{prob[0][0]*100:.2f}"
        spam = f"{prob[0][1]*100:.2f}"
        
        if pred[0] == 'ham':
            pred = "not spam"
        else:
            pred = "spam"


        return jsonify({
            "success":True,
            "spam":spam,
            "ham":ham,
            "pred":pred
        })


if __name__ == "__main__":
    app.run(debug=True)
