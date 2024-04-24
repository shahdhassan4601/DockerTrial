import nltk
from nltk.corpus import stopwords
import pandas as pd
import string

# Download stopwords (one-time download)
nltk.download('stopwords')
nltk.download('punkt')

# Define stop words (can be expanded as needed)
stop_words = stopwords.words('english')

# Open the file
with open("random_paragraphs.txt", "r") as f:
  text = f.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Define additional stopwords to filter out specific tokens
additional_stopwords = ["'s", "''", "``","'n"]

# Remove punctuation, single-character tokens, tokens containing digits, and specific tokens
words = [word.lower() for word in words if word not in string.punctuation 
                                         and len(word) > 1 
                                         and not word.isdigit() 
                                         and word not in additional_stopwords]

# Remove stop words from the text
words = [word for word in words if word not in stop_words]

# Count the frequency of each word
word_counts = pd.Series(words).value_counts()


# Export word frequency counts to a text file (change 'word_frequency.txt' to the path of your filename)
with open('word_frequency.txt', 'w') as f:
  for word, count in word_counts.items():
    f.write(f"{word}: {count}\n")  # Write each word and count with newline

print("Word frequency counts exported to word_frequency.txt")

# Check if any stop words are present in the text
has_stop_words = False
for word in words:
  if word in stop_words:
    has_stop_words = True
    print(word)  # Exit the loop once a stop word is found (optional)

if has_stop_words:
  print("There are stop words in the text.")
else:
  print("There are no stop words in the text.")
