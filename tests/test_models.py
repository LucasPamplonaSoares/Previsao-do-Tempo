import pytest
from ..models import user

pytestmark = pytest.mark.django_db  # Acessar o banco de dados


def test_create_user():
    user = user.objects.create_user(
        username='usuario_test', telefone= 47992818634, cpf=11122233344
    )

    assert user.username == 'usuario_test'
    assert user.telefone ==  47992818634
    assert user.cpf == 11122233344
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = user.objects.create_superuser(
        username='admin_test', telefone= 47558886633, cpf= 55566633311
    )
    assert user.username == 'admin_test'
    assert user.telefone == 47558886633
    assert user.cpf == 55566633311
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
