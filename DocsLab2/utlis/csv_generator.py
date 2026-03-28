import csv, random

def generate(path, n=1000):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "venue_name","venue_address","capacity",
            "event_title","date","genre",
            "seat_row","seat_number",
            "price","type",
            "delivery_method","destination"
        ])

        for i in range(n):
            writer.writerow([
                f"Venue{i}",
                "Lviv",
                random.randint(100, 5000),
                f"Event{i}",
                "2025-06-01",
                "Rock",
                random.randint(1, 20),
                random.randint(1, 100),
                random.randint(50, 200),
                "VIP",
                "Courier",
                "Lviv"
            ])

if __name__ == "__main__":
    generate("../data/data.csv", 1000)