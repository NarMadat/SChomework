from quiz import Quiz
from models import Question
from data import questions_data

question_bank = [Question(q["question"], q["correct_answer"]) for q in questions_data]
quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("End victorina")
print(f"Your score is {quiz.score}/{len(question_bank)}")
