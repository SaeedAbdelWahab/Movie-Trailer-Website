class Movie():
    """
    A class movie which contains some movie attributes (story, trailer, image,
    title)
    """
    def __init__(self, movie_title, movie_poster_image, movie_youtube_url,
                 movie_story):
        self.title = movie_title
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_url
        self.story = movie_story