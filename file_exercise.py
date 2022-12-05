import pathlib
from pathlib import Path

file_path = pathlib.Path.home() / "My folder"
file_path.mkdir(exist_ok=True)
new_file_path = file_path / "my_file.txt"
new_file_path.touch(exist_ok=True)
print("Names - ", new_file_path.name)
print("Exists? - ", file_path.exists())
print("Parent -", new_file_path.parent.name)