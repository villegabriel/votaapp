from Song import *
import random

class SongData():
    acceso_a_datos = DataAccess()
    def add_song(self,song):
        """
        Inserta un nuevo socio en la base de datos.
        :param socio: Objeto Socio a insertar.
        :return:
        """
        session = self.acceso_a_datos.get_session()
        session.add(song)
        session.commit()

    def delete_song(self,song):
        """
        Elimina un socio en la base de datos.
        :param idSocio: Numero de ID del socio a eliminar.
        :return:
        """
        session = self.acceso_a_datos.get_session()
        session.delete(song)
        session.commit()

    def modify_song(self,song):
        """
        Modifica un socio de la base de datos.
        :param socio: Objeto Socio con los nuevos valores a guardar.
        :return:
        """
        session = self.acceso_a_datos.get_session()
        session.save(song)
        session.commit()

    def buscar_por_id(self,id_song):
        """
        Busca un socio en la base de datos.
        :param idSocio: Numero de ID del socio a buscar.
        :return: El socio si es encontrado, None si no lo encuentra.
        """
        session = self.acceso_a_datos.get_session()
        return session.query(Song).filter_by(id_song= id_song).first()


    def get_all(self):
        """
        Busca todos los socios y su informacion de la base de datos.
        :return: Una lista con todos los objetos Socio obtenidos.
        """
        session = self.acceso_a_datos.get_session()
        return session.query(Song).all()

    def get_n_random_songs(self,n):
        return random.sample(self.get_all(),n)
