from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from custom_module import generate_time_travel_message

time_now = dt.now()
destinations = ["Japan", "Mexico", "England", "Italy"]

print(time_now)

travel_year = randint(2025, 2060)
current_year = dt.now().year
base_cost = Decimal('1000.00')
cost_multiplier = current_year - travel_year 

final_cost = base_cost + cost_multiplier
destination = choice(destinations)

print(generate_time_travel_message(travel_year, destination, final_cost))

