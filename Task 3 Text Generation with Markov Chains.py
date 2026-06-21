import random

text = """
Python is one of the most popular programming languages in the world.
It is widely used in Artificial Intelligence, Machine Learning, and Web Development.
Python is easy to learn because of its simple syntax and readability.
Many developers use Python for automation, data science, and software development.
Artificial Intelligence systems often use Python libraries for deep learning applications.
Python helps programmers build efficient and scalable software solutions.
Technology companies use Artificial Intelligence to improve modern applications.
Machine Learning models analyze data and generate intelligent predictions.
"""

# Convert text into words
words = text.split()

# Create Markov chain dictionary
markov_chain = {}

for i in range(len(words) - 1):

    current_word = words[i]

    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

# Select random starting word
current_word = random.choice(words)

generated_text = current_word

# Generate text
for i in range(30):

    if current_word in markov_chain:

        next_word = random.choice(markov_chain[current_word])

        generated_text += " " + next_word

        current_word = next_word

# Display generated text
print("\n===== GENERATED TEXT =====\n")

print(generated_text)


