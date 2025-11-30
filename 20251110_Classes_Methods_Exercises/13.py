
class Note:
    def __init__(self, filename):
        self.filename = filename

    def write_note(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
        print("Note added")

    def read_note(self):
        with open(self.filename, "r") as file:
            contents = file.read()
        print("File content :\n" + contents)

n = Note("note.txt")
n.write_note("Texts")
n.read_note()
