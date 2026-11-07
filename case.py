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
        self.nome = nome
        self.qtd_total = quantidade
        self.qtd_disp = quantidade  # Inicia o produto com a quantidade total disponível
        
        # Demais quantidades iniciam com 0
        self.qtd_res = 0
        self.qtd_bloq = 0
    
    # Auxiliares 
    def __eq__(self, other):
        if not isinstance(other, Produto):
            return NotImplemented
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)  # Permite que o produto seja usado em conjuntos e dicionários
    
    def __str__(self): # Representação do produto como string
        return f"Nome: {self.nome}, Total: {self.qtd_total}, Disponível: {self.qtd_disp}, Reservado: {self.qtd_res}, Bloqueado: {self.qtd_bloq}"


    # Requisitos
    def reservar_produtos(self, quantidade):
        if not validar_quantidade(quantidade):
            return False
    
        if quantidade <= self.qtd_disp:
            self.qtd_disp -= quantidade
            self.qtd_res += quantidade
        else:
            return False  # Não há quantidade suficiente disponível para reservar
            
    def bloquear_produtos(self, quantidade):
        if not validar_quantidade(quantidade):
            return
        
        if quantidade <= self.qtd_disp:
            self.qtd_disp -= quantidade
            self.qtd_bloq += quantidade
        
    def liberar_produtos(self, quantidade, tipo):
        if not validar_quantidade(quantidade):
            return False
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
        self.produtos.pop(nome_produto, None)
            
    def listar_produtos(self):
        if not self.produtos:
            return False
        else:
            for produto in self.produtos:
                print(produto)
    
    # Delegações para a classe Produto
    def reservar_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.reservar_produtos(quantidade)
        else:
            return False  # Produto não encontrado no estoque

    def bloquear_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.bloquear_produtos(quantidade)
        else:
            return False  # Produto não encontrado no estoque
    
    def liberar_produtos(self, nome_produto, quantidade, tipo):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.liberar_produtos(quantidade, tipo)
        else:
            return False  # Produto não encontrado no estoque
    
    

