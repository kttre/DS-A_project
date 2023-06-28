from typing import List, Final
from key_algos import *

add_symbols = [' ', '.', ',', '!', '?', '/', '+', '-', '#', '"', "'"]


def check_index(index: int) -> str:
    if index > 9:
        return str(index)
    else:
        new_index = '0' + str(index)
        return new_index


def addition_hash(key: str, text: str) -> str:
    global add_symbols
    new_text: str = ''
    key_list: List = sorted((list(key)), reverse=True)
    key_list = key_list + add_symbols
    for elem in text:
        if elem not in key_list:
            new_text += check_index(key_list.index(elem.lower()))
        else:
            new_text += check_index(key_list.index(elem))
    return new_text


def addition_dehash(key: str, text: str) -> str:
    global add_symbols
    old_text: str = ''
    key_list: List = sorted((list(key)), reverse=True)
    key_list = key_list + add_symbols
    for index in range(0, len(text), 2):
        old_text += key_list[int(text[index:index + 2])]
    return old_text
