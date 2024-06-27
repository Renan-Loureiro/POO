import pessoa
import contas

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checar_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checar_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}{attrs}'
    

if __name__ == '__main__':
    #cc = conta corrente
    #cp = conta poupanca
    c1 = pessoa.Cliente('Renan', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoa.Cliente('Janaina', 28)
    cp1 = contas.ContaPoupanca(111, 333, 3)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    print(banco)