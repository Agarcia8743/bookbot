from collections import Counter

def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def track_character_counts(text: str) -> dict:
    tracker = Counter()
    for char in text.lower():
        if char.isalpha():
            tracker[char] += 1

    return dict(sorted(tracker.items(), reverse=True, key=lambda item: item[1]))