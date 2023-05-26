from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for key in question_data:
    question_text = key['question']
    question_answer = key['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


