def file_write_append_read(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("This is the first line.\n")
        f.write("This is the second line.\n")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("Appending a third line.\n")
        f.write("And a fourth line.\n")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Contents of '{filename}':\n")
    print(content)
if __name__ == "__main__":
    file_write_append_read("example.txt")
