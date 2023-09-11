from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from prettytable import PrettyTable

scoreBoard = PrettyTable()

question_bank = []
for i in question_data:
    i = Question(text=i["question"], answer=i["correct_answer"])
    question_bank.append(i)

quiz = QuizBrain(question_bank)
while quiz.has_more_questions():
    quiz.next_question()

print("You have completed the quiz! Your final score was -- \n")
scoreBoard.add_row(["Correct:", quiz.correct_score])
scoreBoard.add_row(["Incorrect:", quiz.incorrect_score])
scoreBoard.add_row(["Total Questions:", quiz.question_number])
print(scoreBoard)
#print(f"correct {quiz.correct_score} incorrect {quiz.incorrect_score} out of {quiz.question_number}")