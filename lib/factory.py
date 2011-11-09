from artists import Artists
from genres import Genres

class ResourceFactory:
  
  def __init__(self, key, ext):
    self.key = key
    self.ext = ext

  def getArtists(self):
    return Artists(self.key, self.ext)

  def getGenres(self):
    return Genres(self.key, self.ext)

  def getMetrics(self):
    return Metrics(self.key, self.ext)

  def getProfiles(self):
    return Profiles(self.key, self.ext)

  def getServices(self):
    return Services(self.key, self.ext)
