from jsjobs_app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dev = db.Column(db.String(64), index=True, unique=False)
    city_business = db.Column(db.String(100), index=True, unique=False)
    salary = db.Column(db.String(120), index=True, unique=False)
    hashtags = db.Column(db.String(512), index=True, unique=False)
    description = db.Column(db.String(2000), index=True, unique=False)
    contacts = db.Column(db.String(128), index=True, unique=False)

    def __repr__(self):
        return '<Company {}>'.format(self.dev)
