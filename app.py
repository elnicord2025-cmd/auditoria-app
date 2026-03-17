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
    # ... puedes seguir hasta 64
    64: "Auditoría completada"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        auditoria = request.form.get("auditoria")
        tipo = request.form.get("tipo")

        if tipo == "numero":
            num = int(request.form.get("numero", 0))
            if 1 <= num <= TOTAL:
                porc = round((num / TOTAL) * 100)
                resultado = {
                    "auditoria": auditoria,
                    "paso": num,
                    "descripcion": steps.get(num, "Sin definir"),
                    "avance": porc,
                    "fecha": datetime.datetime.now()
                }

        elif tipo == "texto":
            texto = request.form.get("texto", "").lower()
            encontrado = None

            for i in range(1, TOTAL + 1):
                if texto in steps.get(i, "").lower():
                    encontrado = i
                    break

            if encontrado:
                porc = round((encontrado / TOTAL) * 100)
                resultado = {
                    "auditoria": auditoria,
                    "paso": encontrado,
                    "descripcion": steps[encontrado],
                    "avance": porc,
                    "fecha": datetime.datetime.now()
                }

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)