def validate_name(name_string: str) -> bool:
    """Checks if there is a valid name in the text file

    Args:
        name_string (str): String in the text file containing the name

    Returns:
        bool: True if there is a valid name provided, False if not
    """
    name = name_string.removeprefix("Name:").strip()
    return len(name) > 0


def validate_message(message_string: str) -> bool:
    message = message_string.removeprefix("Message:").strip()
    return len(message) > 0


def validate_files(file_contents_dict: dict) -> dict:
    valid_file_contents = {}
    for filename, file_contents in file_contents_dict.items():
        valid = validate_name(file_contents[0]) and validate_message(file_contents[1])
        if valid:
            valid_file_contents[filename] = {
                "name": file_contents[0].removeprefix("Name:").strip(),
                "message": file_contents[1].removeprefix("Message:").strip(),
            }
        else:
            print(f"{filename} not valid")
    return valid_file_contents
