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

### Running tests

```bash
TODO
```

* * *

## License

[MIT](LICENSE)