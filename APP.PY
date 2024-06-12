import sqlite3

perguntar = input("Digite o nome do funcionário: ")

conn = sqlite3.connect('funcionario.db')

c = conn.cursor()

# Correção da consulta SQL e adição da cláusula WHERE
c.execute("SELECT * FROM funcionario WHERE funcionario=?", (perguntar,))
resultado = c.fetchall()

if resultado:
    print(f"USUÁRIO ENCONTRADO: {resultado}")
else:
    print("USUÁRIO NÃO ENCONTRADO!")

conn.close()