def converte_nota_em_conceito(nota):
    if nota >= 9.0:
      return "A"
    elif nota >= 8.0:
      return "B"
    elif nota >= 7.0:
      return "C"
    elif nota >= 6.0:
      return "D"
    elif nota >= 4.0:
      return "E"
    else:
      return "F"

print(converte_nota_em_conceito(4.0))