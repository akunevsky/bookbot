from stats import word_counter, letter_counter, sorted_dict, print_formatted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    return(book_text)


book_text = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
word_counter(book_text)
print("--------- Character Count -------")
character_count = letter_counter(book_text)
sorted_list = sorted_dict(character_count)
print_formatted_list(sorted_list)
print("============= END ===============")