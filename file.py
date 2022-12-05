import pathlib
from pathlib import Path

fake_path = pathlib.Path("c:/Cohort14/private.img")
cwd_path = Path.cwd() / "Yinka" / "numbers" / "green.csv"
print(cwd_path)
# print(cwd_path)
# print("Parent -", cwd_path.parent)
# print("Parent -", path.parent)
# print(list(path.parents))
# print("Anchor - ", path.anchor)
# print("Names - ", path.name)
# print("suffix - ", path.suffix)
# print("stem - ", path.stem)
cwd_path.mkdir(exist_ok=True)

new_file_path = cwd_path / "private.txt"
new_file_path.touch()
print(fake_path.exists())
print("Exists? - ", cwd_path.exists())
print("isDir - ", cwd_path.is_file())