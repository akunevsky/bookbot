import sys
from stats import word_counter, letter_counter, sorted_dict, print_formatted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    try: 
        with open(filepath) as f:
            file_contents = f.read()
        return(file_contents)
    except FileNotFoundError:
        print(f"'{filepath}' is an invalid filepath. Try books/warandpeace.txt")
        sys.exit(2)

def main():
    book_text = get_book_text(filepath)
    return(book_text)


book_text = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
word_counter(book_text)
print("--------- Character Count -------")
character_count = letter_counter(book_text)
sorted_list = sorted_dict(character_count)
print_formatted_list(sorted_list)
print("============= END ===============")