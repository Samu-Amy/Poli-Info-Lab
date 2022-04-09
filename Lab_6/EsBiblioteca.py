from tkinter import *
from tkinter import ttk
from random import randint


# ----------------------------------- Classi ----------------------------------- #

class Biblioteca:

    idCodes = []

    def __init__(self):
        self.error = False
        self.duplicate = False
        self.busy = False
        self.newBook = ""
        self.message = ""
        self.users = []
        self.books = []

    def add_user(self, name, idCode):
        self.users.append(Utente(name, idCode))

        # TODO: elimina
        print("\nUtenti:\n")
        print(self.users)
        for book in self.users:
            print(f"{book.name}, {book.idCode}, {book.loans}\n")

    def add_book(self, title, author, shelf, room):
        self.message = ""
        self.error = False
        self.newBook = Libro(title, author, shelf, room)

        # Controllo duplicati
        self.duplicate = False
        for book in self.books:
            if self.newBook.title == book.title and self.newBook.author == book.author:
                self.duplicate = True
                break

        # Controllo posto
        self.busy = False
        for book in self.books:
            if self.newBook.shelf == book.shelf and self.newBook.room == book.room:
                self.busy = True
                break

        if self.duplicate:
            self.error = True
            self.message = "This book already exist"
        elif self.busy:
            self.error = True
            self.message = "This place is already busy"
        else:
            self.error = False
            self.books.append(self.newBook)

        #TODO: elimina
        print("\nLibri:\n")
        for book in self.books:
            print(f"{book.title}, {book.author}, {book.loaned}\n{book.room}, {book.shelf}\n")

        return not self.error, self.message

    def get_book(self, title, author, idCode):
        self.message = ""
        self.error = False

        if len(self.books) > 0:
            if len(self.users) > 0:
                for user in self.users:
                    try:
                        if user.idCode == int(idCode):  # L'utente è registrato

                            for book in self.books:
                                if book.title == title and book.author == author:  # Il libro esiste

                                    if not book.loaned:
                                        if user.loans < Utente.maxLoans:
                                            self.error = False
                                            book.loaned = True
                                            user.loans += 1
                                            self.message = "Book successfully borrowed"  #TODO: aggiungi controllo prestiti utente
                                            break

                                        else:
                                            self.error = True
                                            self.message = "Max loans reached"

                                    else:
                                        self.error = True
                                        self.message = "This book is on loan to someone else"

                                else:  # Il libro non esiste
                                    self.error = True
                                    self.message = "This book does not exist"

                        else:  # L'utente non è registrato
                            self.error = True
                            self.message = "This user is not registered"
                    except ValueError:
                        self.error = True
                        self.message = "User id not valid"
            else:
                self.error = True
                self.message = "There are no registered users"
        else:
            self.error = True
            self.message = "There are no books"

        return self.error, self.message


class Libro:

    def __init__(self, title, author, shelf, room):
        self.title = title
        self.author = author
        self.shelf = shelf
        self.room = room
        self.loaned = False


class Utente:

    maxLoans = 6

    def __init__(self, name, idCode):
        self.name = name
        self.idCode = idCode
        self.loans = 0


library = Biblioteca()

# ----------------------------------- Funzioni ----------------------------------- #

#  - Globali

def resetVar(*var):
    for i in range(len(var)):
        var[i].set("")


def setMessage(section, var, message, color, duration=800):
    section.config(foreground=color)
    var.set(message)
    root.after(duration, lambda: resetVar(var))


#  - Registrazione

def addUser():
    name = registerUserNameVar.get()
    idCode = randint(1000, 10000)

    while idCode in Biblioteca.idCodes:  # Codici non duplicati
        idCode = randint(1000, 10000)

    if registerUserNameVar.get() != "":
        library.add_user(name, idCode)
        setMessage(registerMessage, registerMessageVar, "Successfully registered", "green")
        setMessage(idMessage, idCodeMessageVar, f"Your id is: {idCode}", "blue", 2000)
        resetVar(registerUserNameVar)
    else:
        setMessage(registerMessage, registerMessageVar, "Registration failed", "red")


# - Prestito

