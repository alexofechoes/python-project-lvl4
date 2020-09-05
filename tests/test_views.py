from http import HTTPStatus

from django.contrib.auth.models import User

from taskmanager.tasks.models import Tag, Task, TaskStatus
from tests.factories import TaskFactory, TaskStatusFactory, UserFactory


def test_task_list(client, user_credentials):
    client.login(**user_credentials)

    tasks = TaskFactory.create_batch(5)

    response = client.get('/')
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    for task in tasks:
        assert task.name in response_body


def test_task_list_with_filter(client, user_credentials):
    client.login(**user_credentials)

    selected_status = TaskStatusFactory()
    not_selected_status = TaskStatusFactory()
    current_user = User.objects.get(username=user_credentials['username'])
    another_user = UserFactory()

    my_tasks_with_selected_status = TaskFactory.create_batch(
        3,
        assigned_to=current_user,
        status=selected_status,
    )
    my_tasks_without_selected_status = TaskFactory.create_batch(
        3,
        assigned_to=current_user,
        status=not_selected_status,
    )
    not_my_task_with_selected_status = TaskFactory.create_batch(
        3,
        assigned_to=another_user,
        status=selected_status,
    )

    response = client.get('/', {
        'status': selected_status.id,
        'my_task': 'on',
    })
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    for task in my_tasks_with_selected_status:
        assert task.name in response_body

    for task in my_tasks_without_selected_status:
        assert task.name not in response_body

    for task in not_my_task_with_selected_status:
        assert task.name not in response_body


def test_task_detail(client, user_credentials):
    client.login(**user_credentials)

    task = TaskFactory()

    response = client.get('/tasks/{id}/'.format(id=task.id))
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert task.name in response_body


def test_task_create_page(client, user_credentials):
    client.login(**user_credentials)

    response = client.get('/tasks/create/')
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert 'Create task' in response_body


def test_task_create(client, user_credentials):
    client.login(**user_credentials)

    task_name = 'new_test_task'
    task_status = TaskStatusFactory()
    assert not Task.objects.filter(name=task_name).exists()

    response = client.post('/tasks/create/', {
        'name': task_name,
        'status': task_status.id,
    })

    assert response.status_code == HTTPStatus.FOUND
    assert Task.objects.filter(name=task_name).exists()


def test_task_update_page(client, user_credentials):
    client.login(**user_credentials)

    task = TaskFactory()

    response = client.get('/tasks/{id}/edit/'.format(id=task.id))
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert 'Update task' in response_body


def test_task_update(client, user_credentials):
    client.login(**user_credentials)

    task = TaskFactory()
    task_new_name = 'new_test_task'
    task_from_db = Task.objects.get(id=task.id)
    assert task_from_db.name != task_new_name

    response = client.post('/tasks/{id}/edit/'.format(id=task.id), {
        'name': task_new_name,
        'status': task_from_db.status.id,
    })

    updated_task_from_db = Task.objects.get(id=task.id)
    assert response.status_code == HTTPStatus.FOUND
    assert updated_task_from_db.name == task_new_name


def test_task_delete(client, user_credentials):
    client.login(**user_credentials)

    task = TaskFactory()
    assert Task.objects.filter(id=task.id).exists()

    response = client.post('/tasks/{id}/delete/'.format(id=task.id))
    assert response.status_code == HTTPStatus.FOUND
    assert not Task.objects.filter(id=task.id).exists()


def test_task_status_list(client, user_credentials):
    client.login(**user_credentials)

    task_statuses = TaskStatusFactory.create_batch(5)

    response = client.get('/task-status/')
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    for task_status in task_statuses:
        assert task_status.name in response_body


def test_task_status_detail(client, user_credentials):
    client.login(**user_credentials)

    task_status = TaskStatusFactory()

    response = client.get('/task-status/{id}/'.format(id=task_status.id))
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert task_status.name in response_body


def test_task_status_create_page(client, user_credentials):
    client.login(**user_credentials)

    response = client.get('/task-status/create/')
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert 'Create status' in response_body


def test_task_status_create(client, user_credentials):
    client.login(**user_credentials)

    task_status_name = 'new_test_task_status'
    assert not TaskStatus.objects.filter(name=task_status_name).exists()

    response = client.post('/task-status/create/', {
        'name': task_status_name,
    })

    assert response.status_code == HTTPStatus.FOUND
    assert TaskStatus.objects.filter(name=task_status_name).exists()


def test_task_status_update_page(client, user_credentials):
    client.login(**user_credentials)

    task_status = TaskStatusFactory()

    response = client.get('/task-status/{id}/edit/'.format(id=task_status.id))
    response_body = response.content.decode()

    assert response.status_code == HTTPStatus.OK
    assert 'Update status' in response_body


def test_task_status_update(client, user_credentials):
    client.login(**user_credentials)

    task_status = TaskStatusFactory()
    task_status_new_name = 'new_test_task_status'
    task_status_from_db = TaskStatus.objects.get(id=task_status.id)
    assert task_status_from_db.name != task_status_new_name

    response = client.post(
        '/task-status/{id}/edit/'.format(id=task_status.id),
        {'name': task_status_new_name},
    )

    updated_task_status_from_db = TaskStatus.objects.get(id=task_status.id)
    assert response.status_code == HTTPStatus.FOUND
    assert updated_task_status_from_db.name == task_status_new_name


def test_task_status_delete(client, user_credentials):
    client.login(**user_credentials)

    task_status = TaskStatusFactory()
    assert TaskStatus.objects.filter(name=task_status.name).exists()

    response = client.post(
        '/task-status/{id}/delete/'.format(id=task_status.id),
    )
    assert response.status_code == HTTPStatus.FOUND
    assert not TaskStatus.objects.filter(name=task_status.name).exists()
