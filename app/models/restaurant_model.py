from database import db

class Restaurante(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    rating = db.Column(db.Integer, nullable = False)

    def __init__(self, name, address, city, phone, description, rating):
        self.name = name
        self.address = address
        self.city = city
        self.phone = phone
        self.description = description
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Restaurante.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Restaurante.query.get(id)
    
    def update(self, name = None, address = None, city = None, phone = None, descrition = None, rating = None):
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if descrition is not None:
            self.description = descrition
        if rating is not None:
            self.rating = rating
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
