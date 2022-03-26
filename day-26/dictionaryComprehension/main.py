names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
student_scores = {name:random.randint(0, 100) for name in names}
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}

# day-26-4-exercise
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Write your code 👇 below:

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
wordLength = {word: len(word) for word in sentence.split()}
print(wordLength)

# day-26-5-exercise
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f:
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Write your code 👇 below:

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5 +32) for (day, temp) in weather_c.items()}
print(weather_f)