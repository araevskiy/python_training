from sys import maxsize



class Contact:

    def __init__(self, firstname=None, secondname=None, id=None):
        self.firstname = firstname
        self.secondname = secondname
        self.id = id

    def __repr__(self):
        return "%s : %s : %s" % (self.id, self.firstname, self.secondname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.secondname == other.secondname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
