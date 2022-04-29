from Es2 import File, TextFile, BipMap


class Directory:

    def __init__(self, name: str) -> None:
        self._name = name
        self._content = []

    def get_name(self) -> str:
        return self._name

    def add_file(self, file: File) -> None:
        self._content.append(file)

    def open_files(self) -> None:
        for file in self._content:
            print(file.__repr__())

    def __repr__(self) -> None:
        string = ""
        string += self._name + ":"
        for file in self._content:
            string += "\n" + " " * 4 + file.get_info()
        return string


def main():
    file = File("empty.info")
    text = TextFile("text.txt")
    text.add_line("Riga 1 del file di testo")
    text.add_line("seconda riga del file")
    img = [[150, 0, 232], [255, 15, 26], [45, 124, 62], [12, 26, 145]]
    bipmap = BipMap("image.bmp", img)

    folder = Directory("Folder")
    folder.add_file(file)
    folder.add_file(text)
    folder.add_file(bipmap)

    folder.open_files()

    print()

    print(folder.get_name())

    print()

    print(folder)


main()
