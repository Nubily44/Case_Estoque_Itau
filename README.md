# Case Itaú: Controle de Estoque

## Organização de Versionamento:

- Initial Commit: Structure
  - Organização de ideias e estrutura da documentação

Classe -> Estoque (guarda todos os produtos, métodos de interação com produtos)
Classe -> Produto (guarda as informações dos produtos, métodos de mudança de estado)

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
      - get_nome - check
      - get_qtd_disp - check
      - get_qtd_res - check
      - get_qtd_bloq - check
      - get_qtd_total - check
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

- Code Review com IA:
  - Mudanças no código para corrigir problemas, melhorar eficiência

## Uso de IA ao longo do desenvolvimento

ChatGPT:
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

Code 

Github Copilot (sem log, uso integrado no VSCode):
Sugestão de auxiliares de funções (__eq__, __str__, __hash__)

## Conclusões:

Como executar o código:
