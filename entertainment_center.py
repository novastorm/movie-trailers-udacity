import fresh_tomatoes
import media

"""Compile movie trailer website"""

def main():
	movies = media.Movie_Collection().init_with_filename('movie_data.json').load_data()
	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
	main()