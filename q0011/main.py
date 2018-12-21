if __name__ == '__main__':
    with open('filtered_words.txt', encoding='utf-8') as f:
        s = f.read()
    words = s.split('\n')
    message = "What do you want to say?\n> "
    word = input(message)
    while word not in ("quit", "q", "Q", "QUIT"):
        if word in words:
            print("Freedom")
        else:
            print("Human Rights")
        word = input(message)
