from flask import Flask, render_template, request
import pickle


app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('flight_delay.pickle', 'rb'))


@app.route('/')
def Home():
    return render_template('index.html')


# @app.route("/sub", methods=['POST'])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]

#     return render_template("sub.html", n=name)

@app.route("/add", methods=['POST'])
def predict():
    if request.method == 'POST':
        flight = float(request.form['fl'])
        origin = float(request.form['or'])

        prediction = model.predict([[flight, origin]])
        pred = prediction[0]
        out = "Error"
        if pred == 1:
            out = "Flight Delayed"
        else:
            out = "Flight is on time"

        return render_template('index.html', results=out)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
