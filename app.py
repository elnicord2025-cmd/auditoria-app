from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        auditoria = request.form.get("auditoria")
        procedimientos = int(request.form.get("procedimientos"))

        total = 0
        scores = []

        # Procedimientos
        for i in range(1, procedimientos + 1):
            val = int(request.form.get(f"proc{i}", 0))
            total += val
            scores.append(val)

        # Factores
        calidad = int(request.form.get("calidad", 0))
        entrega = int(request.form.get("entrega", 0))

        total += calidad + entrega

        divisor = procedimientos + 2
        promedio = total / divisor

        # Clasificación
        if promedio >= 3.51:
            nivel = "BUENO"
            color = "green"
        elif promedio >= 3.01:
            nivel = "SATISFACTORIO"
            color = "orange"
        elif promedio >= 2.51:
            nivel = "PARCIALMENTE SATISFACTORIO"
            color = "yellow"
        else:
            nivel = "NO SATISFACTORIO"
            color = "red"

        resultado = {
            "auditoria": auditoria,
            "promedio": round(promedio, 2),
            "nivel": nivel,
            "color": color,
            "scores": scores,
            "calidad": calidad,
            "entrega": entrega
        }

    return render_template("index.html", resultado=resultado)