class Category:


    def __init__(self,id,title,date):
        self.id = id
        self.title = title
        self.time = time


class User():
    __tablename__ = 'users'

    id = db.column(db.Integer,primary_key = True)
