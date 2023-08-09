import unittest
from unittest.mock import patch
from src.get_bbox_coordinates import get_bbox_coordinates, generate_bbox

class TestStringMethods(unittest.TestCase):

  def test_generate_bbox_coordinates(self):
    lat = 4.43
    lng = -75.21
    width_deg = 0.15
    height_deg = 0.15
    expected_output = [-75.285, 4.3549999999999995, -75.13499999999999, 4.505]
    output = generate_bbox(lat, lng, width_deg, height_deg)
    self.assertEqual(output, expected_output)


  @patch('src.get_bbox_coordinates.generate_bbox')
  def test_get_bbox_coordinates(self, mocked_generate_bbox):
    mocked_generate_bbox.return_value = [1, 1, 1, 1]
    mocked_csv = ['field_id,lat,lon,dim',
    '1,4.429441533567927,-75.21989302730766,0.09']

    expected_output = [{'field_id': '1', 'first_point': {'lat': 1, 'lon': 1}, 'second_point': {'lat': 1, 'lon': 1}}]
    output = get_bbox_coordinates(mocked_csv)
    self.assertEqual(output, expected_output)


if __name__ == '__main__':
  unittest.main()