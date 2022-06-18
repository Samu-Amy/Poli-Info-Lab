from elements import Desktop, Folder, File


class Model:

    def __init__(self):
        self._desktop = Desktop()

        # Prova
        self._desktop.add(Folder("Files").add(File("Text"))).add(File("Text"))
        folder = Folder("Images").add(File("Image 1")).add(File("Image 2"))
        self._desktop.add(folder)

    def get_desktop(self):
        return self._desktop
