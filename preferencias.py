import pandas as pd

# Leitura da tabela do excel e armazenando na variavel df
df = pd.read_excel(r"C:\Users\Evandro\Downloads\preferencias.xlsx")

# Adicionando a cada variavel as médias das idades
brasileira = df[df.Culinária_preferida == "Brasileira"].Idades.mean().round()
francesa = df[df.Culinária_preferida == "Francesa"].Idades.mean().round()
italiana = df[df.Culinária_preferida == "Italiana"].Idades.mean().round()
japonesa = df[df.Culinária_preferida == "Japonesa"].Idades.mean().round()

# Verificando a quantidade de pessoas a cada preferencia
qtdBrasileira = df[df.Culinária_preferida == "Brasileira"].Culinária_preferida.count()
qtdFrancesa = df[df.Culinária_preferida == "Francesa"].Culinária_preferida.count()
qtdItaliana = df[df.Culinária_preferida == "Italiana"].Culinária_preferida.count()
qtdJaponesa = df[df.Culinária_preferida == "Japonesa"].Culinária_preferida.count()

# Imprimindo resultado
print('De {} pessoas que preferem comida Brasileira, a média de idade é de {:.0f} anos'.format(qtdBrasileira, brasileira))
print('De {} pessoas que preferem comida Francesa, a média de idade é de {:.0f} anos'.format(qtdFrancesa, francesa))
print('De {} pessoas que preferem comida Italiana, a média de idade é de {:.0f} anos'.format(qtdItaliana, italiana))
print('De {} pessoas que preferem comida Japonesa, a média de idade é de {:.0f} anos'.format(qtdJaponesa, japonesa))

# Criando dicionario com os dados que ja temos
d = {'Culinária_preferida':['brasileira', 'francesa', 'italiana', 'japonesa'], 'Média de idade': [brasileira, francesa, italiana, japonesa]}

# Impressão de dicionario
print(d)

# Criação do DataFrame
dados = pd.DataFrame(data= d)

# Exportando para tabela do excel
dados.to_excel('dados.xlsx', index = False)
