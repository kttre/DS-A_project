from typing import List
from key_algos import *


def division_hash(key: str, text: str) -> str:
    new_str: str = ''
    sum_key = sum_of_key(key)
    for elem in text:
        new_elem = ord(elem)
        has_elem = str(new_elem % sum_key)
        count_elem = str(new_elem // sum_key)
        new_str += has_elem + '/' + count_elem + '_'
    return new_str[:-1]


def division_dehash(key: str, text: str) -> str:
    word_list: List = list(text.split('_'))
    old_text: str = ''
    sum_key = sum_of_key(key)
    for elem in word_list:
        hash_elem, count = map(int, elem.split('/'))
        old_elem = count * sum_key + hash_elem
        old_text += chr(old_elem)
    return old_text
