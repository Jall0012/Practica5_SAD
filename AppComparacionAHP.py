import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class AppComparacionAHP:
    def __init__(self, root, diccionario_criterios,criteriosNormalizados = None):
        self.root = root
        self.root.title("Evaluación Multicriterio (AHP) - Múltiples Matrices")
        self.root.geometry("850x600")
        self.criteriosNormalizados = criteriosNormalizados

        self.diccionario_criterios = diccionario_criterios
        self.respuestas_var = {}

        self.escala = [
            (9, -8, "red"), (8, -7, "red"), (7, -6, "red"), (6, -5, "red"),
            (5, -4, "red"), (4, -3, "red"), (3, -2, "red"), (2, -1, "red"),
            (1, 0, "black"),
            (2, 1, "purple"), (3, 2, "purple"), (4, 3, "purple"), (5, 4, "purple"),
            (6, 5, "purple"), (7, 6, "purple"), (8, 7, "purple"), (9, 8, "purple")
        ]

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.construir_interfaz()
        # Nota: El botón global ha sido eliminado de aquí

    def construir_interfaz(self):
        tab_instrucciones = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(tab_instrucciones, text="Instrucciones")

        # Título de las instrucciones
        lbl_titulo_inst = tk.Label(
            tab_instrucciones,
            text="Instrucciones de Evaluación Multicriterio (AHP)",
            font=("Arial", 16, "bold"),
            bg="#ffffff"
        )
        lbl_titulo_inst.pack(pady=20, padx=20, anchor="w")

        # Texto explicativo
        texto_inst = (
            "Bienvenido a la herramienta de evaluación AHP.\n\n"
            "Para cada pregunta, compare la importancia de los elementos mostrados a los lados:\n\n"
            "• Centro (1): Ambos elementos tienen exactamente la misma importancia.\n"
            "• Lado Izquierdo (Rojo): El elemento izquierdo es más importante que el derecho.\n"
            "• Lado Derecho (Morado): El elemento derecho es más importante que el izquierdo.\n\n"
            "Significado de los números (Escala de Saaty):\n"
            "  3 : Importancia moderada\n"
            "  5 : Importancia fuerte\n"
            "  7 : Importancia muy fuerte\n"
            "  9 : Importancia extrema\n"
            "  (Los números pares 2, 4, 6, 8 son valores intermedios de compromiso).\n\n"
            "IMPORTANTE: Complete todas las pestañas de evaluación. "
            "El botón para procesar\nlos resultados aparecerá al final de la última pestaña.\n"
            "En la ultima pestaña tienes un botón que muestra los resultados"
        )

        lbl_texto_inst = tk.Label(
            tab_instrucciones,
            text=texto_inst,
            font=("Arial", 11),
            bg="#ffffff",
            justify="left"
        )
        lbl_texto_inst.pack(padx=20, pady=10, anchor="w")

        total_grupos = len(self.diccionario_criterios)

        # Usamos enumerate para saber el índice (i) de la pestaña actual
        for i, (nombre_grupo, lista_criterios) in enumerate(self.diccionario_criterios.items()):

            tab_frame = tk.Frame(self.notebook, bg="#ffffff")
            self.notebook.add(tab_frame, text=nombre_grupo)

            # Si es la última pestaña, anclamos el botón en la parte inferior
            if i == total_grupos - 1:
                btn_guardar = tk.Button(
                    tab_frame,
                    text="Guardar Valoraciones y Mostrar Resultados",
                    font=("Arial", 11, "bold"),
                    bg="#4CAF50",
                    fg="white",
                    padx=10,
                    pady=8,
                    command=self.procesar_respuestas
                )
                btn_guardar.pack(side="bottom", pady=15)

            # Canvas y Scrollbar
            canvas = tk.Canvas(tab_frame, borderwidth=0, background="#ffffff")
            scrollbar = tk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, background="#ffffff")

            scrollable_frame.bind(
                "<Configure>",
                lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Empaquetamos el scroll y el canvas DESPUÉS del botón para que ocupen el resto del espacio
            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)

            lbl_titulo = tk.Label(
                scrollable_frame,
                text=f"Comparación: {nombre_grupo}",
                font=("Arial", 16, "bold"),
                bg="#ffffff"
            )
            lbl_titulo.pack(pady=15, padx=20, anchor="w")

            for idx, crit in enumerate(lista_criterios):
                frame_criterio = tk.Frame(scrollable_frame, bg="#f9f9f9", bd=1, relief="solid", padx=10, pady=10)
                frame_criterio.pack(fill="x", expand=True, padx=20, pady=10)

                lbl_pregunta = tk.Label(
                    frame_criterio,
                    text=f"{idx + 1}. {crit.pregunta}",
                    font=("Arial", 11, "bold"),
                    bg="#f9f9f9",
                    justify="left"
                )
                lbl_pregunta.pack(anchor="w", pady=(0, 10))

                frame_escala = tk.Frame(frame_criterio, bg="#ffffff", bd=1, relief="solid")
                frame_escala.pack(fill="x", expand=True)

                lbl_elem_i = tk.Label(
                    frame_escala,
                    text=f"Elemento {crit.fila}",
                    font=("Arial", 10, "italic"),
                    bg="#ffffff",
                    width=15,
                    anchor="e"
                )
                lbl_elem_i.pack(side="left", padx=5)

                valor_inicial = int(crit.media()) if hasattr(crit, 'media') else 0
                var_opcion = tk.IntVar(value=valor_inicial)

                self.respuestas_var[crit] = var_opcion

                for texto_num, valor_num, color in self.escala:
                    sub_frame = tk.Frame(frame_escala, bg="#ffffff")
                    sub_frame.pack(side="left", expand=True, fill="both")

                    rb = tk.Radiobutton(
                        sub_frame,
                        text=str(texto_num),
                        value=valor_num,
                        variable=var_opcion,
                        fg=color,
                        selectcolor="#e6e6e6",
                        font=("Arial", 10, "bold"),
                        bg="#ffffff",
                        activebackground="#ffffff",
                        indicatoron=False,
                        bd=0,
                        padx=6,
                        pady=4
                    )
                    rb.pack(padx=1, pady=1)

                lbl_elem_j = tk.Label(
                    frame_escala,
                    text=f"Elemento {crit.columna}",
                    font=("Arial", 10, "italic"),
                    bg="#ffffff",
                    width=15,
                    anchor="w"
                )
                lbl_elem_j.pack(side="right", padx=5)

    def montarMatriz(self, criterios, elementos):
        # 1. Crear matriz cuadrada de NumPy rellena de 1.0 (diagonal y por defecto)
        mediaCriterio = np.ones((elementos, elementos), dtype=float)

        # 2. Rellenar las comparaciones pareadas respetando la propiedad recíproca de AHP
        for criterio in criterios:
            med = criterio.media()
            i, j = criterio.fila, criterio.columna

            if med > 0:
                # Selección hacia la derecha (morado): Elemento j predomina sobre i
                val_ahp = 1.0 / (med + 1)
            elif med < 0:
                # Selección hacia la izquierda (rojo): Elemento i predomina sobre j
                val_ahp = float(abs(med) + 1)
            else:
                # Centro (0): Ambos son igual de importantes
                val_ahp = 1.0

            mediaCriterio[i, j] = val_ahp
            mediaCriterio[j, i] = 1.0 / val_ahp

        return mediaCriterio

    def autovalores(self,matriz):
        autovalores, autovectores = np.linalg.eig(matriz)
        return autovalores.real

    def autovectores(self,matriz):
        autovalores, autovectores = np.linalg.eig(matriz)
        return autovectores.real

    def normalizar(self,vector):
        maxVal = max(vector)
        sol = []
        for i in vector:
            sol.append(i / maxVal)
        return sol

    def indiceConsistencia(self,matriz):
        return ((np.max(self.autovalores(matriz)) - (len(matriz))) / ((len(matriz)) - 1))

    def ratioConsistencia(self,matriz):
        if len(matriz) == 3:
            R = 0.58
        elif len(matriz) == 4:
            R = 0.9
        elif len(matriz) == 5:
            R = 1.12
        elif len(matriz) == 6:
            R = 1.24
        elif len(matriz) == 7:
            R = 1.32
        elif len(matriz) == 8:
            R = 1.41
        elif len(matriz) == 9:
            R = 1.45
        elif len(matriz) == 10:
            R = 1.49
        else:
            return "Ratio Incorrecto"

        return self.indiceConsistencia(matriz)/R
    def mediageometrica(self,fila):
        x = 1
        for i in fila:
            x = i * x
        return (x)**(1/len(fila))

    def metodoaproximacion(self,matriz):
        vector = []
        solucion = []
        for linea in matriz:
            vector.append(sum(linea))
        for i in range(len(vector)):
            solucion.append(vector[i]/sum(vector))

        return solucion

    def metodoautovalores(self,matriz):
        autovectores = self.autovectores(matriz)
        autovalores = self.autovalores(matriz)

        psoicionmax = np.argmax(autovalores)

        vectorfinal = autovectores[:,psoicionmax]

        sumatorio = sum(vectorfinal)

        if sumatorio != 0:
            sol = vectorfinal/sumatorio
        else:
            sol = vectorfinal

        return np.real(sol).tolist()

    def sumatorio(self,fila):
        return sum(fila)

    def prioridadGlobal(self,criterios,elementos):
        if len(criterios) != len(elementos):
            raise ValueError("Matrices no compatibles")
        t = 0
        for i,x in zip(criterios, elementos):
            t += i * x
        return t

    def vectorRankingGeo(self, criterios, elementos,valnormalizados):
        mediaGeocriterios = []
        for cri in criterios:
            mediaGeocriterios.append(self.mediageometrica(cri))


        sumatorioGeo = sum(mediaGeocriterios)
        pesoCriterios = []

        for cri in mediaGeocriterios:
            pesoCriterios.append(cri / sumatorioGeo)


        ele = []
        for vec in elementos:
            mediaElementos = []
            for i in vec:
                mediaElementos.append(self.mediageometrica(i))

            sumatorioEle = sum(mediaElementos)
            pesoEl = []
            for i in mediaElementos:
                pesoEl.append(i / sumatorioEle)

            ele.append(pesoEl)

        if self.criteriosNormalizados is not None:
            for i in valnormalizados:
                ele.append(self.normalizar(i))

        pesosalt = list(zip(*ele))

        ar = {}
        for i, alt in enumerate(pesosalt, 1):
            ar[f"Alternativa {i}"] = self.prioridadGlobal(pesoCriterios, alt)

        sol = dict(sorted(ar.items(), key=lambda item: item[1], reverse=True))
        return  sol

    def vectorRankingAprox(self, criterios, elementos,valnormalizados):
        cr = self.metodoaproximacion(criterios)

        ele = []
        for matrices in elementos:
            ele.append(self.metodoaproximacion(matrices))

        if self.criteriosNormalizados is not None:
            for i in valnormalizados:
                ele.append(self.normalizar(i))

        pesosalt = list(zip(*ele))

        ar = {}
        for i, alt in enumerate(pesosalt, 1):
            ar[f"Alternativa {i}"] = self.prioridadGlobal(cr, alt)

        sol = dict(sorted(ar.items(), key=lambda item: item[1], reverse=True))
        return  sol

    def vectorRankingAutoval(self,criterios,elementos,valnormalizados = None):
        cr = self.metodoautovalores(criterios)

        ele = []
        for matrices in elementos:
            ele.append(self.metodoautovalores(matrices))

        if self.criteriosNormalizados is not None:
            for i in valnormalizados:
                ele.append(self.normalizar(i))

        pesosalt = list(zip(*ele))

        ar = {}
        for i, alt in enumerate(pesosalt, 1):
            x = float(self.prioridadGlobal(cr, alt))
            ar[f"Alternativa {i}"] = x

        sol = dict(sorted(ar.items(), key=lambda item: item[1], reverse=True))
        return  sol

    def procesar_respuestas(self):
        resumen = ""
        count = 0
        ele = []
        cr = np.ones(1)
        for nombre_grupo, lista_criterios in self.diccionario_criterios.items():
            resumen += f"=== {nombre_grupo} ===\n"

            # Guardar valoraciones en los objetos Criterio
            for crit in lista_criterios:
                valor_seleccionado = self.respuestas_var[crit].get()
                crit.valorar(valor_seleccionado)

            # Deducir dimensión de la matriz
            max_index = 0
            for c in lista_criterios:
                if c.fila > max_index: max_index = c.fila
                if c.columna > max_index: max_index = c.columna

            num_elementos = max_index + 1

            # Generar matriz en formato ndarray de NumPy
            matriz = self.montarMatriz(lista_criterios, num_elementos)

            if count == 0:
                cr = matriz
            else:
                ele.append(matriz)
            count = count + 1
            # Formatear la matriz NumPy con alineación limpia
            resumen += "Matriz Resultante (NumPy):\n"
            matriz_str = np.array2string(matriz, precision=3, suppress_small=True)
            resumen += matriz_str + "\n"
            resumen += "Indice de consistencia:"+ str(self.indiceConsistencia(matriz)) + "\n"
            resumen += "Ratio de consistencia:" + str(self.ratioConsistencia(matriz)) + "\n"
            if self.ratioConsistencia(matriz) >= 0.10:
                resumen += "La consistencia es inaceptable, revisa los valores" + "\n"
            else:
                resumen += "La consistencia es aceptable" + "\n"
            #resumen += "Autovalores:" + str(self.autovalores(matriz)) + "\n"
            #resumen += "Autovectores:" + str(self.autovectores(matriz)) + "\n"
            resumen += "-" * 40 + "\n\n"

        resumen += "Vector de prioridad:" + "\n"
        ranking = self.vectorRankingGeo(cr, ele,self.criteriosNormalizados)
        resumen += "Ranking media geometrica:\n"
        for alt, score in ranking.items():
             resumen += f"{alt}: {score:.4f}\n"

        ranking = self.vectorRankingAprox(cr, ele,self.criteriosNormalizados)
        resumen += "\n"
        resumen += "Ranking medida aproximada:\n"
        for alt, score in ranking.items():
            resumen += f"{alt}: {score:.4f}\n"

        ranking = self.vectorRankingAutoval(cr, ele,self.criteriosNormalizados)
        resumen += "\n"
        resumen += "Ranking media autovalor:\n"
        for alt, score in ranking.items():
            resumen += f"{alt}: {score:.4f}\n"

        # Crear ventana secundaria con scrollbar
        ventana_resultados = tk.Toplevel(self.root)
        ventana_resultados.title("Resultados Guardados")
        ventana_resultados.geometry("550x450")

        frame_texto = tk.Frame(ventana_resultados)
        frame_texto.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side="right", fill="y")

        text_area = tk.Text(frame_texto, yscrollcommand=scrollbar.set, font=("Courier", 10))
        text_area.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_area.yview)

        text_area.insert(tk.END, resumen)
        text_area.config(state="disabled")