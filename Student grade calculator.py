name = input("Enter the student's name: ")
scores = input("Enter the scores in multiple subjects, separated by spaces: ")
scores = list(map(float, scores.split()))
average_score = sum(scores) / len(scores)

if 90 <= average_score <= 100:
    grade = 'A'
elif 80 <= average_score < 90:
    grade = 'B'
elif 70 <= average_score < 80:
    grade = 'C'
elif 60 <= average_score < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"Student: {name}")
print(f"Average Score: {average_score:.2f}")
print(f"Grade: {grade}")
