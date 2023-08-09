from os import getenv

def save_to_local(image_response, field_id, cwd):
  DATE = getenv('date')
  date = DATE.replace('-','_')
  filepath = f'{cwd}/images/{field_id}{date}_imagery.png'
  with open(filepath, 'wb') as f:
    f.write(image_response.content)