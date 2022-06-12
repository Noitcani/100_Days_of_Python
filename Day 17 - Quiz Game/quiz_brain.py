class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def next_q(self):
        user_answer = input(f"Q.{self.q_number + 1}: {self.q_list[self.q_number].text} (True/False?) :  ")
        self.check_answer(user_answer, self.q_list[self.q_number].answer)
        self.q_number += 1

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are Correct!")
            self.score += 1

        else:
            print("That's Wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")

    def print_final_score(self):
        print("You've completed the quiz!")
        print(f"Your final score is {self.score}/{self.q_number}")
