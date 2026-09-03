# 👀 Visitas — Sesiones en Flask

> **Curso:** Desarrollo Web con Flask desde Cero  
> **Actividad:** Visitas — Core + Bonus  
> **Tecnologías:** Python · Flask · Jinja2 · HTML · CSS

---

## 📖 Descripción

Esta aplicación permite contabilizar la cantidad de veces que un cliente ha visitado una página utilizando **sesiones (`session`) de Flask**.

Además del contador principal, la aplicación implementa las funcionalidades solicitadas en los distintos niveles de la actividad:

- Contador de visitas.
- Eliminación completa de la sesión.
- Incremento manual de `+2`.
- Reinicio del contador.
- Incremento mediante un formulario.
- Registro de la cantidad de veces que se ha reiniciado el contador.

El objetivo principal es comprender cómo Flask puede **mantener información entre distintas solicitudes HTTP**.

---

# 🎯 Objetivos

Al finalizar la actividad se debe comprender y aplicar:

- `session`.
- `app.secret_key`.
- Comprobación de propiedades dentro de una sesión.
- Inicialización de valores.
- Modificación de valores en sesión.
- `session.clear()`.
- `session.pop()`.
- Formularios `POST`.
- `request.form`.
- `redirect()`.
- `url_for()`.
- Renderizado de información mediante Jinja2.

---

# 📁 Estructura final del proyecto

```text
visitas/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

---

# 🐍 `app.py`

El servidor contiene toda la lógica relacionada con las sesiones y las distintas acciones disponibles para el usuario.

```python
# ==========================================================
# VISITAS - SESIONES EN FLASK
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)


# ==========================================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# SECRET KEY
# ==========================================================
#
# Flask necesita una clave secreta para utilizar session.
#
# Esta clave permite firmar y proteger la información
# asociada a la sesión.
#
# En una aplicación real no deberíamos dejar una clave
# sensible escrita directamente en el código fuente.
#
# Para esta actividad utilizamos una clave únicamente
# con fines educativos.
# ==========================================================

