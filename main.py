"""
Main file
"""

class Custos:
    def __init__(self):
        self.custos: list = list()

    def adiciona_custo_fixo(self, nome: str, valor: float) -> None:
        print(f"Adicionando custo fixo de {nome}...")
        novo_custo: dict = {nome: valor}
        self.custos.append(novo_custo)
        print(f"Custo Adicionado.")

        return

custos_totais: Custos = Custos()
tipo_acao: int = int(input("Digite 1 para adicionar custo."))

if tipo_acao == 1:
    nome_custo: str = input("Digite o nome do custo: ")

    tipo_custo: int = int(input("Digite 1 para custo fixo ou 2 para Custo variável: "))

    if tipo_custo == 1:
        valor: float = float(input("Digite o valor: "))
        custos_totais.adiciona_custo_fixo(nome=nome_custo, valor=valor)


print(custos_totais.custos)