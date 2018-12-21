if __name__ == '__main__':
    with open('filtered_words.txt', encoding='utf-8') as f:
        s = f.read()
    words = s.split('\n')
    message = "What do you want to say?\n> "
    sentence = input(message)
    while sentence not in ("quit", "q", "Q", "QUIT"):
        for w in words:
            sentence = sentence.replace(w, len(w)*"*")
        print(sentence)
        sentence = input(message)
