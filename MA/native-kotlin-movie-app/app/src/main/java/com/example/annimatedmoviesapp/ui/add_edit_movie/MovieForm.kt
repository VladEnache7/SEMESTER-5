import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CornerSize
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.animatedmoviesapp.data.models.Movie

@Composable
fun MovieForm(pageTitle: String, movie: Movie, onSave: (Movie) -> Unit, onCancel: () -> Unit) {
    var name by remember { mutableStateOf(movie.name) }
    var genre by remember { mutableStateOf(movie.genre) }
    var description by remember { mutableStateOf(movie.description) }
    var durationStr by remember { mutableStateOf(movie.duration.toString()) }
    var yearStr by remember { mutableStateOf(movie.year.toString()) }

    val isYearError = yearStr.toIntOrNull() == null
    val isDurationError = durationStr.toIntOrNull() == null

    Column(
        modifier = Modifier
            .padding(20.dp)
            .fillMaxWidth()
            .fillMaxSize()
            .clip(RoundedCornerShape(CornerSize(40.dp)))
            .background(Color(0xFFADBBDA)),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = pageTitle,
            fontSize = 30.sp,
            modifier = Modifier.padding(top = 40.dp, bottom = 10.dp),
            fontWeight = FontWeight.Bold,
            textAlign = TextAlign.Center,

            )
        Spacer(modifier = Modifier.padding(8.dp))
        TextField(value = name, onValueChange = { name = it }, label = { Text("Name") })
        Spacer(modifier = Modifier.padding(8.dp))
        TextField(value = genre, onValueChange = { genre = it }, label = { Text("Genre") })
        Spacer(modifier = Modifier.padding(8.dp))
        TextField(
            value = yearStr,
            onValueChange = { yearStr = it },
            label = { Text("Year") },
            isError = isYearError,
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal)
        )
        Spacer(modifier = Modifier.padding(8.dp))
        TextField(
            value = durationStr,
            onValueChange = { durationStr = it },
            label = { Text("Duration") },
            isError = isDurationError,
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal)
        )
        Spacer(modifier = Modifier.padding(8.dp))
        TextField(
            value = description,
            onValueChange = { description = it },
            label = { Text("Description") },
            modifier = Modifier.padding(16.dp)
        )
        if (isYearError or isDurationError) {
            Text(
                "Year and duration must contains only integer values!",
                color = Color.Red,
                modifier = Modifier.padding(15.dp)
            )
        }
        Row {
            Button(
                onClick = {
                    val movie = Movie(
                        id = movie.id,
                        name = name,
                        genre = genre,
                        year = yearStr.toIntOrNull() ?: 0,
                        description = description,
                        duration = durationStr.toIntOrNull() ?: 0
                    )
                    onSave(movie)
                },
                enabled = (!isYearError && !isDurationError && name != "")
            ) {
                Text("Save")
            }
            Spacer(modifier = Modifier.width(8.dp))
            Button(
                onClick = { onCancel() }
            ) {
                Text("Cancel")
            }
        }
    }
}