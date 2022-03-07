import re
from random import randint


def valida_cpf(num_cpf=None):
    while True:
        if num_cpf is None:
            cpf = str(randint(10000000000, 99999999999))
        else:
            cpf = str(num_cpf)

        cpf = re.sub(r'[^0-9]', '', cpf)

        if len(cpf) < 11:
            return False

        novo_cpf = cpf[:9]
        total = 0
        mult = 10

        for i in range(19):
            if i > 8:
                i -= 9

            total += int(novo_cpf[i]) * mult

            mult -= 1
            if mult < 2:
                mult = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)

        sequencia = novo_cpf == novo_cpf[0] * 11  # IF MENOR retorna TRUE ou FALSE
        if cpf == novo_cpf and not sequencia:
            return novo_cpf
        elif num_cpf is not None:
            return False