def getBook():
    title = borrowTitleVar.get()
    author = borrowAuthorVar.get()
    idCode = borrowUserCodeVar.get()

    result = library.get_book(title, author, idCode)
    if result[0]:
        setMessage(borrowMessage, borrowMessageVar, result[1], "red")
    else:
        setMessage(borrowMessage, borrowMessageVar, result[1], "green")
        resetVar(borrowTitleVar, borrowAuthorVar, borrowUserCodeVar)


#  - Aggiunta libro

def addBook():
    error = False
    title = addBookTitleVar.get()
    author = addBookAuthorVar.get()
    try:
        shelf = int(addBookShelfVar.get())
        room = int(addBookRoomVar.get())
        error = False
    except ValueError:
        error = True
        shelf = ""  # Solo per eliminare l'avviso di pycharm
        room = ""

    if title != "" and author != "":
        if not error:
            result = library.add_book(title, author, shelf, room)
            if result[0]:
                setMessage(addBookMessage, addBookMessageVar, "Book successfully added", "green")
                resetVar(addBookTitleVar, addBookAuthorVar, addBookShelfVar, addBookRoomVar)
            else:
                setMessage(addBookMessage, addBookMessageVar, result[1], "red")
        else:
            setMessage(addBookMessage, addBookMessageVar, "Shelf or room invalid", "red")
    else:
        setMessage(addBookMessage, addBookMessageVar, "Book title or author invalid", "red")


# ----------------------------------- Grafica ----------------------------------- #

root = Tk()
root.title("Dashboard")
root.geometry("+450+300")


# Variabili

# - Sezione back

addBookTitleVar = StringVar()
addBookAuthorVar = StringVar()
addBookShelfVar = StringVar()
addBookRoomVar = StringVar()
addBookMessageVar = StringVar()

findBookTitleVar = StringVar()
findBookAuthorVar = StringVar()
findBookMessageVar = StringVar()

findBookShelfVar = StringVar()
findBookRoomVar = StringVar()
findShelfMessageVar = StringVar()

userCodeVar = StringVar()
loanBookMessageVar = StringVar()


# - Sezione front

registerUserNameVar = StringVar()
registerMessageVar = StringVar()
idCodeMessageVar = StringVar()

borrowTitleVar = StringVar()
borrowAuthorVar = StringVar()
borrowUserCodeVar = StringVar()
borrowMessageVar = StringVar()

returnTitleVar = StringVar()
returnAuthorVar = StringVar()
returnMessageVar = StringVar()


# Gestione biblioteca

frameBack = Frame(root)
frameBack.grid(row=0, column=0, sticky="nw")  # -------------------------------------------


# - Aggiunta libro

addBookSection = Frame(frameBack)
addBookSection.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

addBookTitle = ttk.Label(addBookSection, text="Add book", font=",12", anchor="center")
addBookTitle.grid(row=0, column=0, columnspan=2, pady=(0, 10))

bookTitleLabel = ttk.Label(addBookSection, text="Book title:")
bookTitle = ttk.Entry(addBookSection, textvariable=addBookTitleVar)
bookTitleLabel.grid(row=1, column=0, sticky="w")
bookTitle.grid(row=2, column=0, padx=(0, 20), pady=(0, 20))

bookAuthorLabel = ttk.Label(addBookSection, text="Book author:")
bookAuthor = ttk.Entry(addBookSection, textvariable=addBookAuthorVar)
bookAuthorLabel.grid(row=1, column=1, sticky="w")
bookAuthor.grid(row=2, column=1, pady=(0, 20))

bookShelfLabel = ttk.Label(addBookSection, text="Shelf:")
bookShelf = ttk.Entry(addBookSection, textvariable=addBookShelfVar)
bookShelfLabel.grid(row=3, column=0, sticky="w")
bookShelf.grid(row=4, column=0, padx=(0, 20))

bookRoomLabel = ttk.Label(addBookSection, text="Room:")
bookRoom = ttk.Entry(addBookSection, textvariable=addBookRoomVar)
bookRoomLabel.grid(row=3, column=1, sticky="w")
bookRoom.grid(row=4, column=1)

addBookMessage = ttk.Label(addBookSection, textvariable=addBookMessageVar)
addBookMessage.grid(row=5, column=0, sticky="w", pady=(10, 0))

addBookSubmit = ttk.Button(addBookSection, text="Add", command=addBook)
addBookSubmit.grid(row=5, column=1, sticky="e", pady=(10, 0))


# - Ricerca libro

findBookSection = Frame(frameBack)
findBookSection.grid(row=0, column=2, sticky="nw", padx=(10, 20), pady=(20, 10))

findBookTitle = ttk.Label(findBookSection, text="Find book", font=",12", anchor="center")
findBookTitle.grid(row=0, column=0, columnspan=2, pady=(0, 10))

bookTitleLabel = ttk.Label(findBookSection, text="Book title:")
bookTitle = ttk.Entry(findBookSection, textvariable=findBookTitleVar)
bookTitleLabel.grid(row=1, column=0, sticky="w")
bookTitle.grid(row=2, column=0, padx=(0, 20))

bookAuthorLabel = ttk.Label(findBookSection, text="Book author:")
bookAuthor = ttk.Entry(findBookSection, textvariable=findBookAuthorVar)
bookAuthorLabel.grid(row=1, column=1, sticky="w")
bookAuthor.grid(row=2, column=1)

findBookMessage = ttk.Label(findBookSection, textvariable=findBookMessageVar)
findBookMessage.grid(row=3, column=0, sticky="w", pady=(10, 0))

findBookSubmit = ttk.Button(findBookSection, text="Find", command=addBook)
findBookSubmit.grid(row=3, column=1, sticky="e", pady=(10, 0))


# - Scaffale

shelfBookSection = Frame(frameBack)
shelfBookSection.grid(row=2, column=0, sticky="nw", padx=(20, 10), pady=(10, 20))

shelfBookTitle = ttk.Label(shelfBookSection, text="Find in shelf", font=",12", anchor="center")
shelfBookTitle.grid(row=0, column=0, columnspan=2, pady=(0, 10))

bookShelfLabel = ttk.Label(shelfBookSection, text="Shelf:")
bookShelf = ttk.Entry(shelfBookSection, textvariable=findBookShelfVar)
bookShelfLabel.grid(row=1, column=0, sticky="w")
bookShelf.grid(row=2, column=0, padx=(0, 20))

bookRoomLabel = ttk.Label(shelfBookSection, text="Room:")
bookRoom = ttk.Entry(shelfBookSection, textvariable=findBookRoomVar)
bookRoomLabel.grid(row=1, column=1, sticky="w")
bookRoom.grid(row=2, column=1)

shelfBookMessage = ttk.Label(shelfBookSection, textvariable=findShelfMessageVar)
shelfBookMessage.grid(row=3, column=0, sticky="w", pady=(10, 0))

shelfBookSubmit = ttk.Button(shelfBookSection, text="Find", command=addBook)
shelfBookSubmit.grid(row=3, column=1, sticky="e", pady=(10, 0))


# - Libri in prestito

loansSection = Frame(frameBack)
loansSection.grid(row=2, column=2, sticky="nsew", padx=(10, 20), pady=(10, 20))

loanBookTitle = ttk.Label(loansSection, text="Lent books", font=",12", anchor="center")
loanBookTitle.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 10))

userCodeLabel = ttk.Label(loansSection, text="User code:")
userCode = ttk.Entry(loansSection, textvariable=userCodeVar)
userCodeLabel.grid(row=1, column=0, sticky="w")
userCode.grid(row=2, column=0)

loanBookSubmit = ttk.Button(loansSection, text="Check books", command=addBook)
loanBookSubmit.grid(row=2, column=1, sticky="e", padx=(20, 0))

loanBookMessage = ttk.Label(loansSection, textvariable=loanBookMessageVar)
loanBookMessage.grid(row=3, column=0, sticky="w", pady=(10, 0))


# - Stampa

# print di titoli, autori, nomi, codici
# mettere un messaggio personalizzato in base all'azione scelta


# Azioni utenti

frameFront = Frame(root)
frameFront.grid(row=0, column=2, sticky="ne")  # -------------------------------------------


# - Registrazione

registerSection = Frame(frameFront)
registerSection.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

registerTitle = ttk.Label(registerSection, text="Register", font=",12")
registerTitle.grid(row=0, column=0, columnspan=2, sticky="nw", pady=(0, 10))

nameLabel = ttk.Label(registerSection, text="Enter your name:")
nameLabel.grid(row=1, column=0, columnspan=2, sticky="w", padx=(5, 0))
labelUserName = ttk.Entry(registerSection, textvariable=registerUserNameVar)
labelUserName.grid(row=2, column=0, sticky="w", padx=(5, 0))

