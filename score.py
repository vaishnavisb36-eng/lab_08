
import sys

n = int(sys.argv[1])

scores = []

# Accept scores
for i in range(n):
    score = float(sys.argv[i + 2])
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

# Find maximum and minimum
maximum = scores[0]
minimum = scores[0]

for score in scores:
    if score > maximum:
        maximum = score

    if score < minimum:
        minimum = score

print("Maximum Score:", maximum)
print("Minimum Score:", minimum)
