from pathlib import Path


def file_maker1():
    my_list = []
    new_file_path = Path.cwd() / "Olayinka_folder"
    new_file_path.mkdir(exist_ok=True)
    new_file = new_file_path / "Private.txt"
    new_file.touch()
    new_file_path.write_text("Hello world")
    new_file_path.read_text()
