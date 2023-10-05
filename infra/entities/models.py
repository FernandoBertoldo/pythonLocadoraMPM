from sqlalchemy import Column, String, Integer, ForeignKey
from typing import List
from sqlalchemy import ForeignKey, Column, Table
from infra.configs.base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column

filme_ator = Table(
    "filme_ator",
    Base.metadata,
    Column("filme_id", ForeignKey("filmes.id"), primary_key=True),
    Column("ator_id", ForeignKey("atores.id"), primary_key=True),

)


# Criamos uma classe filme herdada Base (declarative_base)
class Filme(Base):
    #Definimos o nome da tabela
    __tablename__ = 'filmes'

    #Definimos os atributos e seus tipos de dados que serao criados na base
    id:Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero:Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    atores: Mapped[List["Ator"]] = relationship(secondary=filme_ator, cascade='all, delete',back_populates='filmes', passive_deletes=False, lazy='joined')


    #Sobrescrevemos a função magica que ocorre para apresentação doa dados do objeto desta classe
    def __repr__(self):
        return f'Filme[Titulo = {self.titulo}, Ano = {self.ano}] \n'


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    nascimento: Mapped[int] = mapped_column(nullable=False)
    filmes: Mapped[List[Filme]] = relationship(secondary=filme_ator, cascade='all, delete',back_populates='atores', passive_deletes=False, lazy='joined')

    def __repr__(self):
        return f'Ator[Nome = {self.nome}, Nascimento = {self.nascimento}] \n'
