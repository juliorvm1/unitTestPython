""" ESte es el Docstring del módulo docString.py sedebe colocar en la primera línea del
    módulo
"""


#Docstring
#__doc__

class user:
    """Permite representar un usuario este es un Docstring de una clase"""
    def __init__(self,username,password)->None:
        """Permite instanciar un objeto de tipo user en la primera liena de la definicion del metodo constructor 

        Args:
            username (str): el username del usuario
            password (str): el passwor del usuario
        """

def palindromo(sentence: str)->bool:
    """Permite conocer si un string es palindromo.
    
    Args:
        sentence:String

    Returns: 
        bool: True o False

    Examples:

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False

    >>> sentence='oso'
    >>> palindromo(sentence)
    True
    """
    sentence=sentence.lower().replace(' ','')
    return sentence==sentence[::-1]
