from infra.configs.connection import DBConnectionHandler
from infra.entities.models import Filme

class FilmeRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            filmes = db.session.query(Filme).all()
            return filmes


    def select_one(self, filme=None):
        with DBConnectionHandler() as db:
            if filme and isinstance(filme, Filme):
                f = db.session.query(Filme).filter(Filme.id == filme.id).first()
            else:
                f = db.session.query(Filme).first()
            return f


    def insert(self, data):
        with DBConnectionHandler() as db:
            if isinstance(data, list):
                db.session.add_all(data)
                db.session.commit()
            elif isinstance(data, Filme):
                db.session.add(data)
                db.session.commit()


    def update(self, filme):
        with DBConnectionHandler() as db:
            db.session.query(Filme).filter(Filme.id == filme.id).update(
                 {
                     'titulo': filme.titulo,
                     'genero': filme.genero,
                     'ano': filme.ano

                 }
             )
            db.session.commit()



    def delete(self, filme):
        with DBConnectionHandler() as db:
            db.session.delete(filme)
            db.session.commit()
