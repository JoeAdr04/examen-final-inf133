from database  import db
from models.user_model import User
from models.restaurant_model import Restaurante
class Reserve(db.Model):

    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True, nullable =False)
    user_id = db.Column(db.Foreigkey(User.id), nullable = False, primary_key = True)
    restaurant_id = db.Column(db.Foreignkey(Restaurante.id), nullable = False)
    reservation_date = db.Column(db.Datetime, nullable = False)
    num_guest = db.Column(db.Integer, nullable = False)
    special_request = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(100), nullable = False)

    def __init__(self, user_id, restaurant_id, reservation_date, num_gues, special_request, status):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.reservation_date = reservation_date
        self.num_guest = num_gues
        self.special_request = special_request
        self.status = status
    
    @staticmethod
    def get_all():
        return Reserve.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Reserve.query.get(id)
    
    def update(self, reservation_date=None, num_guest=None, special_request = None, status=None):
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guest is not None:
            self.num_guest = num_guest
        if special_request is not None:
            self.special_request = special_request
        if status is not None:
            self.status = status
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    
