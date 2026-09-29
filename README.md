# Proyecto CC4401 · Equipo 5

Aplicación web desarrollada en Django para el curso **CC4401 Ingeniería de Software**
(FCFM, Universidad de Chile, Primavera 2026).

> **Tema del proyecto:** _por completar_

## Requisitos

- Python 3.10 (Django 3.2 no funciona con Python 3.11 o superior)
- Git

## Cómo levantar el proyecto

1. Clonar el repositorio y entrar a la carpeta:

   ```bash
   git clone <url-del-repositorio>
   cd proyecto-cc4401
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate           # Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones y levantar el servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Abrir <http://127.0.0.1:8000/> en el navegador.

## Estructura

```
proyecto-cc4401/
├── config/            # Configuración del proyecto (settings, urls, wsgi)
├── manage.py
├── requirements.txt
└── README.md
```

## Forma de trabajo

- Cada tarea del sprint se registra como un *issue* en GitHub.
- Se trabaja en una rama por tarea y se integra a `main` mediante *pull request*.
- Commits pequeños y con mensajes descriptivos (ej. `Agrega formulario de registro de usuarios`).
- Si agregas una dependencia, actualiza `requirements.txt` con `pip freeze > requirements.txt`.

## Integrantes

_Por completar con los nombres del equipo._
