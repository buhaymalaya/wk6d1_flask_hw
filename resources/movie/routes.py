from flask import jsonify
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from schemas import MovieSchema, MovieWithDirectorSchema
from . import bp

from models.movie_model import MovieModel

from app import db 

@bp.route('/movie')
class MovieList(MethodView):
    
    @bp.response(201, MovieWithDirectorSchema)
    @bp.arguments(MovieSchema)
    def post(self, movie_data):

        try:
            movie = MovieModel()
            movie.from_dict(movie_data)

            movie.save_movie()

            return movie
        except:
            abort(400, message=f"{movie.title} failed to post")



    @bp.response(200, MovieWithDirectorSchema(many=True))
    def get(self):
        return MovieModel.query.all()




@bp.route('/movie/<movie_id>')
class Movie(MethodView):

    @bp.response(200, MovieWithDirectorSchema)
    def get(self, movie_id):
        try: 
            return MovieModel.query.get(movie_id)
        except:
            abort(400, message="Movie not found")



    @bp.arguments(MovieSchema)
    @bp.response(201, MovieWithDirectorSchema)
    def put(self, movie_data, movie_id):
        
        movie = MovieModel.query.get(movie_id)

        if not movie:
            abort(400, message="Movie not found")

        if movie_data['director_id'] == movie.director_id:
            original_director_id = movie.director_id
            movie.from_dict(movie_data)
            movie.director_id = original_director_id

            movie.save_movie()
            return movie



    def delete(self, movie_id):

        movie = MovieModel.query.get(movie_id)

        if not movie:
            abort(400, message="Movie not found")

        movie.del_movie()
        return {'Message': f"Movie: {movie_id} deleted"}, 200

