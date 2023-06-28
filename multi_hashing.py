from typing import List, Final
from key_algos import *


def multi_hash(key: str, text: str) -> str:
    new_str: str = ''
    sum_key = sum_of_key(key)
    c: Final = 0.1
    for elem in text:
        new_elem = ord(elem)
        hash_elem = int((sum_key * (new_elem * c)))
        new_str += str(hash_elem) + '_'
    return new_str[:-1]


def multi_dehash(key: str, text: str) -> str:
    word_list: List = list(text.split('_'))
    old_text: str = ''
    sum_key = sum_of_key(key)
    c: Final = 0.1
    for elem in word_list:
        hash_elem = int(elem)
        old_elem = int(round(hash_elem / (sum_key * c), 1))
        old_text += chr(old_elem)
    return old_text
