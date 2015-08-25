class Video():
	"""main class, create vars and methods for other two classes"""
	def __init__(self, title, duration, image):
		self.title = title
		self.duration = duration
		self.image = image

class Movie(Video):
	"""class for movies"""
	def __init__(self, title, duration, image, storyline, youtube_trailer):
		Video.__init__(self, title, duration, image)
		self.storyline = storyline
		self.youtube_trailer = youtube_trailer

	def show_trailer(self):
		print 'watch trailer at: ' + self.youtube_trailer

class TvShow(Video):
	"""class for videos"""
	def __init__(self, season, episode, tv_station):
		Video.__init__(self, title, duration, image)
		self.season = season
		self.episode = episode
		self.tv_station = tv_station

	def get_local_listing(self):
		print 'local listing at: ' + self.tv_station

midnight_in_paris = Movie('Midnight In Paris', 97, 'midnight.jpg', 'Owen Wilson kicking it with Lit greats', 'youtube/midnight.com')

print midnight_in_paris.title
midnight_in_paris.show_trailer()