def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)
