from resource import Resource

class Profiles(Resource):
  
  def artist(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

  def search(self, url):
    return self.get(self.genUrl( ), {'q':query})
  
  def add(self, profiles):
    return self.post(self.genUrl( ), {'profiles':profiles, 'key':'ad644d582c7dcf7dc29479ff2d4df1ef'})
