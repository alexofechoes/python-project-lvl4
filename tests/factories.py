from django.contrib.auth import get_user_model
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from taskmanager.tasks.models import Tag, Task, TaskStatus


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')

    class Meta:
        model = get_user_model()


class TagFactory(DjangoModelFactory):
    name = Faker('word')

    class Meta:
        model = Tag


class TaskStatusFactory(DjangoModelFactory):
    name = Faker('word')

    class Meta:
        model = TaskStatus


class TaskFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=3)
    description = Faker('text', max_nb_chars=200)  # noqa WPS432
    creator = SubFactory(UserFactory)
    assigned_to = SubFactory(UserFactory)

    class Meta:
        model = Task
