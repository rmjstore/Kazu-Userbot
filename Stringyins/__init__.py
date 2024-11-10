from .strings import get_languages, get_string, language
from bs4 import BeautifulSoup
import yaml
import os

# Memuat file YAML
yaml_path = os.path.join(os.path.dirname(__file__), "string/id.yml")
with open(yaml_path, "r", encoding="utf-8") as file:
    strings = yaml.safe_load(file)

# Fungsi untuk mengambil string berdasarkan kunci
def get_string(key):
    return strings.get(key, "")
