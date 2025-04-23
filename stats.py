filepath = "books/frankenstein.txt"

#define a function to take a txt file and return as a string
def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

book = get_book_text(filepath)
lower_book = book.lower()

#define function as a .split function and counts number of indices
def get_num_words(filepath):
    book = get_book_text(filepath)
    num_words = 0
    word_list = book.split()
    for i in range(0, len(word_list)):
        num_words += 1
    return f"{num_words} words found in the document"

#take portion of previous function to split text and then loop to a dict for counting
def count_characters(filepath):
    book = get_book_text(filepath)
    lower_book = book.lower()
    count = {}
    for char in lower_book:
            in_count = char in count
            if in_count == False:
                 count[char] = 1
            else:
                 count[char] += 1
    return count             
     