app.secret_key = "clave-secreta-visitas"


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra la cantidad de visitas del usuario.

    Cada vez que se accede a esta ruta se considera
    una nueva visita.
    """

    # ------------------------------------------------------
    # COMPROBAR SI EXISTE EL CONTADOR
    # ------------------------------------------------------

    if "visitas" in session:

        # Si ya existe, aumentamos una visita.

        session["visitas"] += 1

    else:

        # Si no existe, inicializamos el contador.

        session["visitas"] = 1


    # ------------------------------------------------------
    # INICIALIZAR CONTADOR DE REINICIOS
    # ------------------------------------------------------

    if "reinicios" not in session:

        session["reinicios"] = 0


    # ------------------------------------------------------
    # ENVIAR INFORMACIÓN A LA PLANTILLA
    # ------------------------------------------------------

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


# ==========================================================
# AUMENTAR VISITAS EN 2
# ==========================================================

@app.route("/sumar_dos")
def sumar_dos():
    """
    Aumenta el contador de visitas en dos unidades.
    """

    # Si no existe el contador, lo inicializamos.

    if "visitas" not in session:

        session["visitas"] = 0


    # Aumentamos la cantidad en dos.

    session["visitas"] += 2


    # Volvemos a la página principal.

    return redirect(url_for("index"))


# ==========================================================
# REINICIAR CONTADOR
# ==========================================================

@app.route("/reiniciar")
def reiniciar():
    """
    Reinicia el contador de visitas.

    Además registra que se realizó un reinicio.
    """

    # ------------------------------------------------------
    # ASEGURAR QUE EXISTA EL CONTADOR DE REINICIOS
    # ------------------------------------------------------

    if "reinicios" not in session:

        session["reinicios"] = 0


    # Registrar un nuevo reinicio.

    session["reinicios"] += 1


    # Reiniciar contador de visitas.

    session["visitas"] = 0


    # Volver a la página principal.

    return redirect(url_for("index"))


# ==========================================================
# SUMAR UNA CANTIDAD PERSONALIZADA
# ==========================================================

@app.route("/sumar", methods=["POST"])
def sumar():
    """
    Recibe una cantidad desde un formulario
    y la agrega al contador de visitas.
    """

    # ------------------------------------------------------
    # OBTENER INFORMACIÓN DEL FORMULARIO
    # ------------------------------------------------------

    cantidad = int(
        request.form["cantidad"]
    )


    # ------------------------------------------------------
    # COMPROBAR QUE EXISTA EL CONTADOR
    # ------------------------------------------------------

    if "visitas" not in session:

        session["visitas"] = 0


    # ------------------------------------------------------
    # SUMAR CANTIDAD
    # ------------------------------------------------------

    session["visitas"] += cantidad


    # ------------------------------------------------------
    # REDIRECCIONAR
    # ------------------------------------------------------

    return redirect(url_for("index"))


# ==========================================================
# DESTRUIR TODA LA SESIÓN
# ==========================================================

@app.route("/destruir_sesion")
def destruir_sesion():
    """
    Elimina todas las propiedades almacenadas
    en la sesión del usuario.
    """

    # Elimina completamente el contenido de session.

    session.clear()


    # Volvemos al inicio.

    return redirect(url_for("index"))


# ==========================================================
# EJECUTAR APLICACIÓN
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
```

---

# 🌐 Rutas disponibles

| Ruta | Método | Función |
|---|---|---|
| `/` | `GET` | Muestra y aumenta el contador |
| `/sumar_dos` | `GET` | Aumenta las visitas en `+2` |
| `/reiniciar` | `GET` | Reinicia el contador y registra el reinicio |
| `/sumar` | `POST` | Aumenta las visitas según el valor ingresado |
| `/destruir_sesion` | `GET` | Elimina toda la sesión |

---

# 🖥️ `templates/index.html`

Esta plantilla permite visualizar el estado actual de la sesión y ejecutar las distintas acciones.

```html
<!DOCTYPE html>
<html lang="es">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Contador de Visitas</title>

    <!-- Bootstrap -->

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >

    <!-- Bootstrap Icons -->

    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css"
    >

    <!-- CSS propio -->

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}"
    >

</head>

<body>


<div class="container">

    <div class="visitas-card">

        <div class="icono">

            <i class="bi bi-eye-fill"></i>

        </div>


        <h1>

            Contador de Visitas

        </h1>


        <p class="descripcion">

            Seguimiento de visitas mediante
            sesiones de Flask.

        </p>


        <!-- ==================================================
             CONTADOR
        =================================================== -->

        <div class="contador">

            <span>

                {{ visitas }}

            </span>

        </div>


        <p class="texto-visitas">

            {% if visitas == 1 %}

                Has visitado esta página 1 vez.

            {% else %}

                Has visitado esta página
                {{ visitas }} veces.

            {% endif %}

        </p>


        <!-- ==================================================
             BOTONES
        =================================================== -->

        <div class="acciones">

            <a
                href="{{ url_for('sumar_dos') }}"
                class="btn btn-primary"
            >

                <i class="bi bi-plus-circle"></i>

                Sumar +2

            </a>


            <a
                href="{{ url_for('reiniciar') }}"
                class="btn btn-warning"
            >

                <i class="bi bi-arrow-counterclockwise"></i>

                Reiniciar

            </a>

        </div>


        <!-- ==================================================
             FORMULARIO PERSONALIZADO
        =================================================== -->

        <div class="formulario">

            <h3>

                Agregar visitas

            </h3>


            <form
                action="{{ url_for('sumar') }}"
                method="POST"
            >

                <div class="input-group">

                    <input
                        type="number"
                        name="cantidad"
                        min="1"
                        class="form-control"
                        placeholder="Ingresa una cantidad"
                        required
                    >

                    <button
                        type="submit"
                        class="btn btn-success"
                    >

                        <i class="bi bi-plus-lg"></i>

                        Agregar

                    </button>

                </div>

            </form>

        </div>


        <!-- ==================================================
             REINICIOS
        =================================================== -->

        <div class="reinicios">

            <i class="bi bi-arrow-repeat"></i>

            Contador reiniciado:

            <strong>

                {{ reinicios }}

            </strong>

            veces.

        </div>


        <!-- ==================================================
             DESTRUIR SESIÓN
        =================================================== -->

        <div class="destruir">

            <a
                href="{{ url_for('destruir_sesion') }}"
                class="btn btn-outline-danger"
            >

                <i class="bi bi-trash3-fill"></i>

                Destruir sesión

            </a>

        </div>

    </div>

</div>


</body>

</html>
```

---

# 🎨 `static/css/style.css`

```css
/* ==========================================================
   CONTADOR DE VISITAS
   ========================================================== */


/* ==========================================================
   VARIABLES
   ========================================================== */

:root {
    --color-primary: #0d6efd;
    --color-success: #198754;
    --color-warning: #ffc107;
    --color-danger: #dc3545;
    --color-background: #f4f7fb;
    --color-text: #212529;
}


/* ==========================================================
   CONFIGURACIÓN GENERAL
   ========================================================== */

body {
    min-height: 100vh;
    background: linear-gradient(135deg, #eef4ff, #f8f9fa);
    font-family: Arial, Helvetica, sans-serif;
    color: var(--color-text);
    display: flex;
    align-items: center;
}


/* ==========================================================
   TARJETA PRINCIPAL
   ========================================================== */

.visitas-card {
    max-width: 650px;
    margin: 60px auto;
    padding: 50px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
    text-align: center;
}


/* ==========================================================
   ICONO
   ========================================================== */

.icono {
    width: 80px;
    height: 80px;
    margin: 0 auto 20px;
    border-radius: 50%;
    background: #e7f0ff;
    color: var(--color-primary);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 36px;
}


/* ==========================================================
   TÍTULO
   ========================================================== */

.visitas-card h1 {
    font-weight: bold;
    margin-bottom: 10px;
}


.descripcion {
    color: #6c757d;
    margin-bottom: 30px;
}


/* ==========================================================
   CONTADOR
   ========================================================== */

.contador {
    width: 180px;
    height: 180px;
    margin: 0 auto 20px;
    border-radius: 50%;
    background: var(--color-primary);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 10px 25px rgba(13, 110, 253, 0.3);
}


.contador span {
    font-size: 64px;
    font-weight: bold;
}


.texto-visitas {
    font-size: 18px;
    color: #495057;
}


/* ==========================================================
   BOTONES
   ========================================================== */

.acciones {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin: 30px 0;
    flex-wrap: wrap;
}


.btn {
    border-radius: 10px;
    font-weight: bold;
}


/* ==========================================================
   FORMULARIO
   ========================================================== */

.formulario {
    margin-top: 30px;
    padding: 25px;
    background: #f8f9fa;
    border-radius: 15px;
}


.formulario h3 {
    margin-bottom: 20px;
}


.form-control {
    border-radius: 8px;
}


.input-group .form-control {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}


.input-group .btn {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}


/* ==========================================================
   CONTADOR DE REINICIOS
   ========================================================== */

.reinicios {
    margin-top: 25px;
    padding: 15px;
    background: #fff8e1;
    border-radius: 10px;
    color: #856404;
}


.reinicios strong {
    font-size: 20px;
}


/* ==========================================================
   DESTRUIR SESIÓN
   ========================================================== */

.destruir {
    margin-top: 25px;
}


/* ==========================================================
   RESPONSIVE
   ========================================================== */

@media (max-width: 576px) {

    body {
        display: block;
    }


    .visitas-card {
        margin: 25px 15px;
        padding: 30px 20px;
    }


    .contador {
        width: 140px;
        height: 140px;
    }


    .contador span {
        font-size: 48px;
    }


    .acciones {
        flex-direction: column;
    }


    .acciones .btn {
        width: 100%;
    }

}
```

---

# 🔍 Conceptos fundamentales

## `app.secret_key`

```python
app.secret_key = "clave-secreta-visitas"
```

Es necesaria para utilizar `session`.

Flask utiliza esta clave para firmar la información asociada a la sesión.

En producción debe utilizarse una clave segura y almacenada fuera del código fuente.

---

# 🧠 `session`

La sesión funciona de manera similar a un diccionario:

```python
session["visitas"] = 1
```

Podemos guardar información:

```python
session["nombre"] = "Dany"
```

Modificarla:

```python
session["visitas"] += 1
```

Y recuperarla:

```python
session["visitas"]
```

---

# 🔎 Comprobar si existe información

```python
if "visitas" in session:
```

significa:

> ¿Existe una propiedad llamada `visitas` dentro de la sesión?

También podemos utilizar:

```python
if "visitas" not in session:
```

para comprobar que todavía no existe.

Esto es especialmente importante al inicializar valores.

---

# 🆕 Inicialización

La primera vez que entra el usuario:

```python
if "visitas" not in session:
    session["visitas"] = 1
```

Posteriormente:

```python
session["visitas"] += 1
```

Por lo tanto:

```text
Primera visita → 1

Segunda visita → 2

Tercera visita → 3
```

---

# 🗑️ `session.clear()`

```python
session.clear()
```

elimina todas las propiedades almacenadas.

Por ejemplo:

```python
session["visitas"] = 15
session["reinicios"] = 3
```

después:

```python
session.clear()
```

la sesión queda vacía.

---

# 🗑️ `session.pop()`

Para eliminar solamente una propiedad:

```python
session.pop("visitas", None)
```

El segundo argumento:

```python
None
```

evita que se produzca un error si la propiedad no existe.

---

# 🔄 `redirect()`

Las rutas que modifican información utilizan:

```python
return redirect(url_for("index"))
```

Por ejemplo:

```text
/sumar_dos
      ↓
modifica session
      ↓
redirect
      ↓
/
```

Esto permite volver a la página principal después de ejecutar la acción.

---

# 📨 POST + `request.form`

El formulario utiliza:

```html
<form
    action="{{ url_for('sumar') }}"
    method="POST"
>
```

Por eso Flask tiene:

```python
@app.route("/sumar", methods=["POST"])
```

El valor ingresado se obtiene mediante:

```python
request.form["cantidad"]
```

Como los formularios entregan los valores como texto, se convierte:

```python
int(request.form["cantidad"])
```

Por ejemplo:

```text
"5"
```

se convierte en:

```python
5
```

---

# 🔄 Flujo completo

## Visita normal

```text
GET /
 ↓
¿Existe session["visitas"]?
 ↓
NO → crear = 1
 ↓
render_template()
 ↓
HTML
```

En una visita posterior:

```text
GET /
 ↓
session["visitas"] existe
 ↓
+= 1
 ↓
render_template()
```

---

## Botón `+2`

```text
GET /sumar_dos
 ↓
session["visitas"] += 2
 ↓
redirect("/")
 ↓
GET /
 ↓
mostrar contador
```

---

## Reiniciar

```text
GET /reiniciar
 ↓
session["reinicios"] += 1
 ↓
session["visitas"] = 0
 ↓
redirect("/")
 ↓
GET /
```

---

## Formulario personalizado

```text
POST /sumar
 ↓
request.form["cantidad"]
 ↓
int()
 ↓
session["visitas"] += cantidad
 ↓
redirect("/")
 ↓
GET /
```

---

## Destruir sesión

```text
GET /destruir_sesion
 ↓
session.clear()
 ↓
redirect("/")
 ↓
GET /
 ↓
session["visitas"] vuelve a inicializarse
```

---

# ✅ Requisitos cumplidos

## Nivel 1

- ✅ Mostrar cantidad de visitas.
- ✅ Crear `/destruir_sesion`.
- ✅ Eliminar sesión.
- ✅ Redireccionar al inicio.

## Nivel 2

- ✅ Botón `+2`.
- ✅ Botón para reiniciar el contador.

## Nivel 3

- ✅ Formulario para ingresar cualquier cantidad.
- ✅ Sumar cantidad personalizada.
- ✅ Contabilizar reinicios.
- ✅ Mostrar cantidad de reinicios.

---

# 🧪 Comportamiento esperado

Al entrar por primera vez:

```text
Contador de Visitas

        1

Has visitado esta página 1 vez.
```

Después de actualizar:

```text
        2

Has visitado esta página 2 veces.
```

Después de utilizar `+2`:

```text
        4
```

Después de reiniciar:

```text
        0

Contador reiniciado: 1 vez.
```

Si posteriormente se vuelve a visitar `/`:

```text
        1

Contador reiniciado: 1 vez.
```

---

# 💡 Consideración sobre el reinicio

En esta implementación, cuando se ejecuta:

```python
session["visitas"] = 0
```

el contador queda efectivamente en `0`.

Después, al entrar nuevamente a `/`, se ejecuta:

```python
session["visitas"] += 1
```

por lo que la visita siguiente será:

```text
1
```

Esto es consistente con la idea de que **el acceso a `/` representa una nueva visita**.

---

# 🏁 Resultado final

La aplicación integra en un solo proyecto:

```text
                    FLASK
                      │
                      ▼
                   session
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
     visitas       reinicios      acciones
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
                 Jinja2 / HTML
                      │
                      ▼
                  Navegador
```

El proyecto demuestra cómo Flask puede mantener información relacionada con un usuario entre diferentes solicitudes y cómo combinar **sesiones, formularios POST, `request.form`, `redirect()` y Jinja2** para construir una aplicación web interactiva.