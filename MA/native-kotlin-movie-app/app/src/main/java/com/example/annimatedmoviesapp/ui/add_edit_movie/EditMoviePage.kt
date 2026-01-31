package com.example.annimatedmoviesapp.ui.add_edit_movie

import MovieForm
import androidx.compose.runtime.*
import com.example.animatedmoviesapp.data.models.Movie

@Composable
fun EditMoviePage(movie: Movie, onSave: (Movie) -> Unit, onCancel: () -> Unit) {
    MovieForm(pageTitle = "Edit Movie", movie = movie, onSave = onSave, onCancel = onCancel)
}
