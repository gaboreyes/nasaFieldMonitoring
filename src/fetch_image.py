import requests
import datetime

def fetch_image(coordinates):
  base_url = 'https://services.sentinel-hub.com/ogc/wms/41bb8f68-da0b-41b2-a0ea-eea615543ddd?REQUEST=GetMap&LAYERS=NATURAL-COLOR&WIDTH=320&HEIGHT=320&FORMAT=image/png&CRS=CRS:84'
  x_lat = coordinates['first_point']['lat']
  x_lon = coordinates['first_point']['lon']
  y_lat = coordinates['second_point']['lat']
  y_lon = coordinates['second_point']['lon']
  bbox_query_string = f"&BBOX={x_lat},{x_lon},{y_lat},{y_lon}"
  image_response = requests.get(base_url + bbox_query_string)
  return (image_response)
