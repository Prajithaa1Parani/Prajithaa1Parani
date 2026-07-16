import os
import re

README_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")

FIELDS = {
    "REPOS": os.environ["REPOS"],
    "COMMITS": f'{int(os.environ["COMMITS"]):,}',
    "STARS": os.environ["STARS"],
    "FOLLOWERS": os.environ["FOLLOWERS"],
    "LOC": f'{int(os.environ["LOC"]):,}',
    "UPTIME": os.environ["UPTIME"],
}

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

for key, value in FIELDS.items():
    pattern = re.compile(rf"(<!--STAT:{key}-->)(.*?)(<!--/STAT:{key}-->)", re.DOTALL)
    content = pattern.sub(lambda m, v=value: f"{m.group(1)}{v}{m.group(3)}", content)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)
