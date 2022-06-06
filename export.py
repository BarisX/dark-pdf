import dataclasses
import shutil
import json

with open('Dark PDF/manifest.json') as f:
    data = json.load(f)
shutil.make_archive(data["name"], 'zip', "Dark PDF")