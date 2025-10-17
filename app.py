def eh_maior_idade(idade, limite=18):
  try:
    idade = int(idade)
  except (ValueError, TypeError):
    raise ValueError("Idade inválida")
  if idade < 0:
    raise ValueError("Idade não pode ser negativa")
  return idade >= limite

if __name__ == "__main__":
  entrada = input("Digite a idade: ").strip()
  try:
    if eh_maior_idade(entrada):
      print("Maior de idade")
    else:
      print("Menor de idade")
  except ValueError as e:
    print("Erro:", e)
