from marshmallow import Schema, fields

class MovieSchema(Schema):
    movie_id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str()
    year = fields.Int(required=True)
    director_id = fields.Int(required=True)

class DirectorSchema(Schema):
    director_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    imdb_rating = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()



class MovieWithDirectorSchema(MovieSchema):
    director = fields.Nested(DirectorSchema)

class DirectorWithMovieSchema(DirectorSchema):
    movie = fields.List(fields.Nested(MovieSchema), dump_only=True)
    