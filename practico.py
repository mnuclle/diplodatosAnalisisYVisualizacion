# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import matplotlib.pyplot as plt
import numpy
import pandas
import seaborn


path='C:/Users/23376168824/Downloads/the-human-freedom-index/'
dataset = pandas.read_csv(path+'hfi_cc_2018.csv')
dataset.shape

dataset.columns


important_cols = ['year', 'ISO_code', 'countries', 'region']
important_cols += [col for col in dataset.columns if 'pf_identity' in col]
important_cols += [
 'ef_score', # Economic Freedom (score)
 'ef_rank', # Economic Freedom (rank)
 'hf_score', # Human Freedom (score)
 'hf_rank', # Human Freedom (rank)
]

dataset[important_cols]
dataset[important_cols].describe()

important_cols2=['pf_identity','hf_score','ef_score']
dataset[important_cols2].describe()

datasetlatin=dataset[(dataset.region=='Latin America & the Caribbean')]

datasetlatin.describe()
datasetlatin[important_cols].describe()

dataset[important_cols2].describe()
datasetlatin[important_cols2].describe()

dataset[important_cols2].median()
datasetlatin[important_cols2].median()



"Nosotros centrarermos nuestro análisis en variables relacionadas a 
"Identity and Relationships en paises de Latinoamérica, y los compararemos con las estadísticas globales.
" La pregunta a responder es simple: ¿Qué niveles de libertad se viven en Latinoamérica, especificamente en cuanto libertades de indentidad?. 
"Sin embargo, para hacer un análisis de los datos tenemos que platear también estas sub preguntas:

"¿Qué significa tener un puntaje de 4.5? Hay que poner los puntajes de la región en contexto con los datos del resto del mundo.
"¿Cuál es la tendencia a lo largo de los años? ¿Estamos mejorando, empeorando?
"En este estudio, la libertad se mide con dos estimadores principales: 
    "hf_score que hace referencia a Human Freedom, y 
    "ef_score que hace referencia a Economic Freedom. 
"Estos dos estimadores, ¿se relacionan de la misma manera con la libertad de identidad?


seaborn.barplot(data=dataset, x='region', y='pf_identity')
plt.xticks(rotation=45)

seaborn.barplot(data=dataset, x='region', y='hf_score')
plt.xticks(rotation=45)

seaborn.barplot(data=dataset, x='region', y='ef_score')
plt.xticks(rotation=45)



plt.figure(figsize=(10,6))
seaborn.barplot(data=dataset, x='year', y='pf_identity',
                hue='region', ci='sd')
plt.ylabel('identidad')
plt.xlabel('libertad economica')
plt.ylim(0, 4)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine(left=True)

" grafico de lineas por regiones
plt.figure(figsize=(10,8))
seaborn.pointplot(data=dataset,
                  x='year', y='pf_identity',
                  hue='region', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)
plt.ylabel('pf identity')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()

plt.figure(figsize=(10,8))
seaborn.pointplot(data=datasetlatin,
                  x='year', y='hf_score',
                  dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)
seaborn.pointplot(data=datasetlatin,
                  x='year', y='ef_score',
                  dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)
plt.ylabel('pf identity')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()


plt.figure(figsize=(10,8))
seaborn.pointplot(data=dataset,
                  x='year', y='pf_identity',
                   dodge=True, ci='sd',
                  markers='v', linestyles='-', errwidth=1, capsize=0.2)
plt.ylabel('pf identity')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()


"libertad economica de paises de latinoamerica"
plt.figure(figsize=(10,8))
seaborn.pointplot(data=datasetlatin,
                  x='year', y='ef_score',
                  hue='countries', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()

"libertad economica de paises de latinoamerica argentina y venezuela"
plt.figure(figsize=(10,8))
seaborn.pointplot(data=datasetlatin[datasetlatin.countries=='Argentina'],
                  x='year', y='ef_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#33C4FF")
seaborn.pointplot(data=datasetlatin[datasetlatin.countries=='Argentina'],
                  x='year', y='hf_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#bb3f3f")
seaborn.pointplot(data=datasetlatin[datasetlatin.countries=='Argentina'],
                  x='year', y='py_identity', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#ff5733")
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()


"prueba anterior"
plt.figure(figsize=(10,8))
seaborn.pointplot(data=datasetlatin[datasetlatin.countries=='Argentina'],
                  x='year', y='hf_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#ff5733")
seaborn.pointplot(data=datasetlatin[datasetlatin.countries=='Argentina'],
                  x='year', y='ef_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#33C4FF")
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()


"libertad de paises de oceania"
plt.figure(figsize=(10,8))
seaborn.pointplot(data=dataset,
                  x='year', y='hf_score',
                  hue='countries', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)
seaborn.pointplot(data=dataset,
                  x='year', y='py_identity',
                  hue='countries', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2)

plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()



color="#bb3f3f"









dataset.hf_score+

" respuesta 3 graficos con y sin valores nulos
plt.figure(figsize=(10,8))
seaborn.pointplot(data=dataset,
                  x='year', y='ef_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#33C4FF")
seaborn.pointplot(data=dataset,
                  x='year', y='hf_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#bb3f3f")
seaborn.pointplot(data=dataset,
                  x='year', y='pf_identity', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#ff5733")
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()

datasetna=dataset[important_cols].dropna()
datasetna.shape

datasetna=dataset[['year','pf_identity', 'hf_score', 'ef_score']].dropna()
datasetna.columns
datasetna.shape



plt.figure(figsize=(10,8))
seaborn.pointplot(data=datasetna,
                  x='year', y='ef_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#33C4FF")
seaborn.pointplot(data=datasetna,
                  x='year', y='hf_score', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#bb3f3f")
seaborn.pointplot(data=datasetna,
                  x='year', y='pf_identity', dodge=True, ci='sd',
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#ff5733")
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
seaborn.despine()














plt.figure(figsize=(10,8))
seaborn.pointplot(data=dataset,
                  x='year', y='pf_identity', dodge=True, ci='sd', 
                  hue='region'
                  markers='v', linestyles='--', errwidth=1, capsize=0.2, color="#ff5733")
plt.ylabel('lib economica')
plt.xlabel('años')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
seaborn.despine()




plot_data = plot_data.rename(columns={
    'Años en la empresa actual': 'Antiguedad', 'Años de experiencia': 'Experiencia',
    NETO_COL: 'Salario', '¿De qué % fue el ajuste?': 'Ajuste'
})
seaborn.pairplot(
    data=dataset,
    vars=['pf_identity', 'hf_score', 'ef_score'], hue='region',
    markers='+')