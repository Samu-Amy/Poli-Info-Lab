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
            if isinstance(element, Source):
                type = "Source"
                outFlow = [element.get_flow()]  # Uso una lista per la selezione dagli split con l'indice
                next = [element.get_output()]  # Uso una lista per il ciclo for successivo (altrimenti non funziona)


            for index in range(len(next)):  # Controlla una connessione per volta

                if element == next[index]:

                    if isinstance(element, Tap):
                        previous = type  # Salvo il tipo dell'oggetto precedente
                        type = "Tap"

                        if previous != "Sink":
                            inFlow = outFlow[index]
                        else:
                            inFlow = splitOutFlow[index]

                        if element.get_status():  # Aperto
                            outFlow = [inFlow]
                        else:                     # Chiuso
                            outFlow = [0]

                        next = [element.get_output()]


                    elif isinstance(element, Split):
                        previous = type
                        type = "Tap"

                        if previous != "Sink":
                            inFlow = outFlow[index]
                        else:
                            inFlow = splitOutFlow[index]

                        outFlow = (inFlow/2, inFlow/2)
                        splitOutFlow = outFlow

                        next = element.get_outputs()

                    elif isinstance(element, Sink):
                        type = "Sink"
                        inFlow = outFlow[index]  # TODO: devo salvare l'outFlow dello split
                        outFlow = [0]


            if type != "Split":
                self._simulationOutput.append(f"{type} {element.get_name()} {inFlow :.3f} {outFlow[0] :.3f}")
            else:
                self._simulationOutput.append(f"{type} {element.get_name()} {inFlow :.3f} {outFlow[0] :.3f} {outFlow[1] :.3f}")

        return self._simulationOutput


