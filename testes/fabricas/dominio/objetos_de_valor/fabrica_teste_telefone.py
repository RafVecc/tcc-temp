import random

import factory

from dominio.objetos_de_valor import Telefone


def gerar_numero() -> str:
    formatos = ['(xx)xxxxx-xxxx', '(xx)xxxx-xxxx']
    formato = random.choice(formatos)
    numero = ''
    for char in formato:
        if char == 'x':
            numero += str(random.randint(0, 9))
        else:
            numero += char
    return numero


class FabricaTesteTelefone(factory.Factory):
    class Meta:
        model = Telefone

    valor = gerar_numero()
