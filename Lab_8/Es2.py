class File:

    def __init__(self, title: str) -> None:
        self._title = title
        self._dim = 0
        self._content = ""

    def get_name(self) -> str:
        return self._title

    def get_dim(self) -> int:
        return 0

    def get_info(self) -> str:
        return f"{self.get_name()}: {self.get_dim()}"

    def __repr__(self) -> str:
        return ""


class TextFile(File):

    def __init__(self, title: str) -> None:
        super().__init__(title)

    def add_line(self, line: str) -> None:
        self._content += line + "\n"

    def get_dim(self) -> int:
        lenght = self._content.split("\n")
        return len(lenght) - 1

    def __repr__(self) -> str:
        return self._content

class BipMap(File):

    def __init__(self, title: str, tab: list[list[int]]) -> None:
        super().__init__(title)
        self._image = tab

    def get_dim(self) -> tuple[int]:
        width = len(self._image[0])
        height = len(self._image)
        return (width, height)

    def __repr__(self) -> hex:
        string = ""
        for i in range(len(self._image)):
            for j in range(len(self._image[i])):
                string += hex(self._image[i][j]) + " "
        return string


def main():

    file = File("empty.info")

    print(file.get_name())
    print(file.get_dim())
    print(file.get_info())

    text = TextFile("text.txt")
    text.add_line("Riga 1 del file di testo")
    text.add_line("seconda riga del file")
    text.add_line("ultima riga.")

    print("\n" + text.get_name())
    print(text.get_dim())
    print(text.get_info())
    print("\n" + text.__repr__())

    img = [[150, 0, 232], [255, 15, 26], [45, 124, 62]]
    bipmap = BipMap("image.bmp", img)

    print("\n" + bipmap.get_name())
    print(bipmap.get_dim())
    print(bipmap.get_info())
    print("\n" + bipmap.__repr__())


main()