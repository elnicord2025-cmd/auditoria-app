from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

TOTAL = 64

steps = {
    1: "Elegir la auditoria por el plan anual de auditorias",
2: "Elegir equipo de la auditoria",
3: "Crear grupo en teams de la auditoria",
4: "Enviar informes de antecedentes",
5: "Verificar incidentes abiertas o en seguimiento TeamMate",
6: "Crear proyecto en teamMate para asignar horas",
7: "Definir objetivos de la auditoria",
8: "Definir alcance de la auditoria",
9: "Socializar alcance y objetivos",
10: "Crear carta auditoria con alcance y objetivos",
11: "Solicitar reunion de kickoff - inicio de la auditoria",
12: "Preparar presentacion del kickoff - inicio de la auditoria",
13: "Socializar presentacion de kickoff",
14: "Gerente de auditoria envia carta de inicio de la auditoria",
15: "Preparar requerimientos para enviar al area",
16: "Envio de requerimientos a las areas de la auditoria",
17: "En espera de recepcion de requerimientos - SLA - 3 dias laborables",
18: "Parcialmente recibidos los requerimientos de las areas",
19: "Respuesta inicial de requerimientos remitidos de las areas",
20: "Verificando items pendientes con areas (post-respuesta) evidencias",
21: "Revisión inicial de las evidencias solicitadas - Trabajo de Campo",
22: "Organización y clasificación de las evidencias por procesos o controles - Trabajo de Campo",
23: "Realización de entrevistas y walkthroughs con el personal responsable - Trabajo de Campo",
24: "Evaluación controles de TI sobre de las evidencias - Trabajo de Campo",
25: "Ejecución de pruebas de los control - Trabajo de Campo",
26: "Análisis preliminar de los resultados de las pruebas realizadas - Trabajo de Campo",
27: "Identificacion y solicitud formal de evidencias adicionales requeridas - Trabajo de Campo",
28: "Recepcion y análisis de las evidencias complementarias obtenidas - Trabajo de Campo",
29: "Identificacion y registro preliminar de hallazgos y desviaciones - Trabajo de Campo",
30: "Validación de los hallazgos con el área auditada - Trabajo de Campo",
31: "Borradores de Formularios sobre de conclusiones y recomendaciones preliminares - Trabajo de Campo",
32: "Revision interna (Equipo Auditoria) comparativa antescedentes Hallazgos- Trabajo de Campo",
33: "Socializando evidencias recibidas por los auditados - reuniones - Trabajo de Campo",
34: "En espera de nuevas evidencias luego del trabajo de campo",
35: "Documentando incidencias encontradas en la matriz de formularios",
36: "Parcialmente documentadas las incidencias en la matriz de formularios",
37: "Enviada la matriz de formularios para aprobacion de gerente del area de auditoria",
38: "Enviada la matriz de formularios para aprobacion del director del area de auditoria",
39: "Socializando formularios con gerente y director de auditoria",
40: "Pasando los formularios al formato estandar local luego de aprobados",
41: "Reunion de presentacion de formularios con el area auditada",
42: "Socializacion y/o cambios en formularios luego de reunion con el area auditada",
43: "Actualizando documento de formularios luego de socializacion",
44: "Envio de formularios a las areas auditadas por correo",
45: "En espera de planes de accion por el area auditada - SLA - 5 dias",
46: "Verificando respuesta de planes de accion - campos completos y firmas",
47: "Preparando calificacion de riesgo final de la auditoria",
48: "Preparando presentacion de cierre final con el presidente",
49: "Actualizando formularios luego de socializacion con el presidente",
50: "En espera de cambios o planes de accion luego de cierre",
51: "Presentacion del comite de auditoria final",
52: "Actualizacion de formularios luego de socializacion con el comite",
53: "Cargar en teamMate la calificacion de riesgo final",
54: "Documentacion en teamMate de la auditoria",
55: "Parcialmente documentada la auditoria en teamMate",
56: "Elaboracion de informe borrador final para VP de auditoria interna",
57: "Envio de encuestas a los auditados luego de la auditoria",
58: "En espera de encuestas a los auditados",
59: "Preparacion del documento de calidad de la auditoria - QA Doc",
60: "Completar documentacion en teamMate luego de tener toda la documentacion",
61: "Cargar incidencias finales en teamMate y enlazarlas con planes de accion",
62: "Auditoria abierta por el comite por temas pendientes",
63: "Auditoria completada con temas de seguimiento abiertos",
64: "Auditoria completada en su totalidad sin pendientes"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        auditoria = request.form.get("auditoria")
        tipo = request.form.get("tipo")

        if tipo == "numero":
            numero = int(request.form.get("numero"))

            descripcion = pasos.get(numero, "Sin definir")

            avance = int((numero / TOTAL) * 100)

            resultado = {
                "auditoria": auditoria,
                "paso": numero,
                "descripcion": descripcion,
                "avance": avance,
                "fecha": datetime.now().strftime("%Y-%m-%d")
            }

        elif tipo == "texto":
            texto = request.form.get("texto").lower()

            encontrado = 0
            descripcion = "Sin definir"

            for i, desc in pasos.items():
                if texto in desc.lower():
                    encontrado = i
                    descripcion = desc
                    break

            if encontrado > 0:
                avance = int((encontrado / TOTAL) * 100)

                resultado = {
                    "auditoria": auditoria,
                    "paso": encontrado,
                    "descripcion": descripcion,
                    "avance": avance,
                    "fecha": datetime.now().strftime("%Y-%m-%d")
                }

    return render_template("index.html", resultado=resultado)