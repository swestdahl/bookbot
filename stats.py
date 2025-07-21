def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = str(text).lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char(text):
    char_counts = count_characters(text)
    sorted_chars = sorted(
        [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()],
        key=lambda item: item["num"],
        reverse=True)
    return sorted_chars

    


