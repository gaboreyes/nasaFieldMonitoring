
def save_to_local(image_response, field_id, cwd):
  date = image_response.headers['Date'][5:-4].replace(' ','_').replace(':','')
  filepath = f'{cwd}\images\{field_id}{date}_imagery.png'
  with open(filepath, 'wb') as f:
    f.write(image_response.content)