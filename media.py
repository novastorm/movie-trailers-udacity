import json
import os
import webbrowser

class Movie(object):
	"""A movie related information store"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, us_release_date):
		self._title = movie_title
		self._storyline = movie_storyline
		self._poster_image_url = poster_image
		self._trailer_youtube_url = trailer_youtube
		self._us_release_date = us_release_date

	@property
	def title(self):
		"""Get the title"""
		return self._title

	@property
	def storyline(self):
		"""Get the storyline"""
		return self._storyline

	@property
	def poster_image_url(self):
		"""Get the poster image URL"""
		return self._poster_image_url

	@property
	def trailer_youtube_url(self):
		"""Get the YouTube trailer URL"""
		return self._trailer_youtube_url

	@property
	def us_release_date(self):
		"""Get the US release date"""
		return self._us_release_date

	def show_trailer(self):
		webbrowser.open(self._trailer_youtube_url)


class Movie_Collection(object):
	"""A collection of Movie records"""

	def __init__(self):
		self._collection = []
		self._database_filename = ""

	@property
	def collection(self):
		return self._collection

	@property
	def database_filename(self, filename):
		if filename:
			self._database_filename = filename
			return self
		return _database_filename

	@classmethod
	def init_with_filename(cls, filename):
		self = cls()
		self._database_filename = filename
		return self

	def load_data(self, filename=None):
		if filename: self._database_filename = filename

		assert os.path.exists(self._database_filename), \
			'%s File does not exist' % self._database_filename

		with open(self._database_filename) as movie_data_file_handle:
			movie_data = json.load(movie_data_file_handle)
		movie_data_file_handle.close()

		for record in movie_data:
			movie = Movie(
				record['title'],
				record['storyline'],
				record['poster_image_url'],
				record['trailer_youtube_url'],
				record['release_date']['US']
				)
			self._collection.append(movie)

		return self._collection

