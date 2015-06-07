# import necessary modules 
import webbrowser

# define Movie class to store movie information and to show trailer
class Movie():
    # Construct init function in order to 
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    # using webbrowser module to open trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
#define Movies class to collect movies
class Movies():
    # define init function initiate a array to store movies
    def __init__(self):
        self.store = []

    # define add funtion to create a movie and store into araay
    def add(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        single_movie=Movie(movie_title,movie_storyline,poster_image,trailer_youtube)
        self.store.append(single_movie)
        return single_movie


