def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    words = text.split()
    print(f"Total words in '{filename}': {len(words)}")
if __name__ == "__main__":
    count_words_in_file("data.txt")
