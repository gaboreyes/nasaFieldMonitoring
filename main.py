import os
import concurrent.futures
from pathlib import Path
from src.fetch_image import fetch_image
from src.get_bbox_coordinates import get_bbox_coordinates
from src.save_to_local import save_to_local
from src.save_to_s3 import save_images_to_s3
from src.clear_from_local import clear_from_local

def create_img_directory():
  cwd = os.getcwd()
  Path(f"{cwd}/images").mkdir(parents=True, exist_ok=True)
  return cwd


def read_csv():
  # Assume that the fields' location is stored in a csv file with the format: field_id, lat, lon, dim (width and height of field in degrees).
  csv_file = open("./dummyLocations.csv", "r")
  return csv_file
  

def main():
  cwd = create_img_directory()
  csv_output = read_csv()

  bbox_array = get_bbox_coordinates(csv_output)
  
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    fetched_images = list(executor.map(fetch_image, bbox_array))

  for i in range(len(fetched_images)):
    save_to_local(fetched_images[0], bbox_array[i]['field_id'], cwd)
  # save_images_to_s3(cwd, bbox_array)
  print('CLEARING FROM LOCAL')
  clear_from_local(cwd)

if __name__ == "__main__":
  main()



# TODO:
# The images shall be stored in a S3 bucket with the following folder structure: `s3://{BUCKET_NAME}/{field_id}/{date}\_imagery.png`



"""
# ----------Satellite field monitoring----------
The objective of this assignment is to create a daily process that uses public NASA imagery from Landsat 8 constellation 
to monitor a list of fields. The imagery is provided by NASA throuhg Earth API (see https://api.nasa.gov)). 
The service requires an API key that can be obtained for free.








## ----------Part 2: Infrastructure----------
Define a possible cloud arquitecture to run this process on a daily basis.

## Notes
- Use concurrency of any kind to retreive and save the images as fast as possible.
- To mock AWS S3 you can use the moto library (https://docs.getmoto.org/). It shall be easy to switch to the real S3 service.
- The process shall run within its own docker container. Configuration shall be provided as enviroment variables to the container 
(date, destination bucket, AWS credentials, API key, etc.)
- If possible, create a new GitHub repository with the solution.
- Document usage in a README file.
- Tests are always welcome!



"""