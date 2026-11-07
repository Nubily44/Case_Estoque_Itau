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
      - reservar_produtos(produto, qtd) - check
      - bloquear_produtos(produto, qtd) - check
      - liberar_produtos(produto, qtd, tipo) - check (uso do tipo, para liberar reservas e bloqueios pela mesma função, porém separando as liberações. Poderia também implementar duas funções, uma para cada finalidade)
      - Auxiliar: get_produto(id_produto) - check
  - Produto:
    - Informações:
      - id - removida (identificador por nome em um conjunto pequeno é mais intuitivo)
      - nome - check
      - qtd_disp - check
      - qtd_res - check
      - qtd_bloq - check
      - qtd_total - check
    - Métodos:
      - get_id(self)
      - get_qtd_disp
      - get_qtd_res
      - get_qtd_bloq
      - qtd_total
      - Auxiliares: eq, str e hash (sugestão do copilot, eu havia esquecido)
- Limitações:
  - Estoque: retirar_produtos(p, n), reservar_produtos(p, n), bloquear_produtos(p, n), liberar_produtos(p, n) -> não pode atingir mais que o disponíve de produtos

## Uso de IA ao longo do desenvolvimento

## Conclusões:

Como executar o código:
