class Category:(db.Model)
    __tablename__ = 'categories'

    id = db.column(db.Integer,primary_key = True)


class User(db.Model):
    __tablename__ = 'users'

    id = db.column(db.Integer,primary_key = True)
    name = db.Column(db.string(255))

def __repr__(self):
    return f'User {self.name}'
