#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from os import path

path_file = "./assets/notas.kdenlive"


def get_note_kdenlive(name_file):
    """Get the note written in kdenlive file

    Args:
        name_file (path): Path from file kdenlive

    Returns:
        str: Content of note
    """
    tree = ET.parse(name_file)
    root = tree.getroot()

    note = root.findall('*/property[@name="kdenlive:documentnotes"]')[0].text

    return note

def get_name_default(name_kdenlive:str):   
    name = name_kdenlive.split(path.sep)[-1]
    name = name.replace(".kdenlive","")
    return f'{name}.description'
    

def save_note_html(content: str, path_save="assets/"):
    """Function to save the html got from kdenlive file 

    Args:
        content (str): html note raw
        path_save (str, optional): Path to save the file. Defaults to "assets/".
    """
    # @Test

    with open(f'{path_save}/note.html', "+w", encoding="utf-8") as note:
        note.write(content)


def save_description(content: str, file_name="description"):

    with open(file_name, "+w", encoding="utf-8") as file:
        file.write(content)

    return True


def clear_time(line: str):
    """Clear the format default from kdenlive file to youtube format

    Args:
        line (str): Line from note

    Returns:
        str: New line with the format correct to youtube
    """
    line = line.split(",")[0]

    if line.startswith("00:"):
        line = line.split(":")[1:]
        time = ":".join(line)

    return time


def clear_line(line: str):
    new_line = ""
    time = line.strip().split(" ")[0]
    new_time = clear_time(time)

    new_line = line.replace(time, new_time)

    return new_line


def get_times(html: str):
    content = bs(html, "html.parser")
    body = content.body

    list_p = body.find_all('p')

    description = ""

    for p in list_p:
        line = p.text
        if line.strip()[0].isdigit():
            line = clear_line(line)

        description += line + "\n"

    return description.strip()


def main():
    note_raw = get_note_kdenlive(path_file)
    # save_note(note_raw)
    description = get_times(note_raw)
    save_description(description, get_name_default(path_file))


if __name__ == "__main__":
    main()
