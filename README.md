# bigdatauni

# Això és un títol (#)
## Això és un subtítol (##)
### Això és un sub-subtítol (###)
```Python
def hola():
	print("Hola! He de posar 3 accents oberts per obrir aquesta cosaaa.")
hola()
```
#això_és_una_etiqueta Permet connectar documents amb les mateixes etiquetes.

Llistes python:
```python
llista1=[poma,taronja,mandarina]

# Això és un títol (#)
## Això és un subtítol (##)
### Això és un sub-subtítol (###)
```Python
def hola():
	print("Hola! He de posar 3 accents oberts per obrir aquesta cosaaa.")
hola()
```
#això_és_una_etiqueta Permet connectar documents amb les mateixes etiquetes.

Llistes python:
```python
llista1=[poma,taronja,mandarina]
```
**Append vs. extend:** Quan volem sumar llistes ens trobem amb dues opcions (append, extend).

```python
nom="Miquel"
print (f"En {nom} és estudiant de la WAP.")
	   
```

Com aparellem elements de dues llistes amb Python?
**Funció ZIP**

```python
notas = ["5","7","6","4","8","2"]
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]

for nota,nom in zip(notas,alumnos):
	print(nota, nom)
```

La funció index: la posició d'elements en una llista.
La funció set() ens treu els elements duplicats d'una llista, deixant els valors únics.
```python
llista=["adria", "carla", "joan", "pere", ]
nom="carla"

if nom in llista:
	print("Sí")
	position = llista.index(nom)
	print(position)

valors_unics=set(llista)
```

```python
notes = ["5","3","7","8","9.5","4","6,2"]
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]

1.  Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".
2.  Calcula e imprime la nota promedio del aula con un decimal
3.  Calcula e imprime la nota más alta junto al nombre del alumno.
4.  calcula e imprime la nota más baja junto al nombre del alumno.
5. ```

**Tuplas**
Les tuples són llistes que tenen dos o més valors per a cada element.
```python
#EXERCICI 2. PANDAS. 28/02/2023
notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]
nomsencer=[]
nomnota=[]

for nom, cognom, nota in zip (alumnes, cognoms, notes):
    nom_complet = f"{nom} {cognom}"
    nomnot=(nom_complet, nota)
    nomnota.append(nomnot)

print(nomnota)
```

**DataFrames with Pandas**
Les taules amb Pandas estan fetes de tuples.
```python
import pandas as pd
df= pd.DataFrame(llista_definitiva, columns=["nom", "nota", "quali"])
df.to_csv("dataset.csv")
```
Read the Docs és una plataforma que serveix per a veure la documentació d'una llibreria de python. 
Pandas serveix tant per a crear dataframes com per a llegir-los.

<h1>Twitch API </h1>
Instal·lem la API de Twitch amb pip install twitchAPI, i instal·lem la versió 2.5, perquè tot i ser antiga compta amb menys errors.

Amb el següent codi extraiem les dades dels 20 streams amb més espectadors en espanyol.

```python
from twitchAPI.twitch import Twitch

twitch = Twitch('59gikkgx87fx1qdk789jtxvcts4y37', '1zfxynl9zypqfw50ycb5s7eokt9ly5')
print(twitch.get_users(logins=['collpetit']))

streams=twitch.get_streams(first=20, language="es")
print(streams)

for d in streams:
	hora = now
	usuari = d["user_name"]
	viewers = d["viewer_count"]
	df = pd.DataFrame({
	"Hora": hora,
	"Usuari": usuari,
	"Viewers": viewers,
	}, index = [0])
	llista_dataframes.append(df)

final_dataframe=pd.concat(llista_dataframes)
print (final_dataframe)

final_dataframe.to_csv("export.csv", index=False)
```

<H1>Pandas Python</h1>
Per obrir un arxiu .csv amb python cal importar la llibreria de pandas, i llegir-lo amb la funció pd.read_csv()

Per veure les columnes podem utilitzar la funció .columns.
<h3>Veure columnes i files</h3>
La funció .shape retorna una tupla amb el número de files i el número de columnes de l'arxiu.

**APUNTE**
Quan fem un readcsv amb python, aquest posa l'arxiu a la RAM per treballar amb ell. Si pesa més 'arxiu que la capacitat de la nostra RAM, estem fora.

**Trobar les files i columnes d'un dataset.**
La funció .shape et torna una tupla amb el valor de les files i el valor de les colmnes. De totes maneres, en fer un print d'un dataset et diu el nombre de files i de columnes.

**Veure les columnes del dataset**
Per a veure les columnes, pandas té una funció que és .columns.

**Treure columnes del dataset**
La funció .drop de pandas 
```python
df.drop(["Columna1", "Columna2", "Columna3", ...], axis=1, inplace=True)
#l'atribut inplace elimina les columnes per sempre. Si es vol mantenir el dataset sencer per a posteriori:

df_nou=df.drop(["Columna1", "Columna2", "Columna3", ...], axis=1)

```
**Funció CHUNKSIZE**
La funció chunksize permet carregar els datasets en blocs més petits de dades. 
Un cop es tenen els chunks creats, es pot iterar una llista amb 

for chunks in df:
	tal tal tal
