from pprint import pprint
import os
import json
from typing import Dict

# [TEST DATA]
backup_folders = "./Backup_folder"
backup_file = "./file.txt"

# Состояния папки или файла
class STATES:
    NOTFOUND = 0    # Не найден
    NOTMODIFED = 1  # Найден, но не изменён
    MODIFED = 2     # Найден, но изменён

# Исходный датасет
DATA = {
    "BACKUP_DIRECTORY": "./Backup_folder",
    "FOLDERS": {},
    "FILES": {
        backup_file: 0
    }
}


def loadJSON(path="./data.json"):
    """
    Подружает JSON

    В случае ошибки создаёт новый и записывает туда исходный датасет DATA
    """
    data = DATA
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data.update(json.load(f, parse_float=float, parse_int=int))
    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    return data


def getFileState(file: str, old_mtime: float):
    """
    Возвращает состояние файла

    Все состояния указаны в STATES
    """
    try:
        if os.path.getmtime(file) != old_mtime:
            return STATES.MODIFED
        return STATES.NOTMODIFED
    except FileNotFoundError:
        return STATES.MODIFED


def START_CHECK(data: dict):
    for file, old_mtime in data["FILES"].items():
        state = getFileState(file, old_mtime)
        if state == STATES.NOTFOUND:
            pass
        elif state == STATES.NOTMODIFED:
            pass
        elif state == STATES.MODIFED:
            print(1)
            pass
    pass

os.path.getmtime(filename=backup_file)
pprint(os.path.getmtime(filename=backup_file))


if __name__ == "__main__":
    data = loadJSON()
    START_CHECK(data)