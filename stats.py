def word_counter(book_text):
    word_count = len(book_text.split())    
    print(f"Found {word_count} total words")

def letter_counter(book_text):
    from collections import Counter
    lower_case = book_text.lower()
    letters = list(lower_case)   
    letter_count = Counter(letters)
    return(letter_count)

def sort_on(items):
    return items["num"]

def sorted_dict(character_count):
    char_dict = []
    for character, count in character_count.items():
        if character.isalpha():
            char_dict.append({"char": character, "num": count})
    char_dict.sort(reverse=True, key=sort_on)
    return(char_dict) 

def print_formatted_list(char_dict):
    for line in char_dict:
        print(f"{line['char']}: {line['num']}")