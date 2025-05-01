def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_dict(og_dict):
    new_list = []
    for c in og_dict:
        new_list.append({"char": c, "num": og_dict[c]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

