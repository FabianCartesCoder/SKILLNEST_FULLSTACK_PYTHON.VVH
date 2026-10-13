




from flask import Flask, render_template

from mascota import Mascota
from usr_data import Usuario






app = Flask(__name__)






@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de info
    y las envía hacia la plantilla HTML.
    """

    
    
    

    mascotas = Mascota.get_all()


    
    
    

    print(mascotas)





    usr_list = Usuario.get_all()

    print(usr_list)

    print(Mascota.get_by_id(3))
    
    
    

    return render_template(
        "index.html",
        mascotas=mascotas,
        usr_list=usr_list
    )






if __name__ == "__main__":

    app.run(debug=True)