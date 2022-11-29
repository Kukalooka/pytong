class Password:
    def __init__(self, word):
        self.word = word

    def hash(self):
        wors = list(self.word)
        spol = ["b", "d", "g", "w", "z", "ź", "ż", "l", "ł", "r", "m", "n", "j", "p", "t",
                "k", "f", "s", "ś", "c", "ć"]

        remember = ""
        firstIndex = 0

        for index, x in enumerate(wors):
            for y in spol:
                if x == y:
                    wors[index] = remember
                    if remember == "":
                        firstIndex = index
                    remember = y
        wors[firstIndex] = remember
        return ''.join(wors)
    @staticmethod
    def unhash(word):
        wors = list(word)
        spol = ["b", "d", "g", "w", "z", "ź", "ż", "l", "ł", "r", "m", "n", "j", "p", "t",
                "k", "f", "s", "ś", "c", "ć"]

        remember = ""
        firstIndex = 0

        for index, x in reversed(list(enumerate(wors))):
            for y in spol:
                if x == y:
                    wors[index] = remember
                    if remember == "":
                        firstIndex = index
                    remember = y
        wors[firstIndex] = remember
        return ''.join(wors)


funny = Password("amfetamina")
print(funny.hash())
print(Password.unhash("anmefatima"))