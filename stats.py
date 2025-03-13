def word_count(text):
    word_list = text.split()
    number_of_words = 0
    for word in word_list:
        number_of_words += 1

    return number_of_words

def char_count(text):
    text = text.lower()
    char_map = {}
    for char in text:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return char_map

def sort_dictionaries(char_count_dict):
    list_of_chars = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_info = {"char": char, "count": count}
            list_of_chars.append(char_info)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars

def sort_on(dict_pair):
    return dict_pair['count']

