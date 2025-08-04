# importing Flask and other necessary modules
from flask import Flask, render_template, url_for, request
# Importing the English_Best_Meaning class from questions.py
from questions import English_Best_Meaning as ebm

app = Flask(__name__)  # Creating an instance of the Flask class

test_body = []  # This will hold the HTML content for the test

q_num = 1  # Counter for question numbers

display = "block"  # Initial display state for the first question
previous_button = ""  # Initial state for the previous button
# The previous button will be empty for the first question

# Button to navigate to the next question
next_button = "<button type=\"button\" class=\"submit-btn\" onclick=\"nextSlide()\">Next</button>"

# Looping through each question in the English_Best_Meaning class
# This will generate the HTML for each question and its options
for q in ebm.questions:

    # Creating the main question block with the current question number and text
    main_q = f'<div class=\"slide\" style=\"display:{display};\">\
        <div class=\"question\">\
        <strong>{q_num}. {q}</strong>\
        </div>\
        <ul class=\"options\">'

    test_body.append(main_q)  # Adding the main question block to the test body

    # Looping through the options for each question
    for num in range(1, 5):
        # Constructing the option text based on the current question and option number
        op = ebm.options[ebm.questions.index(q)][f"key{num}"]

        # Creating the HTML for each option
        option_itration = f'<li><label><input type=\"radio\" name=\"q{q_num}\" value={op}> {op}</label></li>'

        # Adding the option HTML to the test body
        test_body.append(option_itration)

    # If it's the last question, we change the next button to a submit button
    if q_num == len(ebm.questions) or q_num == 30:
        next_button = '<button class="submit-btn" type="submit">Submit Test</button>'

    block_end = f'</ul><div style=\"display: flex; justify-content: flex-end;\">\
        {previous_button}{next_button}\
        </div>\
        </div>'  # Closing the question block and adding the buttons

    test_body.append(block_end)  # Adding the closing block to the test body

    q_num += 1  # Incrementing the question number for the next iteration

    if q_num > 1:  # If it's not the first question, we set the display to none and introduce the previous button
        display = "none"
        previous_button = '<button type="button" class="submit-btn" onclick="prevSlide()">Previous</button>'
    else:
        display = "block"

# print(test_body)


@app.route("/")  # Route for the home page
@app.route("/dashboard")  # Route for the dashboard
def dashboard():
    return render_template("dashboard.html")


@app.route("/test")  # Route for the test page
def test_page():
    return render_template("test.html", dynamic_items=test_body)


@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html")


if __name__ == "__main__":  # Main entry point of the application
    # Running the Flask application with debug mode enabled
    app.run(debug=True)
