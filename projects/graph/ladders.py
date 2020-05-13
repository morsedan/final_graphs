import string

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)

                q.enqueue(path_copy)

with open('words.txt') as f:
    words = f.read().split()

word_set = set()

for w in words:
    word_set.add(w.lower())

letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []

    string_word = list(word)

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter

            w = "".join(temp_word)

            if w != word_set and w in word_set:
                neighbors.append(w)
    return neighbors
