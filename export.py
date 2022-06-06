import dataclasses
import shutil
import json

with open('Dark PDF/manifest.json') as f:
    data = json.load(f)
print(data)
shutil.make_archive(data["name"], 'zip', "Dark PDF")