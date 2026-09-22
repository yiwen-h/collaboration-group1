"""Orchestrates functions into one pipeline which randomly prints out a valid name and message from the files in the data folder"""

from collaboration.display_data import select_and_display_message
from collaboration.read_data import list_files, read_files
from collaboration.validate_data import validate_files


def pipeline():
    """Main pipeline function"""
    list_of_files = list_files("data")
    file_contents_dict = read_files(list_of_files)
    valid_file_contents = validate_files(file_contents_dict)
    select_and_display_message(valid_file_contents)
