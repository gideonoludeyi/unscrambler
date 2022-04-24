import nltk  # type: ignore
from nltk.downloader import download  # type: ignore

download('words', download_dir='./.nltk_data')

while True:
    letters = input("List of words :\t").lower()

    puzzle_letters = nltk.FreqDist(letters)
    obligatory = list(letters)
    wordlist = nltk.corpus.words.words()

    results = set([w for w in wordlist if 2 < len(w) <= len(letters)
                   and nltk.FreqDist(w) <= puzzle_letters
                   for o in obligatory
                   if o in w])

    print(sorted(results))

    q = input('Press q to quit or enter to continue: ')
    if q == 'q':
        break
