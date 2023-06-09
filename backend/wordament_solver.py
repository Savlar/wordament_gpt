import os


def find_words(matrix, length):
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, 'static/dictionary.txt')
    with open(data_file, "r") as f:
        dictionary = dict.fromkeys(f, None)

    """Finds all valid words of a given length in a 4x4 matrix of letters."""
    words = list()
    def dfs(word, visited, i, j):
        """Performs a depth-first search to find words starting from a given position."""
        # Add current letter to the word and mark position as visited
        word += matrix[i][j]
        visited.add((i, j))

        # If the word is of the desired length, add it to the set of valid words
        if len(word) == length and word in dictionary:
            words.append(word)

        # Search all adjacent positions that have not been visited yet
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                new_i = i + di
                new_j = j + dj

                # Check if new position is within bounds and has not been visited yet
                if 0 <= new_i < 4 and 0 <= new_j < 4 and (new_i, new_j) not in visited:
                    dfs(word, visited, new_i, new_j)

    # Call dfs() for each position in the matrix
    for i in range(4):
        for j in range(4):
            dfs('', set(), i, j)

    return words
