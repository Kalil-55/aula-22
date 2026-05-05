#Agora vamos simular uma consulta de dados. Crie uma tabela com alguns nomes e funções usando o pandas e mostre com st.dataframe(). Depois, crie um gráfico de barras que mostre quantas pessoas há em cada função. Dica: use .value_counts() do Pandas e st.bar_chart().

import sqlite3

#conexao = sqlite3.connect("aqui vc cria a database")
#cursor = cursor.execute  - aqui vc já pode colocar as mesmas infos do SQL
#instalar sql viewer

conexao = sqlite3.connect("animais_zoologico.db")

cursor = conexao.cursor()

cursor.execute ('''create table if not exists zoo(
                  id integer primary key autoincrement,
                  nome_animal varchar(70),
                  peso int)
                  ''')

cursor.execute ('''insert into zoo(nome_animal, peso)
                values('onça',80),('mico leão',5),('rinoceronte',2000)''')

conexao.commit()



