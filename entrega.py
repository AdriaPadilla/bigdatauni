'''
EXERCICI 1 
'''
import pandas as pd
import time

chunksize = 12000

# Llegeix el fitxer "feb_23.csv" amb separador de columnes "\t", només llegint les columnes "captured_at" i "viewer_count"
df = pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"], nrows=2)

# Agrupem els valors de viewer_count per captured_at, calculant la suma dels viewers per a cada captured_at
viewers = df.groupby("captured_at")["viewer_count"].sum().tolist()

# Creem una llista amb les distintes hores de captured_at del dataframe original
hora = df["captured_at"].unique().tolist()

# Crea un diccionari amb les llistes d'hores i viewers per crear un nou dataframe
data = {'captura': hora, 'viewers': viewers}

# Mostra les dades del diccionari i el nombre d'elements a les llistes hora i viewers
print(data)
print(len(hora), len(viewers))

# Crea un nou dataframe a partir del diccionari "data", especificant les columnes "captura" i "viewers", i guarda'l en un fitxer CSV
df = pd.DataFrame(data, columns=['captura', 'viewers'])
df.to_csv('exercici1.csv', index=False)


# Print the result DataFrame


'''
EXERCICI 2
'''
import pandas as pd
import time

chunksize=20000
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["game_name", "viewer_count"], chunksize=chunksize)#Llegim les tres columnes que ens interessen de l'arxiu per chunks.

result=[]
result_count=[]

for chunk in df:
	viewers=chunk.groupby("game_name")["viewer_count"].sum().reset_index() #Agrupem per jocs i sumem els viewers de cada chunk.
	counts=(chunk["game_name"].value_counts()/4).reset_index() #calculem les hores (aparicions/4)
	result.append(viewers)#afegim el resultat per de cada chunk.
	result_count.append(counts)



result_count2=pd.concat(result_count, axis=0, ignore_index=True)
df= pd.concat(result, axis=0, ignore_index=True) #concatenem tots els appends en un.

result_count2=result_count2.rename(columns={"game_name":"hores"}) #renombrem les columnes ja que hem detectat que estaven mal nombrades.
result_count2=result_count2.rename(columns={"index":"game_name"})

df2=df.groupby("game_name")["viewer_count"].sum().reset_index()#Tornem a agrupar la llista definitiva
df3=result_count2.groupby("game_name")["hores"].sum().reset_index()#Tornem a agrupar la llista definitiva


result=pd.merge(df2, df3, on="game_name") #ajuntem els dos datasets per la columna "game_name"
#result = pd.concat([df2.reset_index(), result_count2.reset_index()], axis=1)
result.to_csv("exercici2.csv", index=False)

'''
EXERCICI 3
'''
import pandas as pd
import time

chunksize=20000
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "game_name"], chunksize=chunksize)#Llegim les tres columnes que ens interessen de l'arxiu per chunks.

game_counts=[]

for chunk in df:
    for captured_at_value in chunk["captured_at"].unique(): #fem un for per a cada valor únic dela data.
        counts = chunk[chunk["captured_at"] == captured_at_value]["game_name"].value_counts().reset_index() #igualem la variable counts a una taula amb el compte i la categoria.
        counts.columns = ["game_name", "count"] #Nomenem les columnes.
        counts["capture_date"] = captured_at_value #afegim una columna que posarà la data de cada moment.
        game_counts.append(counts.copy()) #fem un append al dataframe final amb copy, per assegurar-nos que estem treballant amb una còpia i en cas que doni error no perjudiqui.


df = pd.concat(game_counts) #concatenem el game_counts
df.to_csv("exercici3.csv", index=False) #ho exportem a dataset.


'''
EXERCICI 4
'''
import pandas as pd
import time

chunksize=20000
df= pd.read_csv("feb_23.csv", sep='\t', usecols=["streamer_name", "viewer_count"], chunksize=chunksize)#Llegim les tres columnes que ens interessen de l'arxiu per chunks.

result=[]
result_count=[]

for chunk in df:
	viewers=chunk.groupby("streamer_name")["viewer_count"].sum().reset_index() #Agrupem per streamers i sumem els viewers de cada chunk.
	counts=(chunk["streamer_name"].value_counts()/4).reset_index() #calculem les hores (aparicions/4)
	result.append(viewers)#afegim el resultat per de cada chunk.
	result_count.append(counts)



result_count2=pd.concat(result_count, axis=0, ignore_index=True)
df= pd.concat(result, axis=0, ignore_index=True) #concatenem tots els appends en un.

result_count2=result_count2.rename(columns={"streamer_name":"hores"}) #renombrem les columnes ja que hem detectat que estaven mal nombrades.
result_count2=result_count2.rename(columns={"index":"streamer_name"})

df2=df.groupby("streamer_name")["viewer_count"].sum().reset_index()#Tornem a agrupar la llista definitiva
df3=result_count2.groupby("streamer_name")["hores"].sum().reset_index()#Tornem a agrupar la llista definitiva


result=pd.merge(df2, df3, on="streamer_name") #ajuntem els dos datasets per la columna "streamer_name"
print(result)
#result = pd.concat([df2.reset_index(), result_count2.reset_index()], axis=1)
result.to_csv("exercici2.csv", index=False)


'''
EXERCICI 5 
'''
import pandas as pd


df= pd.read_csv("feb_23.csv", sep='\t', usecols=["captured_at", "viewer_count"])

# Agrupem els espectadors per hora i els passem a llista
viewers=df.groupby("captured_at")["viewer_count"].sum().tolist()

# Creem una llista única amb les hores de les captures
hora=df["captured_at"].unique().tolist()

# Creem un diccionari amb les dades agrupades i les llistes creades abans
data = {'captura': hora, 'viewers': viewers}

# Unim les llistes "viewers" i "captura" amb la funció "zip"
junto = zip(data["viewers"],data["captura"])

# Creem una nova llista amb les tuples creades
ex = []
for i in junto:
    ex.append(i)

df1 = pd.DataFrame(ex, columns=['viewers','captura'])# Creem un nou df amb les dades agrupades i la nova llista creada


df1['std_viewers'] = df.groupby("captured_at")["viewer_count"].std().round(2).tolist()# Afegim una nova columna amb la desviació estàndard dels espectadors per hora arrodonida a 2 decimals

print(df1)# Imprimim el DataFrame final

df1.to_csv('exercici-5.csv')# Passem el df a .csv