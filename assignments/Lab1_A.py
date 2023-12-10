# Amirhossein Ghaffari - Lab1

import nltk
from nltk.corpus import brown, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

output_file_path = "word_frequency.txt"
nltk.download('brown')
nltk.download('punkt')
words = brown.words()

##### part 1
freq_dist = FreqDist(words)
for w, f in freq_dist.items():
    print(f"{w}: {f}")
with open(output_file_path, "w") as file:
    for w, f in freq_dist.items():
        file.write(f"{w}: {f}\n")

##### part 2
most_common_words = freq_dist.most_common(30)

words, frequencies = zip(*most_common_words)

plt.figure(figsize=(12, 6))
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 30 Most Frequent Words')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

##### part 3
least_frequent_words = freq_dist.most_common()[-30:]

# middle range words selected based on middle of frequency dist-15 and +15
middle_range_words = freq_dist.most_common()[int(len(freq_dist)/2)-15:int(len(freq_dist)/2)+15]
least_frequent_words, least_frequent_frequencies = zip(*least_frequent_words)
middle_frequent_words, middle_frequent_frequencies = zip(*middle_range_words)

plt.figure(figsize=(12, 6))
plt.bar(least_frequent_words, least_frequent_frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Thirty Least Frequent Words')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(middle_frequent_words, middle_frequent_frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Thirty Middle Range Words')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


##### part 4
word_lengths = list(map(len, freq_dist))

word_length_freq = {}

for length in word_lengths:
    if length in word_length_freq:
        word_length_freq[length] += 1  # Increment frequency count
    else:
        word_length_freq[length] = 1   # Initialize frequency count


lengths = list(word_length_freq.keys())
frequencies = list(word_length_freq.values())

plt.figure(figsize=(10, 6))
plt.scatter(lengths, frequencies, alpha=0.5)
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.title('Word Length vs. Frequency in Brown Corpus')
plt.grid(True)
plt.show()


#### part 5
option_list = ['will', 'must', 'might', 'may', 'could', 'can']
option_dict = {}
for option in option_list:
    option_dict[option] = freq_dist[option]

lengths = list(option_dict.keys())
frequencies = list(option_dict.values())

plt.figure(figsize=(8, 6))
plt.scatter(lengths, frequencies, alpha=0.5)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word list vs. Frequency in Brown Corpus')
plt.grid(True)
plt.show()

def calculate_sentence_length(sentence):
    words = nltk.word_tokenize(sentence)
    num_words = len(words)
    num_characters = len(sentence)
    return num_words, num_characters

def process_sentences_with_modals(modal_words):
    sentences_with_modals = []
    for file_id in brown.fileids():
        for sentence in brown.sents(file_id):
            sentence_text = ' '.join(sentence)
            if any(modal in sentence_text.lower() for modal in modal_words):
                sentences_with_modals.append(sentence_text)
    return sentences_with_modals

sentences_with_modals = process_sentences_with_modals(option_list)

for sentence in sentences_with_modals:
    num_words, num_characters = calculate_sentence_length(sentence)
    print(f"Sentence with modals: {sentence}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")

total_sentences = len(sentences_with_modals)
print(f"Total sentences with modal words: {total_sentences}")

##### part 6

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

stopword_count = []
sentence_length_words = []
sentence_length_chars = []

for file_id in brown.fileids():
    for sentence in brown.sents(file_id):
        sentence_text = ' '.join(sentence)
        num_words, num_characters = calculate_sentence_length(sentence_text)
        sentence_length_words.append(num_words)
        sentence_length_chars.append(num_characters)

        stop_word_count = sum(1 for word in nltk.word_tokenize(sentence_text) if word.lower() in stop_words)
        stopword_count.append(stop_word_count)


plt.figure(figsize=(10, 6))
plt.scatter(sentence_length_words, stopword_count, alpha=0.5)
plt.xlabel('Sentence Length (in words)')
plt.ylabel('Number of Stopwords')
plt.title('Number of Stopwords vs. Sentence Length (in words)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(sentence_length_chars, stopword_count, alpha=0.5)
plt.xlabel('Sentence Length (in characters)')
plt.ylabel('Number of Stopwords')
plt.title('Number of Stopwords vs. Sentence Length (in characters)')
plt.grid(True)
plt.show()
