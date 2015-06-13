import trailers
import media

"""Compile movie trailer website"""

def main():
	movies = media.Movie_Collection().init_with_filename('movie_data.json').load_data()
	trailers.open_movies_page(movies)

if __name__ == '__main__':
	main()