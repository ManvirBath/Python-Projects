from data import question_data 
from question_model import Question 
from quiz_brain import QuizBrain 

question_bank = []

for question in question_data:
    q = question['text']
    a = question['answer']
    new_question = Question(q,a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")

if (((quiz.score/quiz.question_number) * 100) >= 70):
    print(f"You passed! Your final score is {quiz.score}/{quiz.question_number}.")
else: 
    print(f"You failed. Your final score is {quiz.score}/{quiz.question_number}.")
