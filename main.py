from stats import word_counter, letter_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    return(book_text)


book_text = main()
word_counter(book_text)
letter_counter(book_text)