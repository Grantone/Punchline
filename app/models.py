class Category:
    __tablename__ = 'categories'

    id = db.column(db.Integer,primary_key = True)


class User():
    __tablename__ = 'users'

    id = db.column(db.Integer,primary_key = True)
    name = db.Column(db.string(255))
