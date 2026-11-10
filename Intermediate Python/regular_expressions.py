import re

message = "Python is easy to learn. Python is powerful."

matches = re.findall(r'Python', message)
updated_text = re.sub(r'Python', 'Java', message)
words = re.findall(r'\b\w+\b', message)

print("Original Message:", message)
print("Number of Matches:", len(matches))
print("Modified Message:", updated_text)
print("Words:", words)
