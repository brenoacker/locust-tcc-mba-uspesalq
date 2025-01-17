import random
import string
from uuid import uuid4



def generate_random_string(length=8):
    '''Gera uma string aleatória para nomes ou outras informações.'''
    
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_phone_number():
    '''Gera um número de telefone aleatório no formato internacional.'''
    
    number = random.randint(1000000000, 9999999999)
    return number

def generate_random_gender():
    '''Gera um gênero aleatório'''
    
    return random.choice(['male', 'female'])

def generate_random_age(range: list = None):
    '''Gera uma idade aleatória'''
    if range:
        return random.randint(range[0], range[1])
    
    return random.randint(18, 100)

def generate_random_email():
    '''Gera um email aleatório'''
    
    uuid = uuid4()

    return f"{uuid}@example.com"