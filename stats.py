# Counts words from file, returns count
def count_words(file_contents):
    word_count = len(file_contents.split())
    return word_count

# Counts letters from file, returns count
def count_letters(file_contents):
    letter_count = {}
    for i in file_contents:
        i = i.lower()
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    return letter_count

# Sorts letters from letter_count into new dictionary
def sort_letters(letters_dict):
    chars_list = []

    for char, count in letters_dict.items():
        char_dict = {"character" : char, "count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
