import boto3
from os import listdir, getenv
from os.path import isfile, join
from moto import mock_s3


def save_images_to_s3(cwd, bbox_array):
  ACCESS_KEY_ID = getenv('aws_access_key_id')
  SECRET_ACCESS_KEY = getenv('aws_secret_access_key')
  BUCKET_NAME = getenv('bucket_name')
  s3 = boto3.client('s3', 
                    aws_access_key_id=ACCESS_KEY_ID, 
                    aws_secret_access_key=SECRET_ACCESS_KEY, 
                    region_name='us-east-1'
                    )
  
  path = f"{cwd}/images"
  files_array = [f for f in listdir(path) if isfile(join(path, f))]

  for i in range(len(files_array)):
    field_id = bbox_array[i]['field_id']
    with open(f"{path}/{files_array[i]}", "rb") as image:
      bytes = bytearray(image.read())
      s3.put_object(Bucket=BUCKET_NAME, Key=f"{field_id}/{files_array[i][1:]}", Body=bytes)
  print('Saved to s3 successfully')
      