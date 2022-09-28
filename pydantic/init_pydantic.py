from pydantic import validate_arguments
from typing import Union
from pydantic.dataclasses import dataclass
from pydantic import BaseModel

# Validate em tempo de execucao se o valora dos parametros esta correto.
@validate_arguments 
def ex1(x:int,y:int):
    return x+y 

# print(ex1('a','b'))


@validate_arguments
def ex2(x:Union[int,str], y:Union[int, str]):
    return x+y 

# print(ex2(1,2))
# print(ex2('a','b'))


@dataclass
class Pessoa:
    nome: str
    idate: int

# print(Pessoa(nome='nome',idate=43))


class Cadastro(BaseModel):
    nome: str
    idade : int

# c=Cadastro(nome='matheus',idade= 24)
# print(c.nome)
# print(c.idade)


class Pessoa(BaseModel):
    nome: str
    idade : int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]


data=[
      {'nome':'matheus','idade':24},
      {'nome':'jayce','idade':26}  
     ]

# print(Pessoas(pessoas=data))

class Festa(BaseModel):
    maiores: Pessoas
    menores: Pessoas = []

data={'maiores': {'pessoas': [{'nome':'matheus','idade':24},{'nome':'jayce','idade':26}]}}
print(Festa(**data))