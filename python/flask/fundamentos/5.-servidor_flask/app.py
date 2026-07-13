from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return '<h1>¡Bienvenido a la Página de Inicio!</h1><p>Esta es la ruta raíz.</p>'

@app.route('/explorar')
def explorar():
    return '<h2>Explorando el enrutamiento</h2><p>Esta es una ruta fija para pruebas.</p>'

@app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    # Personaliza el saludo usando el parámetro de la URL
    return f'<h2>Perfil de Usuario</h2><p>¡Hola, {nombre}! Bienvenido a tu espacio personalizado.</p>'

@app.route("/<mensaje>/<int:veces>")
def repetir(mensaje, veces):

    return f"¡Hola {mensaje * veces}!"

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return '''
    <div style="text-align: center; margin-top: 50px;">
        <h1>Error 404</h1>
        <p>Lo sentimos, la ruta que buscas no existe en este servidor.</p>
        <a href="/">Volver al inicio</a>
    </div>
    ''', 404

if __name__ == "__main__":
    app.run(debug=True)