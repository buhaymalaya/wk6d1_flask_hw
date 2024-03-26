# # create python class that will be a SQL table; same as ddl.sql think: rules of the tables

from datetime import datetime
from app import db

class MovieModel(db.Model):

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    body = db.Column(db.String, nullable  = False)
    year = db.Column(db.Integer, nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)

    director = db.relationship("DirectorModel", back_populates='movie')

    def from_dict(self, a_dict):

        self.title = a_dict['title']
        setattr(self, 'body', a_dict['body'])
        setattr(self, 'director_id', int(a_dict['director_id'] ))

    def save_movie(self):
        db.session.add(self)
        db.session.commit()

    def del_movie(self):
        db.session.delete(self)
        db.session.commit()



 
