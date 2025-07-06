import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    """Crear cliente de prueba"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_home_page(client):
    """Test que la página principal carga"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mis Tareas' in response.data

def test_add_todo_page(client):
    """Test que la página de agregar tarea carga"""
    response = client.get('/add')
    assert response.status_code == 200
    assert b'Agregar Nueva Tarea' in response.data

def test_create_todo(client):
    """Test crear una nueva tarea"""
    response = client.post('/add', data={
        'title': 'Test Task',
        'description': 'This is a test task'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Test Task' in response.data

def test_create_todo_without_title(client):
    """Test que no se puede crear tarea sin título"""
    response = client.post('/add', data={
        'description': 'Task without title'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'El t\xc3\xadtulo es obligatorio!' in response.data

def test_toggle_todo(client):
    """Test marcar tarea como completada"""
    # Crear una tarea
    with app.app_context():
        todo = Todo(title='Test Toggle', description='Test')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id
    
    # Marcar como completada
    response = client.get(f'/toggle/{todo_id}', follow_redirects=True)
    assert response.status_code == 200

def test_delete_todo(client):
    """Test eliminar tarea"""
    # Crear una tarea
    with app.app_context():
        todo = Todo(title='Test Delete', description='Test')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id
    
    # Eliminar tarea
    response = client.get(f'/delete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
