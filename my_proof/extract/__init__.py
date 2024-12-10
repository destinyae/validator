import zipfile
import json
import logging


def validate_json_structure(json_obj: list) -> bool:
    """
    Validates that the provided JSON object is a list of objects each containing
    'input' and 'output' as strings, and 'context' as a dict with 'content' and 'title' as strings.

    :param json_obj: The JSON object to validate
    :raises ValueError: If the JSON object does not conform to the expected structure
    """
    if not isinstance(json_obj, list):
        return False

    for index, item in enumerate(json_obj):
        if not isinstance(item, dict):
            return False

        # Check for required keys
        required_keys = {'input', 'output', 'context'}
        if not required_keys.issubset(item.keys()):
            return False

        # Check types of 'input' and 'output'
        if not isinstance(item['input'], str):
            return False
        if not isinstance(item['output'], str):
            return False
        if not isinstance(item['task'], str):
            return False

        # Check 'context'
        context = item['context']
        if not isinstance(context, dict):
            return False

        if 'content' not in context or 'title' not in context:
            return False

        if not isinstance(context['content'], str):
            return False
        if not isinstance(context['title'], str):
            return False

    return True

def extract_data(zip_file_path: str):
    """
    Extracts the data from the zip file
    :param zip_file_path: Path to the zip file
    :return: Object containing a quality score and whether the file is valid

    Throws
        If extract contraints are not respected
    """
    required_files = ["examples.data"]
    # Load data from zip file and validate that it contains the required files
    try:
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            file_names = zip_ref.namelist()
            if not all(file in file_names for file in required_files):
                raise ValueError(
                    f"Zip file does not contain all required files: {required_files}"
                )
            # Start of Selection

            with zip_ref.open("examples.data", "r") as file:
                data = json.load(file)
                return data
    except Exception as e:
        print(e)
        raise e