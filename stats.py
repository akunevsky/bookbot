def word_counter(book_text):
    word_count = len(book_text.split())    
    print(f"{word_count} words found in the document")

def letter_counter(book_text):
    from collections import Counter
    lower_case = book_text.lower()
    letters = list(lower_case)   
    letter_count = Counter(letters)
    print(letter_count)