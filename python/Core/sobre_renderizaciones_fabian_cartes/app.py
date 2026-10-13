from flask import Flask, render_template

app = Flask(__name__)


info = [
    {"nombre": "Spotify", "usr_list": "515M", "fundado": "2006", "pais": "Suecia"},
    {"nombre": "Netflix", "usr_list": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usr_list": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usr_list": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "TikTok", "usr_list": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "Instagram", "usr_list": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "Discord", "usr_list": "250M", "fundado": "2015", "pais": "EE.UU."},
]


@app.route("/tablas")
def inicio():
    apps = [
        {
            "nombre": "Discord",
            "usr_list": "250M",
            "fundacion": 2015,
            "pais": "EE.UU.",
        },
        {
            "nombre": "Instagram",
            "usr_list": "2.35B",
            "fundacion": 2010,
            "pais": "EE.UU.",
        },
        {"nombre": "Netflix", "usr_list": "247M", "fundacion": 1997, "pais": "EE.UU."},
        {"nombre": "Spotify", "usr_list": "515M", "fundacion": 2006, "pais": "Suecia"},
        {"nombre": "TikTok", "usr_list": "1.7B", "fundacion": 2016, "pais": "China"},
        {"nombre": "Twitch", "usr_list": "140M", "fundacion": 2011, "pais": "EE.UU."},
        {
            "nombre": "YouTube",
            "usr_list": "2.5B",
            "fundacion": 2005,
            "pais": "EE.UU.",
        },
    ]

    return render_template("tablas.html", lista_apps=apps)

if __name__ == "__main__":
    app.run(debug=True)