import random


def select_and_display_message(valid_file_contents: dict) -> None:
    """Randomly selects one of the valid file contents and prints it to the terminal

    Args:
        valid_file_contents (dict): Dictionary of valid files, where the keys are the
        filenames and the values are a dict of the parsed file contents.
    """
    selection = random.choice(list(valid_file_contents.values()))
    print("*** Message of the day follows ***")
    print(f"{selection.get('name')} says {selection.get('message')}!")
