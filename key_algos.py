from random import *
from typing import Final, List

alphabet: List[str] = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                       'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

#eng_alphabet: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generate_key() -> str:
    global alphabet
    length: Final = 33
    ans_key: str = ""

    while len(ans_key) != length:
        elem = alphabet[randint(0, 32)]
        if elem not in ans_key:
            ans_key += elem
    return ans_key


def cypher_key(key: str) -> str:
    global alphabet
    new_key: str = ""
    length: Final = len(key)

    for elem in key:
        new_index_letter: int = (alphabet.index(elem) + length % 33) % 33
        new_key += alphabet[new_index_letter]
    return new_key


def de_cypher_key(cypher_key: str) -> str:
    global alphabet
    ans_key: str = ""
    length: Final = len(cypher_key)

    for elem in cypher_key:
        new_index_letter: int = alphabet.index(elem) - length % 33
        if new_index_letter < 0:
            new_index_letter = 32 + new_index_letter + 1
        ans_key += alphabet[new_index_letter]
    return ans_key


def sum_of_key(key: str) -> int:
    ans: int = 0
    for elem in key:
        ans += ord(elem)
    return ans
