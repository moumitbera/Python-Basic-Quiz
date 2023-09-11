class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_score = 0
        self.incorrect_score = 0

    def next_question(self):
        question_obj = self.question_list[self.question_number]
        self.question_text = question_obj.text
        self.question_answer = question_obj.answer
        self.question_number += 1

        self.userAnswer = input(f"Q.{self.question_number}: {self.question_text} (True/False): ").lower()
        self.check_answer()
        

    def check_answer(self):
        if self.userAnswer == "t" or self.userAnswer == "true":
            self.userAnswer = "True"
        
        if self.userAnswer == "f" or self.userAnswer == "false":
            self.userAnswer = "False"

        if self.userAnswer == self.question_answer:
            self.correct_score += 1
            print("That is correct!")
        else:
            self.incorrect_score += 1
            print("Sorry, that's incorrect!")
        print(f"The correct answer was: {self.question_answer}")
        
        print(f"Your current score is - correct: {self.correct_score} incorrect: {self.incorrect_score} out of total: {self.question_number}\n")

    def has_more_questions(self):
        return (self.question_number+1) <= len(self.question_list)