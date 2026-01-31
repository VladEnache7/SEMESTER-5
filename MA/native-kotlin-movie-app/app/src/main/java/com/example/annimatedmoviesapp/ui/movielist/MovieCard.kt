package com.example.annimatedmoviesapp.ui.movielist

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CornerSize
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.animatedmoviesapp.data.models.Movie
import com.example.annimatedmoviesapp.R

fun String.insertNewlinesBeforeNChars(n: Int): String {
    val sb = StringBuilder(this)
    var i = n
    while (i < sb.length) {
        val spaceIndex = sb.lastIndexOf(' ', i)
        if (spaceIndex != -1) {
            sb.setCharAt(spaceIndex, '\n')
            i = spaceIndex + n + 1
        } else {
            sb.insert(i, '\n')
            i += n + 1
        }
    }
    return sb.toString()
}

/**
 * Composable function for displaying a movie card
 *
 * @param movie: The movie that will be displayed on the card
// * @param onMovieClick: A function that will handle the case when the user click on a movie
 */
@Composable
fun MovieCard(
    movie: Movie,
    goToEditPage: (Movie) -> Unit,
    onDeleteClick: (Int) -> Unit
) {

    var showDialog by remember { mutableStateOf(false) }

    if (showDialog) {
        AlertDialog(
            onDismissRequest = { showDialog = false },
            title = { Text("Delete Movie") },
            text = { Text("Are you sure you want to delete this movie?") },
            confirmButton = {
                Button(
                    onClick = {
                        onDeleteClick(movie.id)
                        showDialog = false
                    }
                ) {
                    Text("Confirm")
                }
            },
            dismissButton = {
                Button(
                    onClick = { showDialog = false }
                ) {
                    Text("Cancel")
                }
            }
        )
    }

    Card(
        modifier = Modifier
            .padding(start = 15.dp, top = 15.dp, end = 15.dp)
            .fillMaxWidth(),
        shape = RoundedCornerShape(CornerSize(20.dp)),
        elevation = CardDefaults.cardElevation(defaultElevation = 10.dp),
        onClick = { goToEditPage(movie) },
        colors = CardDefaults.cardColors(
            Color(0xFFADBBDA)
        )
    ) {
        Row(modifier = Modifier.padding(8.dp)) {
            Image(
                painter = painterResource(id = R.drawable.img),
                contentDescription = "image",
                modifier = Modifier
                    .padding(8.dp)
                    .size(80.dp)
                    .clip(RoundedCornerShape(CornerSize(6.dp)))
                    .align(Alignment.CenterVertically)
            )
            Column(modifier = Modifier.padding(8.dp)) {
                Text(
                    text = movie.name.insertNewlinesBeforeNChars(17),
                    fontSize = 20.sp, // if (movie.name.length < 20) 20.sp else 12.sp,
                    fontWeight = FontWeight.Bold,
                    modifier = Modifier.padding(bottom = 4.dp)
                )
                Text(
                    text = "Genre: ${movie.genre}",
                    fontSize = 14.sp,
                    modifier = Modifier.padding(bottom = 2.dp)
                )
                Text(
                    text = "Year: ${movie.year}",
                    fontSize = 14.sp,
                    modifier = Modifier.padding(bottom = 2.dp)
                )
                Text(
                    text = "Duration: ${movie.duration} min",
                    fontSize = 14.sp
                )
            }
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 8.dp)
                    .align(Alignment.CenterVertically),
                horizontalAlignment = Alignment.End,
                verticalArrangement = Arrangement.Center
            ) {

                Button(
                    onClick = {
                        showDialog = true
                    },
                ) {
                    Text("Delete")
                }
            }

        }
    }
}
