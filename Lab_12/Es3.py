
class Image:

    def __init__(self, img: list) -> None:
        self._img = img

    def get_img(self):
        return self._img

    def __repr__(self) -> str:
        string = ""
        for i in range(len(self._img)):
            for j in range(len(self._img[i])):
                string += str(self._img[i][j]) + "  "
            string += "\n"
        return string


def stampa(l):
    string = ""
    for i in range(len(l)):
        for j in range(len(l[i])):
            string += str(l[i][j]) + "  "
        string += "\n"
    print(string)


def paint_bucket(img, color, pos, all_near):
    x, y = pos[0], pos[1]
    old_color = img[x][y]
    near = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if img[x+i][y+j] == old_color and (x+i, y+j) != (x, y) and (x+i, y+j) not in all_near:  # Se è del vecchio colore e non è il punto su cui è stato eseguito
                    all_near.append((x+i, y+j))
                    near.append((x+i, y+j))
            except IndexError:
                pass
    print(near)
    print(all_near)
    print()

    if len(near) != 0:
        img[x][y] = color
        # paint_bucket(img, color, near[0], all_near)
        # try:
        #     paint_bucket(img, color, near[1], all_near)
        # except IndexError:
        #     pass
        for pos in all_near:
            paint_bucket(img, color, pos, all_near)
            # stampa(img)


list = [[0, 5, 1, 2, 3, 2], [2, 1, 6, 2, 2, 2], [4, 8, 2, 9, 5, 2], [2, 2, 8, 2, 1, 2], [3, 7, 9, 2, 2, 2], [6, 5, 9, 8, 2, 4]]
color = 5
position = (4, 5)


stampa(list)

paint_bucket(list, color, position, [])

stampa(list)


# image = Image(l)
#
# print(image)


