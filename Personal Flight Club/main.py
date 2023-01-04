# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from pprint import pprint

ORIGIN_CITY_IATA = "LON"

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

sheet_data = dm.get_destination_data()

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = fs.get_destination_code(city["city"])

dm.destination_data = sheet_data
#dm.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = fs.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        nm.send_sms(
        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    )