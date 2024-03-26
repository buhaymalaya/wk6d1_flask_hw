from app import db

from werkzeug.security import generate_password_hash, check_password_hash # stores/hashes user pw but will never see raw pw

# follow DirectorSchema class or else there will be conflicts
class DirectorModel(db.Model): 

    __tablename__ = "director" 

# create attribute for each UserSchema item below
    
    id = db.Column(db.Integer, primary_key=True) #define what data type
    username = db.Column(db.String(50), nullable = False, unique = True) #string is varchar; setting constraints
    email = db.Column(db.String(50), nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False) # we dont have access to the encryption key
    first_name = db.Column(db.String(75))
    last_name = db.Column(db.String(75))
    imdb_rating = db.Column(db.String)
    movie = db.relationship("MovieModel", back_populates="director", lazy= 'dynamic')


# will also have methods (think: dml, commands)

    def save_director(self): 
        db.session.add(self)
        db.session.commit()

    def del_director(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, director_dict):
        # loop through dict and set to the key
        for k, v in director_dict.items():
            if k != "password": # referring to schema
            #setattr function sets key
                setattr(self, k, v)
            else:
                setattr(self, "password_hash", generate_password_hash(v))