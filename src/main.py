#!/usr/bin/env python3

from ast import NotEq
import xml.etree.ElementTree as ET

path_file = "./assets/notas.kdenlive"


def read_kdenlive(name_file):
    tree = ET.parse(name_file)
    root = tree.getroot()
    note=""
    for t in root.iter("property"):
        if t.get("name").endswith("documentnotes"):
            return t.text
            
    return None


def parse_note(note_raw):
    print(note_raw)

def main():
    note_raw = read_kdenlive(path_file)
    
    with open("note.html", "+w", encoding="utf-8") as note:
        note.write(note_raw)
    
if __name__ == "__main__":
    main()
    