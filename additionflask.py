import tkinter as tk
import random

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Define the math practice game logic
class MathPractice:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.num_digits = None

    def generate_problem(self):
        self.num1 = random.randint(10**(self.num_digits-1), 10**self.num_digits - 1)
        self.num2 = random.randint(10**(self.num_digits-1), 10**self.num_digits - 1)
        return f"{self.num1} + {self.num2} = "

    def check_answer(self, user_answer):
        correct_answer = self.num1 + self.num2
        self.total_questions += 1
        if int(user_answer) == correct_answer:
            self.score += 1
            return "Correct!"
        else:
            return f"Incorrect. The answer is {correct_answer}"

# Create a MathPractice instance
math_practice = MathPractice()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_problem", methods=["POST"])
def generate_problem():
    num_digits = request.json["num_digits"]
    math_practice.num_digits = int(num_digits)
    problem = math_practice.generate_problem()
    return jsonify({"problem": problem})

@app.route("/check_answer", methods=["POST"])
def check_answer():
    user_answer = request.json["user_answer"]
    result = math_practice.check_answer(user_answer)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

class MathPractice:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Math Practice")
        self.score = 0
        self.total_questions = 0
        self.num_digits = None

        self.num_digits_window = tk.Tk()
        self.num_digits_window.title("Choose Number of Digits")

        tk.Label(self.num_digits_window, text="Choose the number of digits to add:").pack()

        self.num_digits_var = tk.StringVar(self.num_digits_window)
        self.num_digits_var.set("2")  # default value

        options = ["1", "2", "3"]
        option_menu = tk.OptionMenu(self.num_digits_window, self.num_digits_var, *options)
        option_menu.pack()

        def submit():
            self.num_digits = int(self.num_digits_var.get())
            self.num_digits_window.destroy()
            self.start_math_practice()

        submit_button = tk.Button(self.num_digits_window, text="Submit", command=submit)
        submit_button.pack()

        self.num_digits_window.mainloop()

    def start_math_practice(self):
        self.problem_label = tk.Label(self.window, font=("Arial", 20))
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.window, font=("Arial", 20))
        self.answer_entry.pack(pady=10)

        self.result_label = tk.Label(self.window, font=("Arial", 16))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.window, font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.generate_button = tk.Button(self.window, text="New Problem", command=self.generate_problem)
        self.generate_button.pack(pady=10)

        self.check_button = tk.Button(self.window, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.generate_problem()

        self.window.mainloop()

    def generate_problem(self):
        self.num1 = random.randint(10**(self.num_digits-1), 10**self.num_digits - 1)
        self.num2 = random.randint(10**(self.num_digits-1), 10**self.num_digits - 1)
        problem = f"{self.num1} + {self.num2} = "
        self.problem_label.config(text=problem)
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.num1 + self.num2
        self.total_questions += 1
        if int(user_answer) == correct_answer:
            self.score += 1
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Incorrect. The answer is {correct_answer}")
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
        self.generate_problem()

if __name__ == "__main__":
    math_practice = MathPractice()