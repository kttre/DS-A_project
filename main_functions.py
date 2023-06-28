from random import *
from key_algos import *
from division_hashing import *
from multi_hashing import *
from addition_hashing import *

# 1 - умножение, 2 - деление, 3 - сложение
# ### - умножение, %%% - деление, *** - сложение
def choose_algo() -> str:
    current_algo: int = randint(1, 3)
    str_answer: str = ''

    if current_algo == 1:
        str_answer = "###"
    elif current_algo == 2:
        str_answer = "%%%"
    elif current_algo == 3:
        str_answer = "***"
    return str_answer


def make_hash(user_text: str) -> str:
    current_algo = choose_algo()
    hash_text = ''
    key = generate_key()
    if current_algo == '###':
        hash_text = multi_hash(key, user_text)
    elif current_algo == '%%%':
        hash_text = division_hash(key, user_text)
    elif current_algo == '***':
        hash_text = addition_hash(key, user_text)
    final_hash = current_algo + '@' + cypher_key(key) + '@' + hash_text
    return final_hash


def make_dehash(user_hash: str) -> str:
    current_algo, cypher_key, hash_text = map(str, user_hash.split('@'))
    key = de_cypher_key(cypher_key)
    old_text = ''
    if current_algo == '###':
        old_text = multi_dehash(key, hash_text)
    elif current_algo == '%%%':
        old_text = division_dehash(key, hash_text)
    elif current_algo == '***':
        old_text = addition_dehash(key, hash_text)
    return old_text

'''
text = 'Привет, мир! Я тут.'

hash = make_hash(text)
print(hash)
print(make_dehash(hash))

'''




