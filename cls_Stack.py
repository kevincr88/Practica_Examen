giy"""===========================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-311 - Programación III
Period.......: I-2022
Documents....: Exam_01 - 01_Stack
Goals........: Stack declaration (private data structure and public accessors methods).
Description..: A stack is a simple data structure, to store single data most the times.
               A stack is lifo structure, in others words has a behavior last in - first out.
               A stack is composed by:
                 - function empty().......: return a boolean value as current stack status ('in empty').
                 - function full()........: same that last one description ('in full').
                 - function push(<value>).: store a single value into stack internal memory.
                 - function pop().........: retrieve the last inserted value from stack internal memory.

               The internal memory is small, an array controlled by a positional variable,
               and both has private declaration.
Professor....: Jorge Ruiz (york)
Student......:
==========================================================================================================="""
class cls_Stack:

    def __init__(self):
        self._contenedor = ["", "", "", "", "", "", "", "", "", ""]
        self._posi = -1

    def empty(self):
        return self._posi == -1

    def full(self):
        return self._posi == self._contenedor.__len__() - 1

    def push(self, valor):
        self._posi += 1
        self._contenedor[self._posi] = valor

    def pop(self):
        aux = self._contenedor[self._posi]
        self._posi -= 1
        return aux
