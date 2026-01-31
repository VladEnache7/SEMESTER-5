package com.example.animatedmoviesapp.data.models

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "movies")
data class Movie(
    @PrimaryKey(autoGenerate = true) val id: Int = 0, // Here a val (value, constant, read-only variable, immutable) because it is only assigned once and never changed
    var name: String = "", // the rest are variables because they will eventually be changed by the user
    var year: Int = 0,
    var genre: String = "",
    var description: String = "",
    var duration: Int = 0
)
