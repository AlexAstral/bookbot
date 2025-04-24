

#define a function to take a txt file and return as a string
def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#define function as a .split function and counts number of indices
def get_num_words(filepath):
    book = get_book_text(filepath)
    num_words = 0
    word_list = book.split()
    for i in range(0, len(word_list)):
        num_words += 1
    return f"Found {num_words} total words"

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

def sort_on(dict):
    return dict["num"]

def sort_report(filepath):
    count = count_characters(filepath)
    new_count = []
     
    for char in count:
        num = count[char]
        new_dict = {}
        symbols = []
        if char.isalpha():
            new_dict["char"] = char
            new_dict["num"] = num
            new_count.append(new_dict)
        else:
            symbols.append(char)
    new_count.sort(reverse=True, key=sort_on)
    return new_count

    
