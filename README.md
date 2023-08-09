# Python and Sentinel Hub OGC API

AWS S3 storage script that uses [Sentinel Hub OGC API](https://docs.sentinel-hub.com/api/latest/api/ogc/examples/)

## Installation

We recomed setting up a [python venv](https://docs.python.org/3/library/venv.html) for installing dependencies for this project.

```bash
pip install -r /path/to/requirements.txt
```

You have a ```.env.copy``` file, this is a template that you can copy and rename to ```.env```.
In here you will have to add values for the environment variables.

You will need a [Sentinel Hub](https://apps.sentinel-hub.com/dashboard/#/) account in order to use the OGC API. Once registered in the "Configuration Utility" tab you will find your api key. 

## Scripts

### Running the script

```bash
python main.py
```
Note that inside the project at root level you have ```dummyLocations.csv``` this is the default file used for getting the coordinates for the images, if you want to use a different set, add your file to the project at root level and update the value for ```csv_file_path``` inside the env file accordingly. Please make sure your file follows the format of the ```dummyLocations.csv```
### Running tests

```bash
python -m unittest discover
```

* * *

## License

[MIT](LICENSE)