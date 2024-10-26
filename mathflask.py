from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_problem", methods=["POST"])
def generate_problem():
    data = request.get_json()
    num_digits = int(data["num_digits"])
    operation = data["operation"]

    if operation == "addition":
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        problem = f"What is {num1} + {num2}? "
        solution = num1 + num2
    elif operation == "subtraction":
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        problem = f"What is {num1} - {num2}? "
        solution = num1 - num2

    return jsonify({"problem": problem, "solution": solution})

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    user_answer = int(data["user_answer"])
    solution = int(data["solution"])

    if user_answer == solution:
        result = "Correct!"
    else:
        result = f"Sorry, the correct answer is {solution}."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_problem", methods=["POST"])
def generate_problem():
    data = request.get_json()
    num_digits = int(data["num_digits"])
    operation = data["operation"]

    if operation == "addition":
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        problem = f"What is {num1} + {num2}? "
        solution = num1 + num2
    elif operation == "subtraction":
        num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        problem = f"What is {num1} - {num2}? "
        solution = num1 - num2

    return jsonify({"problem": problem, "solution": solution})

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    user_answer = int(data["user_answer"])
    solution = int(data["solution"])

    if user_answer == solution:
        result = "Correct!"
    else:
        result = f"Sorry, the correct answer is {solution}."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)