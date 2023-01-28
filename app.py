from flask import Flask, request, jsonify
import tensorflow as tf
from flask import render_template
import os


app = Flask(__name__)

model_path = "model/model_train2.h5"
if os.path.exists(model_path):
    print("Model exists at: ", model_path)
else:
    print("Model not found at: ", model_path)

model = tf.keras.models.load_model("model/model_train2.h5")



##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/classify", methods=["POST"])
def classify():
    # Get the data from the request
    data = request.get_json()

    # Make a prediction using the model
    prediction = model.predict(data)

    # Return the prediction as a response
    return jsonify({"prediction": prediction.tolist()})


##########################################################################
## Main
##########################################################################

if __name__ == "__main__":
    app.run(debug=True)
