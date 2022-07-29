#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from os import path
from sys import argv, exit


try:
    from bs4 import BeautifulSoup as bs
except:
    try:
        from pip._internal import main as pip
        pip(['install', '--user', 'bs4'])
        from bs4 import BeautifulSoup as bs
    except:
        from pip._internal import main as pip
        pip(['install', 'bs4'])
        from bs4 import BeautifulSoup as bs


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


def get_name_default(name_kdenlive: str):
    name = name_kdenlive.split(path.sep)[-1]
    name = name.replace(".kdenlive", "")
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
        line = line.split(":")[1:-1]
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
        line = p.text.strip()
        # print(line)
        if len(line) and line[0].isdigit():
            line = clear_line(line)

        description += line + "\n"

    return description.strip()


def get_note(path_file: str, save=False):
    """Main function to export

    Args:
        path_file (str): Path file kdenlive

    Returns:
        str: All content formatted
    """

    note_raw = get_note_kdenlive(path_file)
    description = get_times(note_raw)

    if save:
        save_description(description, get_name_default(path_file))

    return description


def test():
    """Function to the the module
    """
    path_file = "./assets/notas.kdenlive"
    note_raw = get_note_kdenlive(path_file)
    # save_note(note_raw)
    description = get_times(note_raw)

    save_description(description, get_name_default(path_file))


def cli():

    HELP = """
    Script to get note from file kdenlive a youtube time format
    
    HOW TO USE:
    
        getnotex file.kdenlive 
    """

    if len(argv) < 2 or len(argv) > 2:
        print(HELP)
        exit(1)

    file_name = argv[1]
    
    if file_name == "--help":
        print(HELP)
        exit(0)
    
    try:
        get_note(file_name, save=True)
    except Exception as e:
        print(e)
        print(HELP)
        exit(1)
    
    exit(0)
    

if __name__ == "__main__":
    # test()
    cli()
    
## por el momento solo pasa el nombre el archivo y generara el archivo .description, aun no tiene mas características
