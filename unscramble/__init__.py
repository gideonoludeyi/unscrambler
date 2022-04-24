import nltk  # type: ignore
from nltk.downloader import download  # type: ignore

download('words', download_dir='./.nltk_data')
nltk.data.path.append('./.nltk_data')

wordlist = nltk.corpus.words.words()


def unscramble(chars: str) -> list[str]:
    chars = chars.replace(' ', '').lower()

    puzzle_letters = nltk.FreqDist(chars)
    required_letters = list(chars)

    results = set()
    for word in wordlist:
        if 2 < len(word) <= len(chars) and nltk.FreqDist(word) <= puzzle_letters:
            for letter in required_letters:
                if letter in word:
                    results.add(word)

    return sorted(results, key=len, reverse=True)
