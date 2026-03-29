from collections import deque

def generate_neighbors(word, word_set):
    neighbors = []
    for i in range(len(word)):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            new_word = word[:i] + ch + word[i+1:]
            if new_word in word_set and new_word != word:
                neighbors.append(new_word)
    return neighbors


def bfs_word_ladder(start_word, end_word, word_list):
    word_set = set(word_list)
    queue = deque([(start_word, [start_word])])
    visited = set([start_word])

    while queue:
        current_word, path = queue.popleft()

        if current_word == end_word:
            return path

        for neighbor in generate_neighbors(current_word, word_set):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None
