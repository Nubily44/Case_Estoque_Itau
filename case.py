"""

--- Case Itaú: Controle de Estoque
Código: case.py
Documentação: README.md

Code by Lily
Uso de IA: ChatGPT Free (Conversa disponível em: ) + Github Copilot (University Student Pack)
Python 3.12.10 / Windows 11 Pro 26H2

"""

def validar_quantidade(quantidade):
    if not isinstance(quantidade, int) or isinstance(quantidade, bool):
        raise TypeError("Quantidade deve ser um número inteiro.")
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

# CLasse Produto (representa um produto no estoque)
class Produto:
    def __init__(self, nome, quantidade):
        validar_quantidade(quantidade)
        self.nome = nome
        self.qtd_total = quantidade
        self.qtd_disp = quantidade  # Inicia o produto com a quantidade total disponível
        
        # Demais quantidades iniciam com 0
        self.qtd_res = 0
        self.qtd_bloq = 0
    
    # Auxiliares
    def __str__(self):
        return f"-----\nNome: {self.nome}\nTotal: {self.qtd_total}\nDisponível: {self.qtd_disp}\nReservado: {self.qtd_res}\nBloqueado: {self.qtd_bloq}\n-----"


    # Requisitos
    def reservar_produtos(self, quantidade):
        validar_quantidade(quantidade)
    
        if quantidade > self.qtd_disp:
            return False
        
        self.qtd_disp -= quantidade
        self.qtd_res += quantidade
        
        return True
            
    def bloquear_produtos(self, quantidade):
        validar_quantidade(quantidade)
        
        if quantidade > self.qtd_disp:
            return False
        
        self.qtd_disp -= quantidade
        self.qtd_bloq += quantidade
        
        return True
        
    def liberar_produtos(self, quantidade, tipo):
        validar_quantidade(quantidade)

        atributos = {
            "reserva": "qtd_res",
            "bloqueio": "qtd_bloq"
        }

        if tipo not in atributos:
            raise ValueError("Tipo inválido.")

        atributo = atributos[tipo]
        quantidade_atual = getattr(self, atributo)

        if quantidade > quantidade_atual:
            return False

        setattr(self, atributo, quantidade_atual - quantidade)
        self.qtd_disp += quantidade

        return True

# Classe Estoque (guarda todos os produtos)
class Estoque:
    def __init__(self):
        self.produtos = {}  # Usando um dict para maior eficiência em buscas e remoções
    
    # Auxiliares
    def get_produto(self, nome_produto):
        return self.produtos.get(nome_produto)
    
    # Requisitos
    def adicionar_produto(self, produto):
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto
        else:
            existente = self.produtos[produto.nome]
            existente.qtd_total += produto.qtd_total
            existente.qtd_disp += produto.qtd_total

    def remover_produto(self, nome_produto):
        produto = self.get_produto(nome_produto)

        if produto is None:
            return False

        if produto.qtd_res > 0 or produto.qtd_bloq > 0:
            return False

        del self.produtos[nome_produto]
        return True
                
    def listar_produtos(self):
        if not self.produtos:
            return False

        for produto in self.produtos.values():
            print(produto)

        return True
    
    # Delegações para a classe Produto
    def reservar_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)

        if produto is None:
            return False

        return produto.reservar_produtos(quantidade)

    def bloquear_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)
        
        if produto is None:
            return False
        
        return produto.bloquear_produtos(quantidade)
    
    def liberar_produtos(self, nome_produto, quantidade, tipo):
        produto = self.get_produto(nome_produto)
        
        if produto is None:
            return False
        
        return produto.liberar_produtos(quantidade, tipo)
    
    def consultar_produto(self, nome_produto):
        return self.get_produto(nome_produto)

