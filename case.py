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

