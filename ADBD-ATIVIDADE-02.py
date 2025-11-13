import pandas as pd

df = pd.read_csv(r"C:\Users\Jeanh\Desktop\testes\ADBD-ATIVIDADE-02\Jogadores.csv", sep=";")

# Converter o salário para número e substituir null por NaN
df["salario_do_jogador"] = pd.to_numeric(df["salario_do_jogador"], errors="coerce")

print(" VISÃO GERAL DOS DADOS ")
print(df.head(), "\n")

# a) Nome e time dos jogadores com salário acima de R$ 20k
acima_20k = df.loc[df["salario_do_jogador"] > 20000, ["nome_do_jogador", "nome_time_jogador"]]
print(" Jogadores com salário acima de R$ 20.000 ")
print(acima_20k, "\n")

# b) Nome e salário dos jogadores dos times de Minas Gerais
times_mg = df.loc[df["nome_estado_jogador"] == "MG", ["nome_do_jogador", "salario_do_jogador"]]
print(" Jogadores dos times de Minas Gerais ")
print(times_mg, "\n")

# c) Nome e time dos jogadores cujo nome contenha a letra u
contendo_u = df.loc[df["nome_do_jogador"].str.contains("u", case=False, na=False), ["nome_do_jogador", "nome_time_jogador"]]
print(" Jogadores cujo nome contém a letra 'u' ")
print(contendo_u, "\n")

# d) Nome, salário e time dos jogadores, ordenados pelo salário decrescente
ordenado_salario = df[["nome_do_jogador", "salario_do_jogador", "nome_time_jogador"]].sort_values(by="salario_do_jogador", ascending=False)
print(" Jogadores ordenados por salário (decrescente) ")
print(ordenado_salario, "\n")

# e) Nome, salário e time ordenados por nome do time (crescente) e salário (decrescente)
ordenado_time_salario = df[["nome_do_jogador", "salario_do_jogador", "nome_time_jogador"]].sort_values(
    by=["nome_time_jogador", "salario_do_jogador"], ascending=[True, False]
)
print(" Jogadores ordenados por time (A–Z) e salário (decrescente) ")
print(ordenado_time_salario, "\n")

# f) Quantidade de jogadores por time
qtd_por_time = df["nome_time_jogador"].value_counts()
print(" Quantidade de jogadores por time ")
print(qtd_por_time, "\n")

# g) Média salarial por time
media_por_time = df.groupby("nome_time_jogador")["salario_do_jogador"].mean()
print(" Média salarial por time ")
print(media_por_time, "\n")
