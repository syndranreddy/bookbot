import sys
from stats import *

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path) as f:
        book_text = f.read()
    
    #Count words
    word_count = count_words(book_text)
    
    #Count letters
    letter_counts = count_letters(book_text)
    sorted_chars = sort_letters(letter_counts)
    
    # Print the formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Only print alphabetical characters
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()

