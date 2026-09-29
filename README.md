# Proyecto CC4401 · Equipo 5

Aplicación web desarrollada en Django para el curso **CC4401 Ingeniería de Software**
(FCFM, Universidad de Chile, Primavera 2026).

> **Tema del proyecto:** _por completar_

## Requisitos

- **Python 3.10.** Django 3.2 es compatible solo hasta Python 3.10.
  En macOS se instala con `brew install python@3.10`; en Windows, desde [python.org](https://www.python.org/downloads/).
- Git

## Cómo levantar el proyecto

1. Clonar el repositorio y entrar a la carpeta:

   ```bash
   git clone https://github.com/juxinxu1/cc4401-equipo5.git
   cd cc4401-equipo5
   ```

2. Crear y activar un entorno virtual con Python 3.10:

   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate           # Windows
   ```

3. Instalar las dependencias (Django 3.2.25, la versión usada en los auxiliares):

   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones y levantar el servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Abrir <http://127.0.0.1:8000/> en el navegador.

Para entrar al panel de administración (`/admin/`), crea antes una cuenta con
`python manage.py createsuperuser`.

## Pruebas

```bash
python manage.py test
```

## Estructura

```
cc4401-equipo5/
├── config/                 # Configuración del proyecto (settings, urls, wsgi)
├── core/                   # Páginas generales del sitio
│   ├── templates/core/     # base.html (plantilla común) e inicio.html
│   └── static/core/        # estilos.css
├── usuarios/               # Cuentas de usuario
│   ├── models.py           # User propio: agrega apodo y pronombres
│   ├── forms.py            # Formulario de registro
│   └── templates/usuarios/ # registro.html y login.html
├── manage.py
└── requirements.txt
```

### Páginas disponibles

| Ruta                 | Página                          |
|----------------------|---------------------------------|
| `/`                  | Inicio                          |
| `/cuentas/registro/` | Crear cuenta                    |
| `/cuentas/ingresar/` | Iniciar sesión                  |
| `/cuentas/salir/`    | Cerrar sesión (botón en la barra) |
| `/admin/`            | Panel de administración         |

## Forma de trabajo

- Cada tarea del sprint se registra como un *issue* en GitHub.
- Se trabaja en una rama por tarea y se integra a `main` mediante *pull request*.
- Commits pequeños y con mensajes descriptivos (ej. `Agrega formulario de registro de usuarios`).
- Todos los modelos y views llevan un comentario que explica qué hacen.
- Si agregas una dependencia, actualiza `requirements.txt` con `pip freeze > requirements.txt`.

## Integrantes

_Por completar con los nombres del equipo._
