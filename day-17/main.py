from data import question_data
from question_model import Question

questionBank = []
for question in question_data:
  newQuestion = (Question(question['text'], question['answer']))
  questionBank.append(newQuestion)
print(questionBank)
