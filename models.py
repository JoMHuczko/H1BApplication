from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    case_status = db.Column(db.String(50), default="Pending")

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}>"
