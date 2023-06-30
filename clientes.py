class Cliente:
    def __init__(self, nome, idade, cpf, email):
        self.Nome = nome,
        self.Idade = idade,
        self.Cpf = cpf,
        self.Email = email
    @property
    def nome(self):
        print("Nome do(a) Cliente: {}".format(self.Nome))
        return self.Nome
    @property
    def idade(self):
        print("Idade do(a) Cliente: {}".format(self.Idade))
        return self.Idade
    @idade.setter
    def idade(self, nova_idade):
        self.Idade = nova_idade
    @property
    def cpf(self):
        print("Nome do Cliente: {}".format(self.Cpf))
        return self.Cpf
    @property
    def email(self):
        print("Email do Cliente: {}".format(self.Email))
        return self.Email





cliente_Anicele = Cliente('Anicele', 21, "06864571530", 'anicelelopes41@gmail.com')


cliente_Anicele.idade

cliente_Anicele.idade = 29

cliente_Anicele.idade
