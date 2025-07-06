# Todo List - Flask

Una aplicación simple de lista de tareas desarrollada con Flask y SQLAlchemy.

## Características

- ✅ **Crear** nuevas tareas
- 📖 **Leer** y visualizar todas las tareas
- ✏️ **Actualizar** tareas existentes
- 🗑️ **Eliminar** tareas
- ✅ Marcar tareas como completadas/pendientes
- 📱 Interfaz responsive con Bootstrap

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:
```bash
python app.py
```

3. Abre tu navegador y ve a: `http://localhost:5000`

## Uso

- **Página principal**: Muestra todas las tareas con opciones para completar, editar o eliminar
- **Agregar tarea**: Formulario para crear nuevas tareas con título y descripción opcional
- **Editar tarea**: Modificar tareas existentes y cambiar su estado
- **Eliminar tarea**: Remover tareas permanentemente (con confirmación)

## Estructura del proyecto

```
todo-list/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias
├── todolist.db        # Base de datos SQLite (se crea automáticamente)
└── templates/          # Plantillas HTML
    ├── base.html       # Plantilla base
    ├── index.html      # Página principal
    ├── add_todo.html   # Formulario para agregar
    └── edit_todo.html  # Formulario para editar
```
