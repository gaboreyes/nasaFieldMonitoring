import requests
from os import getenv


def fetch_image(coordinates):
  DATE = getenv('date')
  SENTINEL_HUB_API_KEY = getenv('sentinel_hub_api_key')
  base_url = f'https://services.sentinel-hub.com/ogc/wms/{SENTINEL_HUB_API_KEY}?REQUEST=GetMap&TIME={DATE}&LAYERS=NATURAL-COLOR&WIDTH=320&HEIGHT=320&FORMAT=image/png&CRS=CRS:84'
  x_lat = coordinates['first_point']['lat']
  x_lon = coordinates['first_point']['lon']
  y_lat = coordinates['second_point']['lat']
  y_lon = coordinates['second_point']['lon']
  bbox_query_string = f"&BBOX={x_lat},{x_lon},{y_lat},{y_lon}"
  image_response = requests.get(base_url + bbox_query_string)
  return (image_response)
