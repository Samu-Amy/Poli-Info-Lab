
class Image:

    def __init__(self, image):
        self._image = image

    def paint_bucket(self, color, pos, initial=None):
        i = pos[0]
        j = pos[1]
        initial_color = self._image[i][j]
        self._image[i][j] = color
        for i in range(max(0, pos[0] - 1), min(pos[0] + 1, len(self._image))):
            for j in range(max(0, pos[1] - 1), min(pos[1] + 1, len(self._image[i]))):
                if self._image[i][j] == initial_color:
                    pos = i, j
                    self.paint_bucket(color, pos, initial_color)

    def __repr__(self):
        string = ""
        for i in range(len(self._image)):
            for j in range(len(self._image[i])):
                string += str(self._image[i][j]) + "  "
            string += "\n"
        return string


img = [[0, 5, 1, 2, 3, 2], [2, 1, 6, 2, 2, 2], [4, 8, 2, 9, 5, 2], [2, 2, 8, 2, 1, 2], [3, 7, 9, 2, 2, 2], [6, 5, 9, 8, 2, 4]]
image = Image(img)
col = 0
position = (4, 5)


print(image)
image.paint_bucket(col, position)
print(image)
