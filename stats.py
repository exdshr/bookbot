def get_word_count(text):
    count = len(text.split())
    return f"Found {count} total words"

def get_char_count(text):
    dict = {}
    for c in text:
        lc = c.lower()
        if lc in dict:
            dict[lc] += 1
        else:
            dict[lc] = 1
    return dict

def sort_on(item):
    return item["num"]

def sort_char_count(char_dict):
    list = []
    for i in char_dict:
        list.append({ "char": i, "num": char_dict[i] })
    list.sort(reverse=True, key=sort_on)
    return list

