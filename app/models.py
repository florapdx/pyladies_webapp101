from app import db

# Todo Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(32), nullable=False)
    lists = db.relationship('List', backref='user', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(120), unique=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    tasks = db.relationship('Task', backref='list', lazy='dynamic')

    def __init__(self, name, owner, tasks):
        self.name = name
        self.owner = owner
        self.tasks = tasks

    def __repr__(self):
        return '<List %r>' % self.name

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list = db.Column(db.Integer, db.ForeignKey('list.id'))
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
    completed_at = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, created_at, completed_at, completed):
        self.title = title
        self.description = description
        self.created_at = created_at
        self.completed_at = completed_at
        self.completed = completed

    def __repr__(self):
        return '<Task %r>' % self.title
