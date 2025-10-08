# Task 2: Count word occurrences

def word_count(text):
    words = text.split()  # split string by spaces
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1  # increment count
    return count


log = "test pass fail pass test fail fail"
print(word_count(log))

# .split() breaks text into words.
# count.get(w, 0) + 1 → adds 1 to the count of each word.
