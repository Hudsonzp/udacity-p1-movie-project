import fresh_tomatoes
import media

the_matrix = media.Movie("The Matrix",
                         "Thomas Anderson is Neo is a young software engineer"
                         " and part-time hacker who is singled out by some"
                         " mysterious figures who want to introduce him into"
                         " the secret of 'the matrix'. The cops also seem to"
                         "  be after him, and he takes a chance on discovering"
                         "  what he has always suspected: that the world is "
                         " not quite what it seems to be and a sinister"
                         " conspiracy is at work.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Vincent Vega and Jules Winnfield are hitmen with a"
                           " penchant for philosophical discussions. In this"
                           " ultra-hip, multi-strand crime movie, their "
                           " storyline is interwoven with those of their boss,"
                           " gangster Marsellus Wallace ; his actress wife,"
                           " Mia; struggling boxer Butch Coolidge; master"
                           " fixer Winston Wolfe and a nervous pair of armed"
                           " robbers, Pumpkin and Honey Bunny",
                           "http://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")

donnie_darko = media.Movie("Donnie Darko",
                           "The film follows the adventures of the troubled"
                           " title character as he seeks the meaning behind"
                           " his Doomsday-related visions.",
                           "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=qdKbNuhXWvQ")

movies = [the_matrix, pulp_fiction, donnie_darko]  # Array of movies to load
fresh_tomatoes.open_movies_page(movies)  # Starts the html page with movies
