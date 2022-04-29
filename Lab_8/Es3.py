from Es2 import File, TextFile, BipMap

class Directory:

    def __init__(self, name: str) -> None:
        self._name = name
        self._content = []

    def add_file(self, file: File) -> None:
        self._content.append(file)

    def open_files(self) -> None:
        for file in self._content:
            print(file.__repr__())

    def __repr__(self) -> None:
        print(self._name)
        for file in self._content:
            print(" "*4 + file.get_info())


def main():
    file = File("empty.info")
    text = TextFile("text.txt")
    img = [[150, 0, 232], [255, 15, 26], [45, 124, 62]]
    bipmap = BipMap("image.bmp", img)

    folder = Directory("Folder")
    folder.add_file(file)
    folder.add_file(text)
    folder.add_file(bipmap)

    # folder.open_files()  TODO: da sistemare il metodo

    folder.__repr__()


main()