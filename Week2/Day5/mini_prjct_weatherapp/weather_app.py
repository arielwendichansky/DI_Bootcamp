from pyowm.owm import OWM
owm = OWM('a2fcad8620f27ba7f2093802b85d2f6d')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Jerusalem,IL')

weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
weather.detailed_status  # detailed version of status (eg. 'light rain')

print(f"The weather in Jerusalem now is {weather.status} and to be more accurate {weather.detailed_status}\n")

wind_dict_in_meters_per_sec = observation.weather.wind()   # Default unit: 'meters_sec'
wind_dict_in_meters_per_sec['speed']
wind_dict_in_meters_per_sec['deg']
# wind_dict_in_meters_per_sec['gust']
wind_dict_in_miles_per_h = mgr.weather_at_place('Jerusalem,IL').weather.wind(unit='miles_hour')
wind_dict_in_knots = mgr.weather_at_place('Jerusalem,IL').weather.wind(unit='knots')
wind_dict_in_beaufort = mgr.weather_at_place('Jerusalem,IL').weather.wind(unit='beaufort')
print(f"Regarding the wing, the speed in knots is {wind_dict_in_knots}\n")


sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
sunrise_iso = weather.sunrise_time(timeformat='iso')
sunrise_date = weather.sunrise_time(timeformat='date')
sunrset_unix = weather.sunset_time()  # default unit: 'unix'
sunrset_iso = weather.sunset_time(timeformat='iso')
sunrset_date = weather.sunset_time(timeformat='date')
print(f"The sunrise in Jerusalem is at {sunrise_iso} and sunset will be at {sunrset_iso}\n")

# city_selection = input("From which city you want to know the current weather?").title()
# reg = owm.city_id_registry()
# list_of_tuples = london = reg.ids_for(city_selection, matching='exact')
# print(list_of_tuples)

from pyowm import OWM
from pyowm.utils import timestamps

# get an air pollution manager object
mgr = owm.airpollution_manager()
coi = mgr.coindex_around_coords(51.507351, -0.127758)
print(f"The pollution in the air at this time in Jerusalem is {coi}")
