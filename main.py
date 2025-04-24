def main():
    import sys
    filepath = ""
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    from stats import get_book_text
    from stats import get_num_words
    from stats import count_characters
    from stats import sort_on
    from stats import sort_report

    sorted = sort_report(filepath)
    word_count = get_num_words(filepath)
    letter_count = count_characters(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {filepath}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for i in range(0, len(sorted)):
        dict_list = sorted[i]
        letter = dict_list["char"]
        number = dict_list["num"]
        print(f"{letter}: {number}")
        
    print("============== END ==============")
main()