from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    capacity = db.Column(db.Integer)

    events = db.relationship("Event", backref="venue")
    seats = db.relationship("Seat", backref="venue")


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_time = db.Column(db.DateTime)
    genre = db.Column(db.String(50))

    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"))
    tickets = db.relationship("Ticket", backref="event")


class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.Integer)
    number = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)

    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime)
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(50))

    tickets = db.relationship("Ticket", backref="order")
    delivery = db.relationship("Delivery", backref="order", uselist=False)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    type = db.Column(db.String(50))

    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    seat_id = db.Column(db.Integer, db.ForeignKey("seat.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(50))
    destination = db.Column(db.String(255))
    tracking_status = db.Column(db.String(50))

    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))