from resource import Resource

class Artists(Resource):

  def view(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

  def search(self, query):
    return self.get(self.genUrl( ), {'q':query})

  def rank(self, type, ids):
    uids = ""    
    for i in ids:
	uids += str(i) + '-'
    uids = uids[:-1]
    return self.get(self.genUrl( ) + "/" + type + "/" + uids, "")

  def add(self, name, profiles):
    data = {}
    propost = ""
    for p in profiles:
      propost += p + ","
    propost = propost[:-1] # Snips the trailing comma
    print propost
    data['name'] = name
    data['profiles'] = propost
    data['key'] = 'ad644d582c7dcf7dc29479ff2d4df1ef'
    return self.post(self.genUrl( ), data)

