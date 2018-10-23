from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    # to_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    subject = db.Column(db.String(255), default = "")
    content = db.Column(db.String(255), default = "")
    created_at = db.Column(db.DateTime(), nullable = False)
    # from_user = db.relationship("User", foreign_keys = [from_user_id])
    # to_user = db.relationship("User", foreign_keys = [to_user_id])
