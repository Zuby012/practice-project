# Utility function to calculate score from user answers
from random import randint
import time
from flask import Flask, request


def calculate_user_score(request_obj, answer_key, num_questions):
    """
    Calculate the user's score based on submitted answers.
    Args:
        request_obj: Flask request object (use request.form for POST)
        answer_key: List of correct answers (strings)
        num_questions: Number of questions in the test
    Returns:
        Tuple: (score, user_answers_list)
    """
    user_answers = []
    score = 0
    for i in range(1, num_questions + 1):
        user_answer = request_obj.form.get(f'q{i}')
        user_answers.append(user_answer)
        if user_answer and user_answer == answer_key[i-1]:
            score += 1
    return score, user_answers


class English_Best_Meaning:
    questions = [
        "In the match against the uplanders team, the sub mariners turned out to be the <u>dark horse</u>",
        "Only the <u>small fry</u> get punished for such social misdemeanors",
        "He spoke with <u>his heart in his mouth</u>",
        "The <u>leader</u> in today's issue of our popular newspaper focuses on inflation",
        "From the ways my friend talks, you can see he is such <u>a bore</u>",
    ]
    options = [
        {
            "key1": "won unexpectedly",
            "key2": "played most brilliantly",
            "key3": "played below their usual form",
            "key4": "lost as expected"
        },
        {
            "key1": "small boys",
            "key2": "unimportant people",
            "key3": "frightened people",
            "key4": "inexperienced people"
        },
        {
            "key1": "courageously",
            "key2": "with such unusual cowardice",
            "key3": "with a lot of confusion in his speech",
            "key4": "with fright and agitation"
        },
        {
            "key1": "president",
            "key2": "headline",
            "key3": "editorial",
            "key4": "columnist"
        },
        {
            "key1": "rude",
            "key2": "brilliant",
            "key3": "uninteresting",
            "key4": "overbearing"
        },
    ]
    answers = [
        "won unexpectedly",
        "unimportant people",
        "with fright and agitation",
        "editorial",
        "uninteresting",
    ]


new_q = []
new_op = []
ans = []


def display_question(module_question, module_options, module_answer, html_body_array):
    """
    Generates random questions and display.
    Args:
        module_question: module, class or iterable containing questions
        module_options: module, class or iterable containing options
        module_answer: module, class or iterable containing answers
        html_body_array: Array which contains content for the page
    """

    q_num = 1  # Counter for question numbers

    display = "block"  # Initial display state for the first question

    previous_button = ""  # Initial state for the previous button
    # The previous button will be empty for the first question

    # Button to navigate to the next question
    next_button = "<button type=\"button\" class=\"submit-btn\" onclick=\"nextSlide()\">Next</button>"

# code to generate questions at random

    while True:
        new_qop_index = randint(0, len(module_question)-1)

        if module_question[new_qop_index] in new_q:
            pass
        else:
            new_q.append(module_question[new_qop_index])
            new_op.append(module_options[new_qop_index])
            ans.append(module_answer.answers[new_qop_index])

        if len(new_q) == len(module_question) and len(new_op) == len(module_options):
            break

    # Looping through each question in the English_Best_Meaning class
    # This will generate the HTML for each question and its options
    for q in new_q:

        # Creating the main question block with the current question number and text
        main_q = f'<div class=\"slide\" style=\"display:{display};\">\
            <div class=\"question\">\
            <strong>{q_num}. {q}</strong>\
            </div>\
            <ul class=\"options\">'

        # Adding the main question block to the test body
        html_body_array.append(main_q)

        # Looping through the options for each question
        for num in range(1, 5):
            # Constructing the option text based on the current question and option number
            op = new_op[new_q.index(q)][f"key{num}"]

            # Creating the HTML for each option
            option_itration = f'<li><label><input type=\"radio\" name=\"q{q_num}\" value=\"{op}\"> {op}</label></li>'

            # Adding the option HTML to the test body
            html_body_array.append(option_itration)

        # If it's the last question, we change the next button to a submit button
        if q_num == len(module_question) or q_num == 30:
            next_button = '<button class="submit-btn" type="submit">Submit Test</button>'

        block_end = f'</ul><div style=\"display: flex; justify-content: flex-end;\">\
            {previous_button}{next_button}\
            </div>\
            </div>'  # Closing the question block and adding the buttons

        # Adding the closing block to the test body
        html_body_array.append(block_end)

        q_num += 1  # Incrementing the question number for the next iteration

        if q_num > 1:  # If it's not the first question, we set the display to none and introduce the previous button
            display = "none"
            previous_button = '<button type="button" class="submit-btn" onclick="prevSlide()">Previous</button>'
        else:
            display = "block"


def calc_score(request_obj, result_page):  # function to calculate score and display it
    """
    Calculate the user's score based on submitted answers.
    Args:
        request_obj: Flask request object (use request.form for POST)
        result_page: array containing body of result page
    """

    user_answers = []

    score = 0
    for i in range(1, len(ans) + 1):
        user_answer = request_obj.form[f'q{i}']
        user_answers.append(user_answer)
        if user_answer and user_answer == ans[i-1]:
            score += 1

    main_body = f'<header>Test Submitted</header>\
                    <div class="container">\
                        <div class="result">\
                            <div class="score">Your Score: {score}/{len(ans)}</div>\
                            <p>Congratulations! You have completed the test.</p>\
                        </div>\
                        <a href="/dashboard" class="submit-btn">Back to Dashboard</a>\
                    </div>'

    result_page.append(main_body)
