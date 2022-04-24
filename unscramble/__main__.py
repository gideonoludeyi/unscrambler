import nltk  # type: ignore
from nltk.downloader import download  # type: ignore

NLTK_DATA = './.nltk_data'

download('words', download_dir=NLTK_DATA)
nltk.data.path.append(NLTK_DATA)  # tell nltk to search for nltk dataset here

while True:
    letters = list(input("List of characters :\t").replace(' ', '').lower())

    puzzle_letters = nltk.FreqDist(letters)
    wordlist = nltk.corpus.words.words()

    results = set()
    for word in wordlist:
        within_length_range = 2 < len(word) <= len(letters)
        if within_length_range and nltk.FreqDist(word) <= puzzle_letters:
            for letter in letters:
                if letter in word:
                    results.add(word)

    print(sorted(results))

    q = input('Press q to quit or enter to continue: ')
    if q == 'q':
        break
