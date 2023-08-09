def generate_bbox(lat, lng, width_deg, height_deg):
  delta_lat = height_deg / 2
  delta_lng = width_deg / 2
  min_lat = lat - delta_lat
  max_lat = lat + delta_lat
  min_lng = lng - delta_lng
  max_lng = lng + delta_lng
  return [min_lng, min_lat, max_lng, max_lat]


def get_bbox_coordinates(csv_output):
  bbox_array = []
  i = False

  for line in csv_output:
    first_point = {}
    second_point = {}

    if(i == False ):
      i = True
      continue
    splits = line.split(',')
    # Generates a set of coordinates in bbox format
    bbox = generate_bbox(float(splits[1]), float(splits[2]), float(splits[3].replace('\n', '')), float(splits[3].replace('\n', '')))
    field_id = splits[0]
    first_point['lat'] = bbox[0]
    first_point['lon'] = bbox[1]
    second_point['lat'] = bbox[2]
    second_point['lon'] = bbox[3]
    bbox_array.append({'field_id': field_id, 'first_point': first_point, 'second_point': second_point})
  return bbox_array