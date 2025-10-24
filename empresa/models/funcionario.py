from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional

@dataclass
class Funcionario:

    _cpf: str
    _pnome: str
    _unome: str
    _data_nasc: date
    _endereco: str = 'Macau-Rn'
    _salario: float = 1518.01
    _sexo: str = 'f'
    _cpf_supervisor: Optional[str] = None
    _numero_departamento: Optional[int] = None
    _create_at: Optional[datetime] = None
    _update_at: Optional[datetime] = None

    # Funcionario -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Funcionario
    @classmethod
    def from_dict(self, data: dict) -> 'Funcionario':
        return Funcionario(
            data.get('cpf'), 
            data.get('pnome'),
            data.get('unome'),
            data.get('data_nasc'),
            data.get('endereco'),
            data.get('salario'),
            data.get('sexo'),
            data.get('cpf_supervisor'),
            data.get('numero_departamento'),
            data.get('create_at'),
            data.get('update_at'),
        )
    
    def __str__(self) -> str:
        return (f"Funcionario(cpf={self._cpf}, pnome={self._pnome}, unome={self._unome}, data_nasc={self._data_nasc}, endereco={self._endereco}, "f"salario={self._salario}, sexo={self._sexo}, cpf_supervisor={self._cpf_supervisor}, numero_departamento={self._numero_departamento}, "f"create_at={self._create_at}, update_at={self._update_at})")
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf
        self._update_at = datetime.now()

    @property
    def pnome(self) -> str:
        return self._pnome
    
    @pnome.setter
    def pnome(self, pnome: str):
        self._pnome = pnome
        self._update_at = datetime.now()

    @property
    def unome(self) -> str:
        return self._unome
    
    @unome.setter
    def unome(self, unome: str):
        self._unome = unome
        self._update_at = datetime.now()

    @property
    def data_nasc(self) -> date:
        return self._data_nasc
    
    @data_nasc.setter
    def data_nasc(self, data_nasc: date):
        self._data_nasc = data_nasc
        self._update_at = datetime.now()

    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        self._endereco = endereco
        self._update_at = datetime.now()

    @property
    def salario(self) -> float:
        return self._salario
    
    @salario.setter
    def salario(self, salario: float):
        self._salario = salario
        self._update_at = datetime.now()

    @property
    def sexo(self) -> str:
        return self._sexo
    
    @sexo.setter
    def sexo(self, sexo: str):
        self._sexo = sexo
        self._update_at = datetime.now()

    @property
    def cpf_supervisor(self) -> Optional[str]:
        return self._cpf_supervisor
    
    @cpf_supervisor.setter
    def cpf_supervisor(self, cpf_supervisor: Optional[str]):
        self._cpf_supervisor = cpf_supervisor
        self._update_at = datetime.now()

    @property
    def numero_departamento(self) -> Optional[int]:
        return self._numero_departamento   
    
    @numero_departamento.setter
    def numero_departamento(self, numero_departamento: Optional[int]):
        self._numero_departamento = numero_departamento
        self._update_at = datetime.now()

    @property
    def create_at(self) -> Optional[datetime]:
        return self._create_at
    
    @create_at.setter
    def create_at(self, create_at: Optional[datetime]):
        self._create_at = create_at
    
    @property
    def update_at(self) -> Optional[datetime]:
        return self._update_at
    
    @update_at.setter
    def update_at(self, update_at: Optional[datetime]):
        self._update_at = update_at