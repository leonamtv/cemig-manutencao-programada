from datetime import datetime
from src.core.pipeline import run
from src.core.arg_parser import parse_args
from src.env.environment import NO_CITY_MESSAGE

arguments = parse_args()
city_name = None
date_to_search = None
if arguments.city:
    city_name = arguments.city

if arguments.date:
    date_to_search = datetime.strptime(arguments.date, '%d/%m/%Y')

if city_name:
    run(city_name, date_to_search)
else:
    print(NO_CITY_MESSAGE)
