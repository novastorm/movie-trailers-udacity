import media
import trailers

from optparse import OptionParser

def main():
	parser = OptionParser()
	parser.add_option("-d", "--data", dest="datafile",
		help="import data from json DATAFILE", default="movie_data.json")
	parser.add_option("-o", "--output", dest="output",
		help="write data to FILE", default="trailers.html")

	"""Compile movie trailer website"""

	(options, args) = parser.parse_args()

	movies = media.Movie_Collection().init_with_filename(options.datafile).load_data()
	trailers.open_movies_page(movies, options.output)

if __name__ == '__main__':
	main()
