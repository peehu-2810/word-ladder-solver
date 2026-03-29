from solver import bfs_word_ladder

def load_words():
    with open("words.txt", "r") as file:
        return [word.strip().lower() for word in file]


print("=== Word Ladder Solver ===")

start = input("Enter start word: ").lower()
end = input("Enter end word: ").lower()

word_list = load_words()

if len(start) != len(end):
    print("Words must be of same length")
else:
    result = bfs_word_ladder(start, end, word_list)

    if result:
        print("\nTransformation Path:")
        for word in result:
            print(word)
        print("\nTotal Steps:", len(result) - 1)
    else:
        print("No transformation found")