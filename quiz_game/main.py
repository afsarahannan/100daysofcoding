import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

game_over = False
questions_asked = 0
score = 0
question_index_list = []
question_bank = []

for question in question_data:
    question_text = question['text']
    answer_text = question['answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print(f"You've completed the quiz and your final score is {quiz.score}/{quiz.question_number}")


############################################################################################
# while questions_asked != len(question_data):
#     question_index = random.randint(0, len(question_data)-1)
#
#     if question_index not in question_index_list:
#         question_index_list.append(question_index)
#
#         random_question = question_data[question_index]['text']
#         random_question_answer = question_data[question_index]['answer']
#         new_question = Question(random_question, random_question_answer)
#
#         user_answer = input(new_question.text)
#
#         if user_answer == new_question.answer:
#             questions_asked += 1
#             score += 1
#             print(f"That is correct. your score: {score}/{questions_asked}")
#         else:
#             questions_asked += 1
#             print(f"That is incorrect. your score: {score}/{questions_asked}")
#
# print(f"Thanks for playing, your final score is {score}/{questions_asked}")

#################################################################################################