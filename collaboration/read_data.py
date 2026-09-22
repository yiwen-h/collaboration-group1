import os


def list_files(filepath: str) -> list:
    """Lists files in a folder, if the filename starts with `file_` and ends with `.txt`.

    Args:
        filepath (str): Folder containing the files

    Returns:
        list: List of the filepaths
    """
    files = [
        os.path.join(filepath, file)
        for file in os.listdir(filepath)
        if file.startswith("file_") and file.endswith(".txt")
    ]
    return files


def read_files(list_of_files: list) -> dict:
    file_contents_dict = {}
    for file in list_of_files:
        with open(file, encoding="utf-8") as f:
            file_contents_dict[file] = f.readlines()
    return file_contents_dict
