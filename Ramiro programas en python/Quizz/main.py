from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Gui

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
interfaz = Gui(quiz)     # se le pasa como parametro quiz al objeto Gui
# while quiz.still_has_questions():
#     quiz.next_question()

print("Completaste el Quizz")
print(f"tu puntuacion final es: {quiz.score}/{quiz.question_number}")
