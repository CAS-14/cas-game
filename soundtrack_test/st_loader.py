import os

GAME_DIR = "."
ST_TXT = os.path.join(GAME_DIR, "soundtrack.txt")
ST_DIR = os.path.join(GAME_DIR, "soundtrack")

with open(ST_TXT, "r") as f:
    content = f.read()

soundtrack = [None,]
for line in content.splitlines():
    soundtrack.append(line)

errors = []
for filename in soundtrack:
    songpath = os.path.join(ST_DIR, filename)
    if not os.path.isfile(filename):
        errors.append(filename)

if errors:
    err_msg = f"Failed to load {len(errors)} sound files. Please check your soundtrack.txt!"