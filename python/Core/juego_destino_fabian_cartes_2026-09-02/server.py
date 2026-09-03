import random
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

# Listas de palabras aceptadas (incluyen variaciones con/sin tilde)
COLORES_PERMITIDOS = [
    "rojo", "azul", "verde", "morado", "amarillo", "rosa", "rosado", 
    "naranja", "negro", "blanco", "violeta", "gris", "turquesa", "marrón", "marron"
]

ANIMALES_PERMITIDOS = [
    "perro", "gato", "águila", "aguila", "león", "leon", "delfín", "delfin", 
    "lobo", "oso", "tigre", "caballo", "serpiente", "zorro", "búho", "buho"
]

PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Grandes cambios profesionales se aproximan. Mantén la mente abierta a nuevas aventuras.",
    "Un viaje inesperado te revelará un secreto valioso sobre tu futuro.",
    "La fortuna tocará a tu puerta pronto; mantén la constancia en tus proyectos."
]

AFINIDADES_COLOR = {
    "rojo": "pasión y determinación.",
    "azul": "serenidad y sabiduría.",
    "verde": "misterio y descubrimiento.",
    "morado": "espiritualidad e intuición.",
    "amarillo": "energía y creatividad.",
    "rosa": "afecto y sensibilidad.",
    "rosado": "afecto y sensibilidad.",
    "naranja": "entusiasmo y vitalidad.",
    "negro": "misterio y elegancia.",
    "blanco": "pureza y claridad.",
    "violeta": "transformación y magia.",
    "gris": "equilibrio y neutralidad.",
    "turquesa": "renovación y tranquilidad.",
    "marrón": "estabilidad y conexión.",
    "marron": "estabilidad y conexión."
}

SIMBOLOS_ANIMAL = {
    "perro": "lealtad y protección.",
    "gato": "independencia y misterio.",
    "águila": "visión y libertad.",
    "aguila": "visión y libertad.",
    "león": "fuerza y liderazgo.",
    "leon": "fuerza y liderazgo.",
    "delfín": "inteligencia y empatía.",
    "delfin": "inteligencia y empatía.",
    "lobo": "astucia y trabajo en equipo.",
    "oso": "fortaleza y calma.",
    "tigre": "valentía y poder.",
    "caballo": "libertad y nobleza.",
    "serpiente": "sabiduría y transformación.",
    "zorro": "agudeza mental y adaptación.",
    "búho": "intuición y conocimiento.",
    "buho": "intuición y conocimiento."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre", "").strip()
    edad = request.form.get("edad", "").strip()
    color = request.form.get("color", "").strip().lower()
    animal = request.form.get("animal", "").strip().lower()
    
    # Validar color ingresado
    if color not in COLORES_PERMITIDOS:
        flash("El color ingresado no es válido. Ejemplos válidos: rojo, azul, verde, morado, amarillo...")
        return redirect(url_for("index"))
        
    # Validar animal ingresado
    if animal not in ANIMALES_PERMITIDOS:
        flash("El animal ingresado no es válido. Ejemplos válidos: perro, gato, águila, león, delfín...")
        return redirect(url_for("index"))

    session["nombre"] = nombre
    session["edad"] = edad
    session["color"] = color
    session["animal"] = animal
    session["numero_suerte"] = random.randint(1, 99)
    session["prediccion"] = random.choice(PREDICCIONES)
    
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))
    
    color_input = session.get("color", "")
    animal_input = session.get("animal", "")

    afinidad_color = AFINIDADES_COLOR.get(color_input, "armonía y equilibrio.")
    simbolo_animal = SIMBOLOS_ANIMAL.get(animal_input, "fortaleza y destreza.")

    return render_template(
        "futuro.html",
        nombre=session.get("nombre"),
        edad=session.get("edad"),
        color=color_input,
        animal=animal_input,
        numero=session.get("numero_suerte"),
        prediccion=session.get("prediccion"),
        afinidad_color=afinidad_color,
        simbolo_animal=simbolo_animal
    )

if __name__ == "__main__":
    app.run(debug=True)