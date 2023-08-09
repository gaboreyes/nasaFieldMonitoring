import os
import concurrent.futures
import sys
from pathlib import Path
from src.fetch_image import fetch_image
from src.get_bbox_coordinates import get_bbox_coordinates
from src.save_to_local import save_to_local
from src.save_to_s3 import save_images_to_s3
from src.clear_from_local import clear_from_local
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def create_img_directory():
  cwd = os.getcwd()
  Path(f"{cwd}/images").mkdir(parents=True, exist_ok=True)
  return cwd


def read_csv():
  csv_file = open(getenv('csv_file_path'), "r")
  return csv_file
  

def main():
  try:
    cwd = create_img_directory()
    csv_output = read_csv()
    bbox_array = get_bbox_coordinates(csv_output)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
      fetched_images = list(executor.map(fetch_image, bbox_array))

    for i in range(len(fetched_images)):
      save_to_local(fetched_images[i], bbox_array[i]['field_id'], cwd)

    s3_upload_result = save_images_to_s3(cwd, bbox_array)
    print(s3_upload_result)
  except:
    e = sys.exc_info()[0]
    print(e)

  clear_from_local(cwd)
    

if __name__ == "__main__":
  main()


"""
## Notes
- To mock AWS S3 you can use the moto library (https://docs.getmoto.org/). It shall be easy to switch to the real S3 service.
- The process shall run within its own docker container. Configuration shall be provided as enviroment variables to the container 
(date, destination bucket, AWS credentials, API key, etc.)
- Document usage in a README file.
- Tests are always welcome!
"""