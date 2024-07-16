class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(nro_patas=kwargs["nro_patas"])

    #def __str__(self):
        #return 'ave 42'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

    #def __str__(self):
        #return self.__class__.__name__


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass

# Mixin adiciona algo que tem que fazer, porém não está acoplado,
# logo não tem questão de ordem -> conceito forte no Django
class FalarMixin:
    def falar(self):
        return "Oi estou falando!!"


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # forma de leitura do codigo para poder exibir
        #print(Ornitorrinco.__mro__)
        #print(Ornitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo,
                         cor_bico=cor_bico,
                         nro_patas=nro_patas)


gato = Gato(cor_pelo="Preto", nro_patas=4)
print(gato)

ornitorrinco = Ornitorrinco(cor_pelo="marrom",
                            cor_bico="Preto",
                            nro_patas=4)
print(ornitorrinco)
print(ornitorrinco.falar())
