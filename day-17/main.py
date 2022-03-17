from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
  newQuestion = (Question(question['text'], question['answer']))
  questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)
quiz.next_question()

while(quiz.more_questions()):
  quiz.next_question()

print(f"You have completed the quiz game. Your final score was {quiz.score}/{quiz.question_number}")
