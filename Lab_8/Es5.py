from Es2 import File, TextFile, BipMap


class Directory(File):

    def __init__(self, name: str) -> None:
        self._name = name
        self._content = []

    def add_file(self, file: File) -> None:
        self._content.append(file)

    def open_files(self) -> None:
        for file in self._content:
            print(file.__repr__())

    def get_info(self) -> tuple:
        string = ""
        string += self._name + ":"
        for file in self._content:
            l = file.get_info()[1]
            if len(l) > 1:
                i = 0
                while i < len(l):
                    string += "\n" + " " * 4 + l[i]
                    i += 1
            else:
                string += "\n" + " " * 4 + file.get_info()
        lista = string.split("\n")
        return string, lista

    def get_dim(self) -> int:
        return len(self._content)

    def __repr__(self) -> str:
        return self.get_info()[0]


def main():
    file = File("empty.info")

    text = TextFile("text.txt")
    text.add_line("Riga 1 del file di testo")
    text.add_line("seconda riga del file")
    text2 = TextFile("another_text.txt")
    text2.add_line("Questo è un altro testo")

    img = [[150, 0, 232], [255, 15, 26], [45, 124, 62], [12, 26, 145]]
    img2 = [[120, 50, 22], [25, 154, 206], [45, 14, 162], [140, 0, 212], [125, 6, 58]]
    bipmap = BipMap("image.bmp", img)
    bipmap2 = BipMap("second_image.img", img2)
    bipmap3 = BipMap("photo.bmp", img)
    bipmap4 = BipMap("photo2.img", img2)

    folder1 = Directory("Cartella")
    folder1.add_file(file)
    folder1.add_file(text)
    folder1.add_file(text2)

    folder2 = Directory("Immagini")
    folder2.add_file(bipmap)
    folder2.add_file(bipmap2)

    folder3 = Directory("Testi")
    folder3.add_file(TextFile("notes.txt"))
    folder3.add_file(TextFile("exercises.txt"))

    folder4 = Directory("Foto")
    folder4.add_file(bipmap3)
    folder4.add_file(bipmap4)

    folder1.add_file(folder2)
    folder1.add_file(folder3)
    folder2.add_file(folder4)

    # folder1.open_files()

    print()

    print(folder1)


main()