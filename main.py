def main():
    filepath = "books/frankenstein.txt"
    from stats import get_num_words
    from stats import count_characters
    word_count = get_num_words(filepath)
    letter_count = count_characters(filepath)
    print(word_count)
    print(letter_count)
main()