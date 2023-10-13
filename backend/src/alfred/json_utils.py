import re


def clean_json_string(json):
    json = remove_markdown(json)
    json = remove_quotes(json)
    json = remove_ending_newline(json)
    return json


def remove_markdown(string):
    # regex pattern to capture content inside ```[optional language]...```
    pattern = r"```(?:[a-zA-Z]+)?\s*(.*?)```"
    matches = re.findall(pattern, string, re.DOTALL)

    if matches:
        # assuming you only want the first match
        return matches[0]
    return string


def remove_quotes(string):
    string = string.strip()  # Remove leading and trailing whitespace
    if string.startswith('"') and string.endswith('"'):
        string = string[1:-1]  # Remove surrounding double quotes
    elif string.startswith("'") and string.endswith("'"):
        string = string[1:-1]  # Remove surrounding single quotes
    return string


def remove_ending_newline(string):
    string = string.strip()
    return string.rstrip("\n")
