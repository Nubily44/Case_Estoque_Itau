# Case Itaú: Controle de Estoque

O programa possui a função de criar um estoque (objeto Estoque) e adicionar e remover produtos (obieto Produto), além de reservar e bloquear quantidades desse produtos, e liberar outras quantidades do bloqueio ou reserva.

## Organização de Versionamento:

- Initial Commit: Structure
  - Organização de ideias e estrutura da documentação
    - Classe -> Estoque (guarda todos os produtos, métodos de interação com produtos)
    - Classe -> Produto (guarda as informações dos produtos, métodos de mudança de estado)

- Planejamento de Requisitos
  - Estoque:
    - Informações:
      - Set de Produtos - check
    - Métodos:
      - adicionar_produtos(produto, qtd) - check
      - retirar_produtos(produto, qtd) - check
      - Auxiliares:
        - get_produto(nome_produto) - check
        - listar_produtos - check
      - Delegações:
        - reservar_produtos - check
        - bloquear_produtos - check
        - liberar_produtos - check
  - Produto:
    - Informações:
      - id - removida (identificador por nome em um conjunto pequeno é mais intuitivo)
      - nome - check
      - qtd_total - check
      - qtd_disp - check
      - qtd_res - check
      - qtd_bloq - check
    - Métodos:
      - reservar_produtos(qtd) - check
      - bloquear_produtos(qtd) - check
      - liberar_produtos(qtd, tipo) - check
        - Uso do tipo, para liberar reservas e bloqueios pela mesma função, porém separando as liberações. Poderia também implementar duas funções, uma para cada finalidade
      - get_id(self) - removido
      - get_nome - check -> removido posteriormente
      - get_qtd_disp - check -> removido posteriormente
      - get_qtd_res - check -> removido posteriormente
      - get_qtd_bloq - check -> removido posteriormente
      - get_qtd_total - check -> removido posteriormente
      - Auxiliares: eq, str e hash (sugestão do copilot, eu havia esquecido) - check
  - Limitações:
    - Estoque (todos tem limite de quantidade disponível):
      - retirar_produtos(p, n) - check
      - reservar_produtos(p, n) - check
      - bloquear_produtos(p, n) - check
      - liberar_produtos(p, n) - check

- Feat: Produto
  - Implementação da classe Produto

- Reorganização de Requisitos
  - reservar, bloquear e liberar produtos movido como métodos do próprio produto, pois lidam diretamente com variáveis internas do Produto. Organização do checklist

- Detalhes de Produto
  - Adicionei alguns gets para ajudar na implementação de Estoque

- Feat: Estoque
  - Impelementação da classe Estoque

- Code Review com IA 1 e 2:
  - Mudanças no código para corrigir problemas, melhorar eficiência e facilitar testes (mais detalhes no Uso de IA)

- Testes

## Estrutura do Código
- Função validar_quantidade: Responsável por validar as quantidades informadas, garantindo que sejam números inteiros positivos. Diferencia erros de tipo (TypeError) e de valor (ValueError).

- Classe Produto: Representa um produto individual no estoque, armazenando seu nome e suas quantidades:
  - qtd_total: quantidade total cadastrada.
  - qtd_disp: quantidade disponível para operações.
  - qtd_res: quantidade reservada.
  - qtd_bloq: quantidade bloqueada.
  - Implementa os métodos de reserva, bloqueio e liberação de produtos, além de uma representação textual personalizada com __str__.
- Classe Estoque: Responsável pelo gerenciamento e armazenamento dos produtos, utilizando um dicionário (dict) para associar cada produto ao seu nome, permitindo buscas e remoções eficientes.
  - Adiciona produtos, somando suas quantidades caso já estejam cadastrados.
  - Remove produtos somente quando não possuem quantidades reservadas ou bloqueadas.
  - Lista e consulta produtos cadastrados.
  - Centraliza as operações de reserva, bloqueio e liberação, delegando suas execuções à classe Produto.
  - Organização da estrutura: A implementação utiliza separação de responsabilidades entre as classes Estoque e Produto, concentrando o gerenciamento geral na primeira e as regras de movimentação de quantidades na segunda.
- Testes
  - Testes de adicionar Produtos
  - Testes de remover Produtos
  - Testes de reservar Produtos
  - Testes de bloquear Produtos
  - Testes de liberar Produtos
  - Testes de consultar Produtos

## Uso de IA ao longo do desenvolvimento

O uso de IA no desenvolvimento pode ser basicamente resumido em 3 funções principais: correções, consulta de sintaxe e autocomplete. A modelagem das classes foi feita de forma independente, e a escrita principal do código também (com auxílio do Github Copilot para maior agilidade). O ChatGPT foi principalmente usado para pedir segundas opiniões (Code Review) e consultar sintaxe. Gosto de usar IAs Generativas para tarefas menores e mais cansativas, e para pedir sugestões de melhorias, focando o trabalho principal de estrutura e modelagem do código eu mesma

ChatGPT:
Disponível em: <chat>[https://chatgpt.com/share/6aef8708-41b4-83e9-98dd-e42fa8255d92]

Consulta de como é a sintaxe do uso de um set():

- set(), .add e .discard()

Consulta sobre o conceito de delegações (Não lembrava o nome)

Code Review com IA - 1

- Correção de sintaxe em get_produto
- Correção no __eq__ e __hash__
- Edge case: quantidades negativas e parciais nas operações com produtos
- Mudança de Set para Dict por eficiência no Estoque
- validar estoque e quantidade
- Mover prints para os tests automatizando, limpando as classes

Code Review com IA - 2

- validar quantidade melhorado
- remoção do __eq__ e __hash__
- Melhoria da lógica de True e Falses, e returns para facilitar os testes
- Proibir remoção de produtos com reservas e bloqueios

Code Review Final

- Mudança na forma que listar produtos funciona
- Simplificação de consultar_produto

Github Copilot (sem log, uso integrado no VSCode):
Sugestão de auxiliares de funções (__eq__, __str__, __hash__)

## Conclusões

Programa feito em 3 horas e 30 minutos, distribuído em 2 dias (Sexta a noite e Sábado a tarde)

Melhorias caso fosse usado em produção:

- Melhorar a estrutura das delegações
- validar se o Estoque só tem objetos de Produto
- Validar o formato do nome do produto
- Melhorar o encapsulamento das funções e acesso a atributos
- Uso do pytest para testes (não conhecia, sugestão do ChatGPT)
- Ter um método de garantir que a soma da quantidade total é sempre constante em operações de bloqueio, reserva e liberação
- Implementação de Threads para evitar mudanças de estado simultâneas
- Uso de Hash como chave principal para busca e demais operações

Principais Dificuldades:

- Não estou acostumada a fazer testagem tão a fundo de código
- Falta de claridade de como a função De liberar bloqueio ou reserva deveria funcionar no enunciado

## Como executar o código

```cmd
python case.py
```
