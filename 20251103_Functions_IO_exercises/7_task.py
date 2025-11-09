def count_words(filename):
    return len([i for i in filename.open().split()])