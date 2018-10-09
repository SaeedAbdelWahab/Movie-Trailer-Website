class Movie():
    """A class movie which have some movie attributes

    Attributes:
        title (str): the title of the movie
        post_image_url (str): The link to the image of the movie
        trailer_youtube_url (str): The link to the trailer
        story (str): the story of the movie
    """
    def __init__(self, movie_title, movie_poster_image, movie_youtube_url,
                 movie_story):
        self.title = movie_title
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_url
        self.story = movie_story
