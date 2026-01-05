import sys

from stats import count_words, track_character_counts

def main():
    check_args()
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_counts = track_character_counts(book_text)
    print_report(path, word_count, char_counts)

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def print_report(path: str, word_count: int, char_counts: dict):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

if __name__ == "__main__":
    main()

