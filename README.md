# Case Itaú: Controle de Estoque

## Organização de Versionamento:

- Initial Commit: Structure
  - Organização de ideias e estrutura da documentação

Classe -> Estoque (guarda todos os produtos, métodos de interação com produtos)
Classe -> Produto (guarda as informações dos produtos, métodos de mudança de estado)

- Planejamento de Requisitos
  - Estoque:
    - Informações:
      - Set de Produtos -
    - Métodos:
      - adicionar_produtos(produto, qtd) -
      - retirar_produtos(produto, qtd) -
      - Auxiliar: get_produto(id_produto) -
  - Produto:
    - Informações:
      - id - removida (identificador por nome em um conjunto pequeno é mais intuitivo)
      - nome - check
      - qtd_total - check
      - qtd_disp - check
      - qtd_res - check
      - qtd_bloq - check
    - Métodos:
      - reservar_produtos(produto, qtd) - check
      - bloquear_produtos(produto, qtd) - check
      - liberar_produtos(produto, qtd, tipo) - check
        - Uso do tipo, para liberar reservas e bloqueios pela mesma função, porém separando as liberações. Poderia também implementar duas funções, uma para cada finalidade
      - get_id(self) - removido
      - get_qtd_disp - 
      - get_qtd_res - 
      - get_qtd_bloq - 
      - get_qtd_total - 
      - Auxiliares: eq, str e hash (sugestão do copilot, eu havia esquecido) - checkl
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

## Uso de IA ao longo do desenvolvimento

ChatGPT:
Consulta de como é a sintaxe do uso de um set():

- declaração: set(), .add e .discard()

Github Copilot (sem log, uso integrado no VSCode):
Sugestão de auxiliares de funções (__eq__, __str__, __hash__)

## Conclusões:

Como executar o código:
