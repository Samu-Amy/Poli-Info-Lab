import operator
file_name = input("Inserire il nome del file: ")
infile = open(file_name + ".txt")
line = infile.readline().lower()
parole = {}

# if line != "\n":
#     cleanLine = line.strip(" \n.,-_:;»").replace(",",'').replace(".",'').replace("»",'').replace("_",'').replace("\"",'').split()
#
# while line != "":
#     if line != "\n":
#         print(cleanLine)
#         cleanLine = line.strip(" \n.,-_:;»").replace(",",'').replace(".",'').replace("»",'').replace("_",'').replace("\"",'').split()
#
#     line = infile.readline()


# Creazione dizionario contenente tutte le parole e il conteggio

while line != "":
    if line != "\n":
        cleanLine = line.strip().replace(".",'').split()
        for parola in cleanLine:
            if parole.get(parola) != None:
                parole[parola] += 1
            else:
                parole[parola] = 1

    line = infile.readline().lower()


classifica = sorted(parole.items(), key = operator.itemgetter(1), reverse = True)

print(classifica)

for i in classifica:
    print(str(i[1]) + " volte - " + i[0])
