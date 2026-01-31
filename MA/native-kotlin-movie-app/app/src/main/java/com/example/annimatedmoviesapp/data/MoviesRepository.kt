package com.example.animatedmoviesapp.data

import com.example.animatedmoviesapp.data.models.Movie
import com.example.annimatedmoviesapp.data.local.DataProvider
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.map

class MoviesRepository {
    private val _movies = MutableStateFlow<List<Movie>>(
        DataProvider.movies
    ) // val in order to not be changed to another List
    private val movies: Flow<List<Movie>> = _movies.asStateFlow()
    private var nextMovieId = 11

    fun getAllMovies(): Flow<List<Movie>> = movies

    fun getMovieByID(id: Int): Flow<Movie?> =
        movies.map { movieList -> movieList.find { it.id == id } }

    fun addMovie(movie: Movie) {
        val newMovie = movie.copy(id = nextMovieId++)
        _movies.value += newMovie
    }

    fun updateMovie(movie: Movie) {
        _movies.value = _movies.value.map { if (it.id == movie.id) movie else it }
    }

    fun deleteMovie(id: Int) {
        _movies.value = _movies.value.filter { it.id != id }
    }


}