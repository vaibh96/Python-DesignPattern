import re
from collections import Counter


def wordCounter(path):

    print("In wordCounter")
    lines = []
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-z]+", file.read())
        all_words = [word.upper() for word in all_words]

    word_count = Counter()
    for word in all_words:
        word_count[word] += 1

    for word in word_count.most_common(20):
        print(word[0], '\t', word[1])




