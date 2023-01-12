from pathlib import Path

folder1 = Path.home() / "my_folder"
folder1.mkdir(exist_ok=True)
docs = [
    folder1 / "file1.txt",
    folder1 / "file2.txt",
    folder1 / "image1.png",
    ]
for file in docs:
    file.touch(exist_ok=True)
folder2 = Path.home()/"my_folder" / "image"
folder2.mkdir(exist_ok=True)
source = Path(r"C:\Users\ADMIN\my_folder\image1.png")
print(source.exists())
destination = Path(r"C:\Users\ADMIN\my_folder\image\image1.png")
print(destination.exists())
source.replace(destination)
file_delete = Path(r"C:\Users\ADMIN\my_folder\file2.txt")
file_delete.unlink()
