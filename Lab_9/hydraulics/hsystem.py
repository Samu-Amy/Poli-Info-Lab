from hydraulics.elements import Element, Source, Tap, Split, Sink
from typing import List


class HSystem:
    def __init__(self) -> None:
        self._components = []
        self._simulationOutput = []

    def add_element(self, elm: Element) -> None:
        self._components.append(elm)

    def get_elements(self) -> List[Element]:
        return self._components

    def simulate(self) -> List[str]:
        self._simulationOutput = []
        type = None
        inFlow = 0
        outFlow = 0
        splitOutFlow = None
        previous = None
        next = None

        for element in self._components:
            valid = False
            if isinstance(element, Source):
                type = "Source"
                outFlow = element.get_flow()
                next = [element.get_output()]  # Uso una lista per il ciclo for successivo (altrimenti non funziona)
                valid = True

            while not valid:
                for index in range(len(next)):  # Controlla una connessione per volta

                    if element == next[index]:  # Controllo il collegamento
                        valid = True
                        break
                    else:
                        i = 0
                        while i < len(self._components) and not valid:
                            try:
                                nextItem = self._components[i].get_output()
                            except:
                                nextItem = self._components[i].get_outputs()[0]

                            if element == nextItem:
                                outFlow = float(self._simulationOutput[i].split()[-1])  # Prendo il flusso in uscita dell'elemento precedente
                                valid = True
                                break

                            i += 1

            if isinstance(element, Tap):
                previous = type  # Salvo il tipo dell'oggetto precedente
                type = "Tap"

                if previous != "Sink":
                    inFlow = outFlow
                else:
                    inFlow = splitOutFlow[index]

                if element.get_status():  # Aperto
                    outFlow = inFlow
                else:                     # Chiuso
                    outFlow = 0

                next = [element.get_output()]


            elif isinstance(element, Split):
                previous = type
                type = "Split"

                if previous != "Sink":
                    inFlow = outFlow
                else:
                    inFlow = splitOutFlow[index]

                outFlow = (inFlow/2, inFlow/2)
                splitOutFlow = outFlow
                outFlow = splitOutFlow[index]

                next = element.get_outputs()

            elif isinstance(element, Sink):
                previous = type
                type = "Sink"
                if previous != "Sink":
                    inFlow = outFlow
                else:
                    inFlow = splitOutFlow[index]
                outFlow = 0


            if type != "Split":
                self._simulationOutput.append(f"{type} {element.get_name()} {inFlow :.3f} {outFlow :.3f}")
            else:
                self._simulationOutput.append(f"{type} {element.get_name()} {inFlow :.3f} {splitOutFlow[0] :.3f} {splitOutFlow[1] :.3f}")

        return self._simulationOutput


