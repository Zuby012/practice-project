# importing Flask and other necessary modules
from flask import Flask, render_template, url_for, request
# Importing the English_Best_Meaning class from questions.py
from questions import calc_score, display_question, English_Best_Meaning as ebm

app = Flask(__name__)  # Creating an instance of the Flask class
app.config['SECRET_KEY'] = 'hwgrhfkuchdwfnkwrcurkhd'

test_body = []  # This will hold the HTML content for the test
english_test = []
maths_test = []
gen_sci = []
result_page = []


# print(test_body)


@app.route("/")  # Route for the home page
@app.route("/dashboard")  # Route for the dashboard
def dashboard():
    return render_template("dashboard.html")


display_question(ebm.questions, ebm.options, ebm, english_test)


@app.route("/english")  # Route for the english test page
def english_test_page():
    return render_template("english.html", dynamic_items=english_test)


@app.route("/general-sci")
def gen_sci_test_page():
    return render_template("gen_sci.html", dynamic_items=gen_sci)


@app.route("/maths")
def maths_test_page():
    return render_template("maths.html", dynamic_items=maths_test)


@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        calc_score(request, result_page)
    return render_template("result.html", dynamic_items=result_page)


if __name__ == "__main__":  # Main entry point of the application
    # Running the Flask application with debug mode enabled
    app.run(debug=True)
