package com.example.annimatedmoviesapp.ui.add_edit_movie

import MovieForm
import androidx.compose.runtime.*
import com.example.animatedmoviesapp.data.models.Movie

@Composable
fun AddMoviePage(onAdd: (Movie) -> Unit, onCancel: () -> Unit) {
    MovieForm("Add Movie", Movie(), onSave = onAdd, onCancel = onCancel)
}