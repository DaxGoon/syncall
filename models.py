from app import db


class Records(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    signed_message = db.Column(db.String)

    def __init__(self, message, signed_message):
        self.message = message
        self.signed_message = signed_message

    def __repr__(self):
        return "Records for %r" % self.message
