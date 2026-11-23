n = int(input("Enter number of scores: "))

scores = []

# Accept scores
for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

# Calculate sum
total = 0

for score in scores:
    total = total + score

# Calculate average
average = total / n

# Display results
print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
