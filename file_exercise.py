import pathlib
from pathlib import Path

# file_path = pathlib.Path.home() / "My folder"
# file_path.mkdir(exist_ok=True)
# new_file_path = file_path / "my_file.txt"
# new_file_path.touch(exist_ok=True)
# print("Names - ", new_file_path.name)
# print("Exists? - ", file_path.exists())
# print("Parent -", new_file_path.parent.name)

file = Path.home() / "Folder"
file.mkdir(exist_ok=True)
new_file = file / "file.txt"
new_file.touch(exist_ok=True)
docs = [file / "videos",
        file / "image",
        file / "bible",
        file / "music",
        file / "games"
        ]
# for files in file.iterdir():
#       print(files.parent.name)

# source = file / "videos.mp4"
# destination = file / "videos" / "videos.mp4"
# source.replace(destination)

# source = pathlib.Path(r"C:\Users\ADMIN\Folder\games.csv")
# destination = pathlib.Path(r"C:\Users\ADMIN\Folder\games\games.csv")
# source.replace(destination)
source = [
    file / "file.txt"
          ]
for i in source:
    i.unlink()

# print(new_folder)


print(file)
print(docs)
