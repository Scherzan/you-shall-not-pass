import yaml
from yaml import FullLoader
from flask import Flask


def load_config(filename):
    with open(filename, "r") as file:
        config_data = yaml.load(file, Loader=FullLoader)
    return config_data


def start_server(config):
    app = Flask(__name__)

    # Apply server configuration
    app.run(
        host=config["server"]["host"],
        port=config["server"]["port"],
        debug=config["server"]["debug"],
    )


config_data = load_config("totally_safe_file.yaml")
start_server(config_data)
