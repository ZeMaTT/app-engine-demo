from google.appengine.ext import ndb


class Todo(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.StringProperty()
    user = ndb.StringProperty()

    @staticmethod
    def get(id):
        key = ndb.Key(urlsafe=id)
        return key.get()

