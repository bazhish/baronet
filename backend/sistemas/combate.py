def dentro_do_range(entidade1, entidade2, alcance):
    cx1 = entidade1.posicao_x + 25
    cy1 = entidade1.posicao_y + 40
    cx2 = entidade2.posicao_x + 25
    cy2 = entidade2.posicao_y + 40
    distancia = ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5
    return distancia <= alcance
