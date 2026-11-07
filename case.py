"""

--- Case Itaú: Controle de Estoque
Código: case.py
Documentação: README.md

Code by Lily
Uso de IA: ChatGPT Free (Conversa disponível em: ) + Github Copilot (University Student Pack)
Python 3.12.10 / Windows 11 Pro 26H2

"""

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
        if isinstance(other, Produto):
            return self.nome == other.nome and self.qtd_total == other.qtd_total
        return False
    
    def __hash__(self):
        return hash(self.id)  # Permite que o produto seja usado em conjuntos e dicionários
    
    def __str__(self): # Representação do produto como string
        return f"ID: {self.id}, Nome: {self.nome}, Total: {self.qtd_total}, Disponível: {self.qtd_disp}, Reservado: {self.qtd_res}, Bloqueado: {self.qtd_bloq}"

    def get_nome(self):
        return self.nome
    
    def get_qtd_total(self):
        return self.qtd_total
    
    def get_qtd_disp(self):
        return self.qtd_disp
    
    def get_qtd_res(self):
        return self.qtd_res
    
    def get_qtd_bloq(self):
        return self.qtd_bloq

    # Requisitos
    def reservar_produtos(self, quantidade):
        if quantidade <= self.qtd_disp:
            self.qtd_disp -= quantidade
            self.qtd_res += quantidade
            print(f"{quantidade} unidades do produto '{self.nome}' reservadas.")
        else:
            print(f"Não há quantidade suficiente disponível para reservar {quantidade} unidades do produto '{self.nome}'.\n Disponível: {self.qtd_disp}, Solicitado: {quantidade}")
            
    def bloquear_produtos(self, quantidade):
        if quantidade <= self.qtd_disp:
            self.qtd_disp -= quantidade
            self.qtd_bloq += quantidade
            print(f"{quantidade} unidades do produto '{self.nome}' bloqueadas.")
        else:
            print(f"Não há quantidade suficiente disponível para bloquear {quantidade} unidades do produto '{self.nome}'.\n Disponível: {self.qtd_disp}, Solicitado: {quantidade}")
            
    def liberar_produtos(self, quantidade, tipo):
        if tipo == "reserva":
            if quantidade <= self.qtd_res:
                self.qtd_res -= quantidade
                self.qtd_disp += quantidade
                print(f"{quantidade} unidades do produto '{self.nome}' liberadas da reserva.")
            else:
                print(f"Não há quantidade suficiente reservada para liberar {quantidade} unidades do produto '{self.nome}'.\n Reservado: {self.qtd_res}, Solicitado: {quantidade}")
        elif tipo == "bloqueio":
            if quantidade <= self.qtd_bloq:
                self.qtd_bloq -= quantidade
                self.qtd_disp += quantidade
                print(f"{quantidade} unidades do produto '{self.nome}' liberadas do bloqueio.")
            else:
                print(f"Não há quantidade suficiente bloqueada para liberar {quantidade} unidades do produto '{self.nome}'.\n Bloqueado: {self.qtd_bloq}, Solicitado: {quantidade}")
        else:
            print("Tipo inválido. Use 'reserva' ou 'bloqueio'.")

# Classe Estoque (guarda todos os produtos)
class Estoque:
    def __init__(self):
        self.produtos = set()  # Usando um conjunto para evitar duplicatas
    
    # Auxiliares
    def get_produto(self, nome_produto):
        return next((produto for produto in self.produtos if produto.name == nome_produto), None)
    
    # Requisitos
    def adicionar_produto(self, produto):
        if produto not in self.produtos:
            self.produtos.add(produto)
            print(f"Produto '{produto.nome}' adicionado ao estoque.")
        else:
            produto_found = self.get_produto(produto.id)
            produto_found.qtd_total += produto.qtd_total
            produto_found.qtd_disp += produto.qtd_total
            print(f"Produto '{produto.nome}' já existe. Quantidade total atualizada para {produto_found.qtd_total}.")
            
    def remover_produto(self, id_produto):
        produto = self.get_produto(id_produto)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto '{produto.nome}' removido do estoque.")
        else:
            print(f"Produto com ID {id_produto} não encontrado no estoque.")
            
    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            print("Produtos no estoque:")
            for produto in self.produtos:
                print(produto)
    
    # Delegações para a classe Produto
    def reservar_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.reservar_produtos(quantidade)
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")

    def bloquear_produtos(self, nome_produto, quantidade):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.bloquear_produtos(quantidade)
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")
    
    def liberar_produtos(self, nome_produto, quantidade, tipo):
        produto = self.get_produto(nome_produto)
        if produto:
            produto.liberar_produtos(quantidade, tipo)
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")
    
    

