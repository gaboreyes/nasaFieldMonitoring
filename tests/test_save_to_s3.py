import os
import boto3
import pathlib
import botocore
import unittest
from src.save_to_s3 import save_images_to_s3
from pyfakefs import fake_filesystem_unittest
from moto import mock_s3


class TestRepo(fake_filesystem_unittest.TestCase):

  def setUp(self):
    self.setUpPyfakefs()
    # This setup is needed so pyfakefs can work along moto
    for module in [boto3, botocore]:
      module_dir = pathlib.Path(module.__file__).parent
      self.fs.add_real_directory(module_dir, lazy_read=False)

  @mock_s3
  def test_save_to_s3(self):
    cwd = os.getcwd()
    path = f"{cwd}/images"
    os.makedirs(path)

    bucket_name = "mybucket"
    
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=bucket_name)
    bbox_array = []
    result = save_images_to_s3(cwd, bbox_array)
    self.assertEqual(result, 'Saved 0 images to s3 successfully')
    

if __name__ == '__main__':
  unittest.main()