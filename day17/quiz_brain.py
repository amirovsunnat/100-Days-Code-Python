class QuizBrain:
    """Quiz Brain class for asking question from user"""
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        """Giving question"""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_guess, current_question.answer)

    def check_answer(self, user_guess, answer):
        """Checks user guess whether it is true or not"""
        if user_guess.lower() == answer.lower():
            self.score += 1
            print(f"You got it. It is true.")
        else:
            print(f"You guessed wrong.")
        print(f"The correct answer: {answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")

    def still_has_question(self):
        """Maintaining to give question until user guess wrong or question come to end"""
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False
