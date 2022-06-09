from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank = []

for q in question_data:
    q_bank.append(Question(q["text"], q["answer"]))

q_brain = QuizBrain(q_bank)
while q_brain.still_has_questions():
    q_brain.next_q()

q_brain.print_final_score()