import yaml
from yaml import FullLoader

yaml.load(open("totally_safe_file.yaml",encoding="utf-8"), Loader=FullLoader)
