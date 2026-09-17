# Sistema de Gestión de Tareas

Aplicación desarrollada en **Python** como parte del caso práctico de la asignatura **Fundamentos de Ingeniería de Software**.

El sistema permite administrar tareas mediante una interfaz de línea de comandos (CLI), ofreciendo funcionalidades para crear, consultar, actualizar, eliminar y filtrar tareas según su estado.

## Funcionalidades

* Crear tareas.
* Consultar y listar tareas.
* Buscar tareas por nombre.
* Actualizar información de una tarea.
* Eliminar tareas.
* Filtrar tareas por estado.
* Validar los datos ingresados.
* Evitar tareas con nombres duplicados.

Los estados disponibles para una tarea son:

* `pendiente`
* `en progreso`
* `completada`

## Estructura del proyecto

```text
sistema_gestion_tareas/
│
├── src/
│   ├── __init__.py
│   ├── tarea.py
│   ├── gestor.py
│   └── main.py
│
├── test/
│   ├── __init__.py
│   ├── test_tarea.py
│   └── test_gestor.py
│
├── docs/
│   └── arquitectura.md
│
├── .gitignore
└── README.md
```

### Componentes principales

* **`tarea.py`**: contiene el modelo `TareaModel` y sus validaciones.
* **`gestor.py`**: administra la colección de tareas y las operaciones sobre ellas.
* **`main.py`**: contiene la interfaz de usuario mediante consola.
* **`test/`**: contiene las pruebas automatizadas del sistema.
* **`docs/`**: contiene documentación adicional relacionada con el proyecto.

## Requisitos

* Python 3.x
* No se requieren librerías externas para ejecutar el sistema o las pruebas.

## Ejecución

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

A continuación, se mostrará el menú de opciones para interactuar con el sistema.

## Ejecución de las pruebas

Para ejecutar todas las pruebas automatizadas:

```bash
python -m unittest discover -s test -p "test_*.py"
```

Las pruebas utilizan el framework estándar **`unittest`** de Python.

Para obtener información detallada de cada prueba:

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

## Pruebas

El proyecto cuenta con **16 casos de prueba** que permiten verificar el comportamiento de los principales componentes del sistema, incluyendo validaciones, creación, actualización, búsqueda, filtrado y eliminación de tareas.


El código también incluye comentarios y docstrings en las funciones y métodos principales para facilitar su comprensión y mantenimiento.
