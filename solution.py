import re

def read_file(file_name):
    # Open the input file
    with open(file_name, 'r') as f:
        # Read the contents of the file
        contents = clean_text(f.readlines())
    return contents


def clean_text(text: list[str]) -> list[str]:
    return [line.rstrip('\n') for line in text]


def split_into_words(contents):
    words = []
    for line in contents:
        line_words = re.split(r'[-+#, .!?():;/]+', line)
        if '' in line_words:
            line_words.remove('')
        for word in line_words:
            words.append(word)
    return words


def find_top_10_words(words):
    word_count = {}
    # count the occurrences of each word in the list
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # sort the words by their count in descending order
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return top_words


def write_file(output, top_words):
    with open(output, "w") as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")

if __name__ == "__main__":
    contents = read_file("input.txt")
    words = split_into_words(contents)
    top_words = find_top_10_words(words)
    write_file("output.txt", top_words)