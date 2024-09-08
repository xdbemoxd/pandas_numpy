import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

out = False

def convert_from_pandas_to_NumPy( panda ):
    
    population = panda.to_numpy()

    population = population[ 0 ]

    return population

def timeframe_selection():

    print( 'Ingrese el periodo de tiempo: ' )
    print( '1.2022 Population\t2.2020 Population\t3.2015 Population\t4.2010 Population\n5.2000 Population\t6.1990 Population\t7.1980 Population\t8.1970 Population' )
    opc = int( input() )

    if opc == 1:

        time_span = '2022 Population'

    elif opc == 2:

        time_span = '2020 Population'

    elif opc == 3:

        time_span = '2015 Population'

    elif opc == 4:

        time_span = '2010 Population'

    elif opc == 5:

        time_span = '2000 Population'

    elif opc == 6:

        time_span = '1990 Population'

    elif opc == 7:

        time_span = '1980 Population'

    elif opc == 8:

        time_span = '1970 Population' 

    return time_span

def population_country( df ):
    
    country_name = input( 'ingrese el nombre del pais: ' )
    
    df_aux = df[ df[ 'Country/Territory' ] == country_name ]

    population = df_aux.loc[ : , [ '1970 Population','1980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population', '2022 Population'] ]
    
    population_2 = convert_from_pandas_to_NumPy( population )

    time = [ '1970 Population','1980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population', '2022 Population']

    #time.reverse()    
    
    plt.figure( figsize = ( 8, 6 ) )

    #crear el grafico
    plt.plot( time, population_2, marker = 'o', color='blue' )

    plt.title( 'Poblacion en los distintos peridos de tiempo' )

    plt.xlabel( 'Años' )
    plt.ylabel( 'Escala de habitantes' )

    plt.show()

def population_continent( df ):

    time_span = timeframe_selection()  

    plt.figure( figsize = ( 8, 8 ) )

    df_aux = df.groupby( 'Continent' )[ time_span ].sum().plot( kind = 'pie' )

    plt.title( "Distribucion de poblacion por contienetes en un periodo de tiempo" )
    plt.show()

def population_continent_2( df ):

    name_continent = input( 'Ingrese el nombre del continente: ' )

    df_aux = df[ df[ 'Continent' ] == name_continent ]

    plt.figure( figsize = ( 8, 8 ) )

    df_aux = df_aux.loc[ : , [ '1970 Population','1980 Population', '1990 Population', '2000 Population', '2010 Population', '2015 Population', '2020 Population', '2022 Population'] ].sum().plot( kind = 'line' )

    plt.title( "Distribucion de poblacion en un contienete en los diferentes periodos de tiempo" )
    plt.show()

def most_populous_countries( df ):
    
    time_span = timeframe_selection()

    plt.figure( figsize = ( 8, 8 ) )

    df_aux = df.groupby( 'Country/Territory' )[ time_span ].nlargest(10)

    df_aux.nlargest(10).plot( kind = 'bar' )

    plt.title( "10 paises con más poblacion en un periodo de tiempo" )
    plt.xticks(rotation=45)
    plt.show()

def continental_population_leaders( df ):
    print( 'Seleccione un contienente' )
    print('1.Asia\n2.Africa\n3.Europe\n4.North America\n5.Oceania\n6.South America')
    opc = int(input())

    if opc == 1:

        name_continent = 'Asia'
    
    elif opc == 2:

        name_continent = 'Africa'

    elif opc == 3:

        name_continent = 'Europe'

    elif opc == 4:

        name_continent = 'North America'

    elif opc == 5:

        name_continent = 'Oceania'

    elif opc == 6:

        name_continent = 'South America'

    time_span = timeframe_selection()

    df_aux = df[ df[ 'Continent' ] == name_continent ]

    df_aux  = df_aux.groupby( 'Country/Territory' )[ time_span ].nlargest(5)

    df_aux.nlargest(5).plot( kind = 'bar' )

    plt.title( "5 paises con más poblacion en un periodo de tiempo" )
    plt.xticks(rotation=45)
    plt.show()


while ( not out ):

    print( 'Ingrese la opcion que considere mas conveniente' )
    print( '1.Mostrar poblacion de un pais en varios periodos de tiempo' )
    print( '2.Mostrar poblacion de los contienentes en un periodo de tiempo' )
    print( '3.Mostrar poblacion de un continente en los distintos periodos de tiempo' )
    print( '4.Top 10 Paises con más poblacion en un periodo de tiempo a nivel mundial' )
    print ( '5.Top 5 paises con más poblacion a nivel continental en un periodo de tiempo' )
    print( '0.Salir' )

    opc = int( input() )

    if opc == 0:

        out = True

    elif opc == 1:

        population_country( df )

    elif opc == 2:

        population_continent( df )

    elif opc == 3:

        population_continent_2( df )

    elif opc == 4:

        most_populous_countries( df )
    
    elif opc == 5: 

        continental_population_leaders( df )
       