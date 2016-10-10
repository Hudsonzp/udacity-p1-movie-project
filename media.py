import webbrowser


class Movie():
    def __init__(self, title, storyline, poster_image, trailer_url):
        """initializes a movie in memory

        Attributes:
             title: Title of the movie
             storyline: storyline for the selected movie
             poster_image: url containing an image from around the web
             trailer_url: direct youtube link to the trailer that will
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """opens browser and plays trailer"""
        webbrowser.open(self.trailer_youtube_url)
