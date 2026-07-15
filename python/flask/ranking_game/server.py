from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
   {"nombre": "AlexGamer", "puntaje": 5000},
   {"nombre": "PixelMaster", "puntaje": 7500},
   {"nombre": "ShadowNinja", "puntaje": 8200},
   {"nombre": "CyberWarrior", "puntaje": 9100},
   {"nombre": "UltraNoob", "puntaje": 3000}
]


# Ruta para mostrar el ranking de jugadores
@app.route('/ranking')
def ranking_completo():
    # Ordena de mayor a menor usando el puntaje
    lista_ordenada = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    return render_template('ranking.html', jugadores=lista_ordenada)
# Ruta para mostrar un número limitado de jugadores
@app.route('/ranking/3')
def ranking_top():
    lista_ordenada = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    top_tres = lista_ordenada[:3]  # Toma solo los 3 mejores
    return render_template('ranking.html', jugadores=top_tres)
# Ruta para personalizar el color del ranking
@app.route('/ranking/3/<string:color_elegido>')
def ranking_color_variable(color_elegido):
    lista_ordenada = sorted(jugadores, key=lambda x: x['puntaje'], reverse=True)
    top_tres = lista_ordenada[:3]
    # Pasa el color que el usuario escribió en la URL directamente al HTML
    return render_template('ranking.html', jugadores=top_tres, color=color_elegido)
# Ejecutar el servidor
if __name__ == "__main__":
   app.run(debug=True)