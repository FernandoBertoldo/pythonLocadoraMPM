from infra.repository.filme_repository import FilmeRepository
from infra.configs.connection import DBConnectionHandler
from infra.entities.models import Filme, Ator


repo = FilmeRepository()
data_base = DBConnectionHandler()

filme_1=Filme(
    titulo='Barbie',
    genero='Terror',
    ano=2023
)

filme_2=Filme(
    titulo='Spawn',
    genero='Ação',
    ano=1997
)

margot=Ator(
    nome='Margot Robbie',
    nascimento=1990
)

ryan=Ator(
    nome='Ryan Google',
    nascimento=1980
)

atores=[margot, ryan]


filme_1.atores=atores
filme_2.atores=atores

repo.insert(filme_1)
repo.insert(filme_2)
#colsultamos e printamos todas os dados da base
filmes = repo.select_all()
print(filmes)

#Atualizamos um filme atraves do id
#repo.update()

#Consultamos o filme atraves do id
filme = repo.select_one(2)
print(filmes)

#Removemos um registro atraves do id

repo.delete(filme_1)

