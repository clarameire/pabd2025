from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional

@dataclass
class Departamento:
    _numero: int
    _nome: str
    _cpf_gerente: str
    _data_ini: date
    _created_at: Optional[datetime] = None
    _updated_at: Optional[datetime] = None

    # Departamento -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Departamento
    @classmethod
    def from_dict(self, data: dict) -> 'Departamento':
        return Departamento (
            data.get('numero'),
            data.get('nome'),
            data.get('cpf_gerente'),
            data.get('data_ini'),
            data.get('created_at'),
            data.get('updated_at'),
        )
    
    def __str__(self) -> str:
        return (
            f"Departamento(numero={self._numero}, nome={self._nome}, cpf_gerente={self._cpf_gerente}, data_ini={self._data_ini}, created_at={self._created_at}, updated_at={self._updated_at})"
        )
        
    
    @property
    def numero(self) -> int:
        return self._numero
    
    @numero.setter
    def numero(self, numero: int):
        self._numero = numero
        self._updated_at = datetime.now()

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
        self._updated_at = datetime.now()

    @property
    def cpf_gerente(self) -> str:
        return self._cpf_gerente
    
    @cpf_gerente.setter
    def cpf_gerente(self, cpf_gerente: str):
        self._cpf_gerente = cpf_gerente
        self._updated_at = datetime.now()

    @property
    def data_ini(self) -> date:
        return self._data_ini
    
    @data_ini.setter
    def data_ini(self, data_ini: date):
        self._data_ini = data_ini
        self._updated_at = datetime.now()

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at
    @created_at.setter
    def created_at(self, created_at: Optional[datetime]):
        self._created_at = created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at: Optional[datetime]):
        self._updated_at = updated_at