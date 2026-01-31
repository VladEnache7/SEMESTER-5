package com.example.annimatedmoviesapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import com.example.animatedmoviesapp.data.MoviesRepository
import com.example.annimatedmoviesapp.ui.movielist.MovieRecyclerView
import com.example.annimatedmoviesapp.ui.theme.AnnimatedMoviesAppTheme


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        val moviesRepo = MoviesRepository()
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AnnimatedMoviesAppTheme {
                MovieRecyclerView(
                    moviesRepo = moviesRepo,
                )
            }
        }
    }
}


@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    AnnimatedMoviesAppTheme {
        Text(text = "Android2")
    }
}

