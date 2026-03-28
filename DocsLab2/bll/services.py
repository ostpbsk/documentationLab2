from models.models import *
from datetime import datetime
from dal.interfaces import IRepository, ICSVReader

class ImportService:

    def __init__(self, repo: IRepository, csv_reader: ICSVReader):
        self.repo = repo
        self.csv_reader = csv_reader

    def import_data(self, path):
        rows = self.csv_reader.read(path)

        for row in rows:
            venue = Venue(
                name=row['venue_name'],
                address=row['venue_address'],
                capacity=int(row['capacity'])
            )
            self.repo.add(venue)

            event = Event(
                title=row['event_title'],
                date_time=datetime.strptime(row['date'], "%Y-%m-%d"),
                genre=row['genre'],
                venue_id=venue.id
            )
            self.repo.add(event)

            seat = Seat(
                row=int(row['seat_row']),
                number=int(row['seat_number']),
                venue_id=venue.id
            )
            self.repo.add(seat)

            order = Order(
                order_date=datetime.now(),
                total_amount=float(row['price']),
                status="NEW"
            )
            self.repo.add(order)

            ticket = Ticket(
                price=float(row['price']),
                type=row['type'],
                event_id=event.id,
                seat_id=seat.id,
                order_id=order.id
            )
            self.repo.add(ticket)

            delivery = Delivery(
                method=row['delivery_method'],
                destination=row['destination'],
                tracking_status="CREATED",
                order_id=order.id
            )
            self.repo.add(delivery)