# Teste de funcionalidades
if __name__ == "__main__":

    ############## Adicionar produtos ##############
    estoque_1 = Estoque()

    # Adicionar produto correto
    estoque_1.adicionar_produto(Produto("Produto A", 100))

    if estoque_1.get_produto("Produto A") is not None:
        print("(Pass) Produto correto adicionado com sucesso.")
    else:
        print("(Fail) Falha ao adicionar produto correto.")

    # Adicionar produto com quantidade negativa
    try:
        estoque_1.adicionar_produto(Produto("Produto B", -5))
        print("(Fail) Produto com quantidade negativa adicionado.")
    except ValueError:
        print("(Pass) Quantidade negativa recusada.")

    # Adicionar produto com quantidade zero
    try:
        estoque_1.adicionar_produto(Produto("Produto C", 0))
        print("(Fail) Produto com quantidade 0 adicionado.")
    except ValueError:
        print("(Pass) Quantidade zero recusada.")

    # Produto com quantidade não inteira
    try:
        estoque_1.adicionar_produto(Produto("Produto D", 10.5))
        print("(Fail) Produto com quantidade não inteira adicionado.")
    except TypeError:
        print("(Pass) Quantidade não inteira recusada.")

    # Adicionar produto duplicado
    estoque_1.adicionar_produto(Produto("Produto A", 50))
    produto = estoque_1.consultar_produto("Produto A")

    if produto.qtd_total == 150 and produto.qtd_disp == 150:
        print("(Pass) Quantidade do produto duplicado somada corretamente.")
    else:
        print("(Fail) Falha ao somar quantidade do produto duplicado.")


    ############## Remover produtos ##############
    estoque_2 = Estoque()

    # Remover produto existente sem reservas ou bloqueios
    estoque_2.adicionar_produto(Produto("Produto B", 50))

    if estoque_2.remover_produto("Produto B"):
        print("(Pass) Produto removido com sucesso.")
    else:
        print("(Fail) Falha ao remover produto existente.")

    # Remover produto existente com reservas
    estoque_2.adicionar_produto(Produto("Produto C", 30))
    estoque_2.reservar_produtos("Produto C", 10)

    if estoque_2.remover_produto("Produto C"):
        print("(Fail) Produto removido mesmo com reservas.")
    else:
        print("(Pass) Produto não removido devido às reservas.")

    # Remover produto existente com bloqueios
    estoque_2.adicionar_produto(Produto("Produto D", 20))
    estoque_2.bloquear_produtos("Produto D", 5)

    if estoque_2.remover_produto("Produto D"):
        print("(Fail) Produto removido mesmo com bloqueios.")
    else:
        print("(Pass) Produto não removido devido aos bloqueios.")

    # Remover produto inexistente
    if estoque_2.remover_produto("Produto X"):
        print("(Fail) Produto inexistente removido.")
    else:
        print("(Pass) Produto inexistente não removido.")


    ############## Reservar produtos ##############
    estoque_3 = Estoque()
    estoque_3.adicionar_produto(Produto("Produto A", 100))

    # Reservar produtos com quantidade disponível
    if estoque_3.reservar_produtos("Produto A", 50):
        produto = estoque_3.consultar_produto("Produto A")

        if produto.qtd_disp == 50 and produto.qtd_res == 50:
            print("(Pass) Reserva realizada e quantidades atualizadas.")
        else:
            print("(Fail) Quantidades inconsistentes após reserva.")
    else:
        print("(Fail) Falha ao reservar produtos.")

    # Reservar produtos com quantidade indisponível
    if estoque_3.reservar_produtos("Produto A", 150):
        print("(Fail) Reserva realizada com quantidade indisponível.")
    else:
        print("(Pass) Reserva recusada por quantidade indisponível.")

    # Reservar produtos inexistentes
    if estoque_3.reservar_produtos("Produto X", 10):
        print("(Fail) Produto inexistente reservado.")
    else:
        print("(Pass) Reserva de produto inexistente recusada.")


    ############## Bloquear produtos ##############
    estoque_4 = Estoque()
    estoque_4.adicionar_produto(Produto("Produto A", 100))

    # Bloquear produtos com quantidade disponível
    if estoque_4.bloquear_produtos("Produto A", 50):
        produto = estoque_4.consultar_produto("Produto A")

        if produto.qtd_disp == 50 and produto.qtd_bloq == 50:
            print("(Pass) Bloqueio realizado e quantidades atualizadas.")
        else:
            print("(Fail) Quantidades inconsistentes após bloqueio.")
    else:
        print("(Fail) Falha ao bloquear produtos.")

    # Bloquear produtos com quantidade indisponível
    if estoque_4.bloquear_produtos("Produto A", 150):
        print("(Fail) Bloqueio realizado com quantidade indisponível.")
    else:
        print("(Pass) Bloqueio recusado por quantidade indisponível.")

    # Bloquear produtos inexistentes
    if estoque_4.bloquear_produtos("Produto X", 10):
        print("(Fail) Produto inexistente bloqueado.")
    else:
        print("(Pass) Bloqueio de produto inexistente recusado.")


    ############## Liberar produtos ##############
    estoque_5 = Estoque()
    estoque_5.adicionar_produto(Produto("Produto A", 100))
    estoque_5.reservar_produtos("Produto A", 50)
    estoque_5.bloquear_produtos("Produto A", 30)

    # Liberar produtos da reserva
    if estoque_5.liberar_produtos("Produto A", 20, "reserva"):
        produto = estoque_5.consultar_produto("Produto A")

        if produto.qtd_disp == 40 and produto.qtd_res == 30:
            print("(Pass) Reserva liberada e quantidades atualizadas.")
        else:
            print("(Fail) Quantidades inconsistentes após liberação da reserva.")
    else:
        print("(Fail) Falha ao liberar produtos da reserva.")

    # Liberar produtos do bloqueio
    if estoque_5.liberar_produtos("Produto A", 10, "bloqueio"):
        produto = estoque_5.consultar_produto("Produto A")

        if produto.qtd_disp == 50 and produto.qtd_bloq == 20:
            print("(Pass) Bloqueio liberado e quantidades atualizadas.")
        else:
            print("(Fail) Quantidades inconsistentes após liberação do bloqueio.")
    else:
        print("(Fail) Falha ao liberar produtos do bloqueio.")

    # Liberar produtos da reserva com quantidade indisponível
    if estoque_5.liberar_produtos("Produto A", 100, "reserva"):
        print("(Fail) Liberação realizada com quantidade indisponível.")
    else:
        print("(Pass) Liberação recusada por quantidade insuficiente na reserva.")

    # Liberar produtos do bloqueio com quantidade indisponível
    if estoque_5.liberar_produtos("Produto A", 50, "bloqueio"):
        print("(Fail) Liberação realizada com quantidade indisponível.")
    else:
        print("(Pass) Liberação recusada por quantidade insuficiente no bloqueio.")

    # Liberar produtos com tipo inválido
    try:
        estoque_5.liberar_produtos("Produto A", 10, "tipo_invalido")
        print("(Fail) Liberação realizada com tipo inválido.")
    except ValueError:
        print("(Pass) Liberação recusada por tipo inválido.")

    # Liberar produtos inexistentes
    if estoque_5.liberar_produtos("Produto X", 10, "reserva"):
        print("(Fail) Produto inexistente liberado.")
    else:
        print("(Pass) Liberação de produto inexistente recusada.")


    ############## Consultar produtos ##############
    estoque_6 = Estoque()
    estoque_6.adicionar_produto(Produto("Produto A", 100))

    # Consultar produto existente
    produto = estoque_6.consultar_produto("Produto A")

    if produto is not None:
        print("(Pass) Produto consultado com sucesso.")
    else:
        print("(Fail) Falha ao consultar produto existente.")

    # Consultar produto inexistente
    produto_2 = estoque_6.consultar_produto("Produto X")
    if produto_2 is None:
        print("(Pass) Produto inexistente não encontrado.")
    else:
        print("(Fail) Produto inexistente consultado com sucesso.")