userNameSubmit = ttk.Button(registerSection, text="Register", command=addUser)
userNameSubmit.grid(row=2, column=1, sticky="e", padx=(20, 0))

registerMessage = ttk.Label(registerSection, textvariable=registerMessageVar)
registerMessage.grid(row=3, column=0, columnspan=2, sticky="w", padx=(5, 0))

idMessage = ttk.Label(registerSection, textvariable=idCodeMessageVar)
idMessage.grid(row=4, column=0, columnspan=2, sticky="w", padx=(5, 0))


# - Prestito

borrowSection = Frame(frameFront)
borrowSection.grid(row=2, column=0, sticky="nw", padx=20, pady=20)


borrowTitle = ttk.Label(borrowSection, text="Get a book", font=",12")
borrowTitle.grid(row=0, column=0, columnspan=2, sticky="nw", pady=(0, 10))

titleLabel = ttk.Label(borrowSection, text="Enter book's title:")
titleLabel.grid(row=1, column=0, columnspan=2, sticky="w", padx=(5, 0))
labeltitle = ttk.Entry(borrowSection, textvariable=borrowTitleVar)
labeltitle.grid(row=2, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

authorLabel = ttk.Label(borrowSection, text="Enter book's author:")
authorLabel.grid(row=1, column=1, columnspan=2, sticky="w", padx=(5, 0))
labelauthor = ttk.Entry(borrowSection, textvariable=borrowAuthorVar)
labelauthor.grid(row=2, column=1, sticky="w", pady=(0, 20))

codeLabel = ttk.Label(borrowSection, text="Enter your id code:")
codeLabel.grid(row=3, column=0, columnspan=2, sticky="w", padx=(5, 0))
labelUserCode = ttk.Entry(borrowSection, textvariable=borrowUserCodeVar)
labelUserCode.grid(row=4, column=0, sticky="w", padx=(0, 20))

borrowBookSubmit = ttk.Button(borrowSection, text="Get book", command=getBook)
borrowBookSubmit.grid(row=4, column=1, sticky="e")

borrowMessage = ttk.Label(borrowSection, textvariable=borrowMessageVar)
borrowMessage.grid(row=5, column=0, columnspan=2, sticky="w", padx=(5, 0))


# - Restituzione

returnSection = Frame(frameFront)
returnSection.grid(row=4, column=0, sticky="nw", padx=20, pady=20)

returnTitle = ttk.Label(returnSection, text="Return a book", font=",12")
returnTitle.grid(row=0, column=0, columnspan=2, sticky="nw", pady=(0, 10))

titleLabel = ttk.Label(returnSection, text="Enter book's title:")
titleLabel.grid(row=1, column=0, columnspan=2, sticky="w", padx=(5, 0))
labeltitle = ttk.Entry(returnSection, textvariable=returnTitleVar)
labeltitle.grid(row=2, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

authorLabel = ttk.Label(returnSection, text="Enter book's author:")
authorLabel.grid(row=1, column=1, columnspan=2, sticky="w", padx=(5, 0))
labelauthor = ttk.Entry(returnSection, textvariable=returnAuthorVar)
labelauthor.grid(row=2, column=1, sticky="w", pady=(0, 20))

returnBookSubmit = ttk.Button(returnSection, text="Return book", command=addUser)
returnBookSubmit.grid(row=4, column=1, sticky="e")

returnMessage = ttk.Label(returnSection, textvariable=returnMessageVar)
returnMessage.grid(row=5, column=0, columnspan=2, sticky="w", padx=(5, 0))


# Divisori

Frame(root, width=2, background="#121212").grid(row=0, column=1, sticky="ns", pady=10)
Frame(frameBack, width=2, background="#121212").grid(row=0, column=1, rowspan=3, sticky="ns", pady=10)
Frame(frameBack, height=2, background="#121212").grid(row=1, column=0, columnspan=3, sticky="we", padx=10)

Frame(frameFront, height=2, background="#121212").grid(row=1, column=0, sticky="we", padx=10)
Frame(frameFront, height=2, background="#121212").grid(row=3, column=0, sticky="we", padx=10)


root.mainloop()
