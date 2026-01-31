package com.example.annimatedmoviesapp.ui.movielist


import android.os.Handler
import android.os.Looper
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.*
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.animatedmoviesapp.data.MoviesRepository
import com.example.animatedmoviesapp.data.models.Movie
import com.example.annimatedmoviesapp.ui.add_edit_movie.AddMoviePage
import com.example.annimatedmoviesapp.ui.add_edit_movie.EditMoviePage


/**
 * Composable function for displaying a RecyclerView of user cards.
 *
 * @param moviesRepo: The repository of the movies
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MovieRecyclerView(moviesRepo: MoviesRepository) {
    val movies by moviesRepo.getAllMovies().collectAsState(initial = emptyList())
    var isLoading by remember { mutableStateOf(false) }
    var triggerEffect by remember { mutableStateOf(false) }
    var selectedMovie by remember { mutableStateOf<Movie?>(null) }
    var isAddingMovie by remember { mutableStateOf(false) }

    if (triggerEffect) {
        LaunchedEffect(Unit) {
            kotlinx.coroutines.delay(1000)
            isLoading = false
            triggerEffect = false
        }
    }
    print("something")
    Box(modifier = Modifier.fillMaxSize()) {
        when {
            selectedMovie != null -> {
                EditMoviePage(
                    movie = selectedMovie!!,
                    onSave = { updatedMovie ->
                        moviesRepo.updateMovie(updatedMovie)
                        selectedMovie = null
                    },
                    onCancel = {
                        selectedMovie = null
                    }
                )
            }

            isAddingMovie -> {
                AddMoviePage(
                    onAdd = { newMovie ->
                        moviesRepo.addMovie(newMovie)
                        isAddingMovie = false
                    },
                    onCancel = {
                        isAddingMovie = false
                    }
                )
            }

            else -> {
                Scaffold(
                    topBar = {
                        TopAppBar(
                            title = { Text("Movie List") },
                            actions = {
                                IconButton(onClick = { /* Handle search action */ }) {
                                    Icon(Icons.Default.Search, contentDescription = "Search")
                                }
                            },
                            colors = TopAppBarDefaults.topAppBarColors(
                                containerColor = Color(
                                    0xFF1abc9c
                                )
                            )
                        )
                    },
                    content = { paddingValues ->
                        LazyColumn(
                            contentPadding = paddingValues
                        ) {
                            items(movies) { movie ->
                                MovieCard(
                                    movie = movie,
                                    goToEditPage = { selectedMovie = it },
                                    onDeleteClick = {
                                        isLoading = true
                                        triggerEffect = true
                                        Handler(Looper.getMainLooper()).postDelayed(
                                            {
                                                // This method will be executed once the timer is over
                                                moviesRepo.deleteMovie(movie.id)
                                            },
                                            1000 // value in milliseconds
                                        )
                                    }
                                )
                            }
                        }
                    },
                    floatingActionButton = {
                        FloatingActionButton(onClick = { isAddingMovie = true }) {
                            Text("+", fontWeight = FontWeight.Bold, fontSize = 30.sp)
                        }
                    }
                )
                if (isLoading) {
                    Box(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(16.dp),
                        contentAlignment = Alignment.Center
                    ) {
                        CircularProgressIndicator(modifier = Modifier.size(60.dp))
                    }
                }
            }
        }
    }
}