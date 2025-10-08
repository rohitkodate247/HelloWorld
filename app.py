# dictionaries (hash maps)

def word_count(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


print(word_count("MANNARINO MONTREAL MANNARINO"))
