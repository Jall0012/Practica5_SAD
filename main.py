# This is a sample Python script.
import tkinter as tk  # ✅ Importación correcta del módulo principal
from tkinter import messagebox

from AppComparacionAHP import AppComparacionAHP
from Criterio import Criterio


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    ############################Valor de Rivera #######################
    score_rivera = 0.9126
    precios = [125, 125, 137.3]
    overall = [0.7402, 0.4431, 0.5987]
    valor_rivera = score_rivera * (sum(precios) / sum(overall))

    print(valor_rivera)

    matrizCriterios = [
        Criterio("¿Como de importantes son la cantidad de compradores respecto a la visibilidad del local?", 0, 1,3),
        Criterio("¿Como de importantes son la cantidad de compradores respecto a la cantidad de competencia?", 0, 2,7),
        Criterio("¿Como de importantes son la cantidad de compradores respecto al costo?", 0, 3,8),
        Criterio("¿Como de importantes es la visibilidad del local respecto a la cantidad de competencia?", 1, 2,3),
        Criterio("¿Como de importantes es la visibilidad del local respecto al costo", 1, 3,6),
        Criterio("¿Como de importantes es la cantidad de competencia respecto al costo?", 2, 3,3)
    ]

    matrizCompradores = [
        Criterio("¿Como de superior es un conjunto de posibles clientes compuesto por fuertes compradores de productos electronicos no son pensionistas respecto a un conjunto compuesto fundamentalmente por oficinistas?",0,1,8),
        Criterio("¿Como de superior es un conjunto de posibles clientes compuesto por fuertes compradores de productos electronicos no son pensionistas respecto a un conjunto compuesto fundamentalmente por una mezcla diversa de transeuntes?", 0, 2,6),
        Criterio("¿Como de superior es un conjunto de posibles clientes compuesto fundamentalmente por oficinistas respecto a un conjunto compuesto por una mezcla diversa de transeuntes?", 1, 2,-3),

    ]

    matrizVisibilidad = [
        Criterio("¿Como de superior es un local con una amplia entrada y una ventana respecto a un local con una pequeña entrada?", 0, 1,5),
        Criterio("¿Como de superior es un local con una amplia entrada y una ventana respecto a un local con una amplia entrada y varias ventanas?", 0, 2,-3),
        Criterio("¿Como de superior es un local con una pequeña entrada respecto a un local con una amplia entrada y varias ventanas?", 1, 2,-7)
    ]

    matrizCompetencia = [
        Criterio("¿Como de superior es tener de competencia a una gran variedad de comercio y tiendas de antigüedades y souvenirs respecto a una competencia compuesta de un local no relacionado con la electronica?", 0, 1,-7),
        Criterio("¿Como de superior es tener de competencia a una gran variedad de comercio y tiendas de antigüedades y souvenirs respecto a un pequeño negocio de moviles?", 0, 2,-2),
        Criterio("¿Como de superior es una competencia compuesta de un local no relacionado con la electronica respecto a un pequeño negocio de moviles?", 1, 2,4)
    ]

    matrizCosto = [
        Criterio("¿Como de superior es una renta costosa respecto a una a la mitad de precio del anterior?", 0, 1,-8),
        Criterio("¿Como de superior es una renta costosa respecto a un costo promedio?", 0, 2,-4),
        Criterio("¿Como de superior es una renta a mitad de precio que la opción A respecto a un costo promedio?", 1, 2,3)
    ]

    ###########################################################################################################################################################
    ###########################################################################################################################################################
    ###########################################################################################################################################################
    ###########################################################################################################################################################

    matrizCriterios2 = [
        Criterio("¿Como de superior es el criterio P.Tareas respecto al criterio colaboración?",0, 1,2),
        Criterio("¿Como de superior es el criterio P.Tareas respecto al criterio E.Riesgos?", 0, 2,6),
        Criterio("¿Como de superior es el criterio P.Tareas respecto al criterio V.Gráfica?", 0, 3,2),
        Criterio("¿Como de superior es el criterio colaboración respecto al criterio E.Riesgos?", 1, 2,7),
        Criterio("¿Como de superior es el criterio colaboración respecto al criterio V.Gráfica?", 1, 3,1),
        Criterio("¿Como de superior es el criterio E.riesgos respecto al criterio V.Gráfica?", 2, 3,5)
    ]

    matrizProgramacionTareas = [
        Criterio("¿Como de superior es la alternativa T1 para P.Tareas respecto a la alternativa T2?", 0, 1,-6),
        Criterio("¿Como de superior es la alternativa T1 para P.Tareas respecto a la alternativa T3?", 0, 2,6),
        Criterio("¿Como de superior es la alternativa T2 para P.Tareas respecto a la alternativa T3?", 1, 2,4)
    ]

    matrizColaboracion = [
        Criterio("¿Como de superior es la alternativa T1 para colaboración respecto a la alternativa T2?", 0, 1,5),
        Criterio("¿Como de superior es la alternativa T1 para colaboración respecto a la alternativa T3?", 0, 2,2),
        Criterio("¿Como de superior es la alternativa T2 para colaboración respecto a la alternativa T3?", 1, 2, -7)
    ]

    matrizEvaluacionRiesgos = [
        Criterio("¿Como de superior es la alternativa T1 para E.Riesgos respecto a la alternativa T2?", 0, 1,-4),
        Criterio("¿Como de superior es la alternativa T1 para E.Riesgos respecto a la alternativa T3?", 0, 2,-2),
        Criterio("¿Como de superior es la alternativa T2 para E.Riesgos respecto a la alternativa T3?", 1, 2,4)
    ]

    matrizVisualizacionGrafica = [
        Criterio("¿Como de superior es la alternativa T1 para V.Gráfica respecto a la alternativa T2?", 0, 1,-5),
        Criterio("¿Como de superior es la alternativa T1 para V.Gráfica respecto a la alternativa T3?", 0, 2,-2),
        Criterio("¿Como de superior es la alternativa T2 para V.Gráfica respecto a la alternativa T3?", 1, 2,1)
    ]

    ###########################################################################################################################################################
    ###########################################################################################################################################################
    ###########################################################################################################################################################
    ###########################################################################################################################################################

    matrizCriterios3 = [
        Criterio("¿Como de importante es el liderazgo respecto a la adaptabilidad?",0, 1,-3),
        Criterio("¿Como de importante es el liderazgo respecto al potencial?", 0, 2,-6),
        Criterio("¿Como de importante es el liderazgo respecto a los goles?", 0, 3,-9),
        Criterio("¿Como de importante es el liderazgo respecto a las asistencias?", 0, 4,-8),
        Criterio("¿Como de importante es la adaptabilidad respecto al potencial?", 1, 2,-3),
        Criterio("¿Como de importante es la adaptabilidad respecto a los goles?", 1, 3,-6),
        Criterio("¿Como de importante es la adaptabilidad respecto a las asistencias?", 1, 4,-5),
        Criterio("¿Como de importantes es el potencial respecto a los goles?", 2, 3,-3),
        Criterio("¿Como de importantes es el potencial respecto a las asistencias?", 2, 4,-2),
        Criterio("¿Como de importantes son los goles respecto a las asistencias?", 3, 4,1)
    ]

    matrizPotencial = [15,11,10,13]

    matrizGoles = [12,11,10,16]

    matrizAsist = [8,1,6,10]

    matrizconjunta = [matrizPotencial,matrizGoles,matrizAsist]

    matrizLiderazgo = [
        Criterio("¿Como de superior es un liderazgo medio respecto a un liderazgo alto?", 0, 1,-5),
        Criterio("¿Como de superior es un liderazgo medio respecto a un liderazgo alto?", 0, 2,-5),
        Criterio("¿Como de superior es un liderazgo medio respecto a un liderazgo alto", 0, 3,-5),
        Criterio("¿Como de superior es un liderazgo alto respecto a un liderazgo alto", 1, 2,1),
        Criterio("¿Como de superior es un liderazgo alto respecto a un liderazgo alto", 1, 3,1),
        Criterio("¿Como de superior es un liderazgo alto respecto a un liderazgo alto", 2, 3,1)
    ]

    matrizAdaptabilidad = [
        Criterio("¿Como de superior es una adaptabilidad media respecto a una adaptabilidad media?", 0, 1,1),
        Criterio("¿Como de superior es una adaptabilidad media respecto a una adaptabilidad alta?", 0, 2,-5),
        Criterio("¿Como de superior es un adaptabilidad media respecto a una adaptabilidad alta?", 0, 3,-5),
        Criterio("¿Como de superior es un adaptabilidad media respecto a una adaptabilidad alta?", 1, 2,-5),
        Criterio("¿Como de superior es un adaptabilidad media respecto a una adaptabilidad alta?", 1, 3,-5),
        Criterio("¿Como de superior es un adaptabilidad alta respecto a una adaptabilidad alta?", 2, 3,1)
    ]

    ListaMatrices1 = {"Comparación criterios":matrizCriterios,"Comparación de compradores":matrizCompradores,"Comparación de visibilidad":matrizVisibilidad,"Comparación de competencia":matrizCompetencia,"Comparación de costo":matrizCosto}
    ListaMatrices2 = {"Comparación criterios":matrizCriterios2,"Comparación de programación de tareas":matrizProgramacionTareas,"Comparación de colaboracion":matrizColaboracion,"Comparación de evaluación de riesgos":matrizEvaluacionRiesgos,"Comparación de visualización":matrizVisualizacionGrafica}
    ListaMatrices3 = {"Comparación criterios":matrizCriterios3,"Comparación de liderazgo":matrizLiderazgo,"Comparación de adaptabilidad":matrizAdaptabilidad}

    root = tk.Tk()
    app1 = AppComparacionAHP(root, ListaMatrices1)

    ventana_secundaria = tk.Toplevel(root)
    app2 = AppComparacionAHP(ventana_secundaria, ListaMatrices2)

    ventana_terciaria = tk.Toplevel(ventana_secundaria)
    app3 = AppComparacionAHP(ventana_terciaria, ListaMatrices3,matrizconjunta)
    root.mainloop()

