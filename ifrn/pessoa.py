from abc import ABC, abstractmethod

class Pessoa(ABC):

    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @abstractmethod
    def __str__(self):
        return f'(nome: {self._nome}, cpf: {self._cpf}'

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, nome):
        self._cpf = nome