# Using users.json file:
# open it and decode the Python object inside it
# filter users with "email" key and encode the resulting object in a JSON
# string; print the string to the console
# filter users with ages between 20 and 40 and encode the resulting object in a
# JSON file, using indent and sort_keys parameters.

import json
from pathlib import Path

# resolve will make the path absolute; it is needed to fetch the parent path
current_path = Path().resolve()
json_file = current_path.parent / "docs" / "users.json"

with json_file.open() as f:
    users = json.load(f)

users_with_email = [user for user in users if "email" in user]
json_string = json.dumps(users_with_email)
print(json_string)

users_between_20_40 = [user for user in users if 20 < user.get("age", 0) < 40]
new_json_path = current_path / "users_between_20_40.json"

with new_json_path.open("w") as f:
    json.dump(users_between_20_40, f, indent=4, sort_keys=True)
