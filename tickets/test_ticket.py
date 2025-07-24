import pytest
from tickets.models import Ticket
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_ticket_creation():
    user = User.objects.create_user(username='testuser', password='testpass')
    ticket = Ticket.objects.create(
        title='Test Ticket',
        description='Testing ticket creation',
        status='open',
        created_by=user
    )
    assert ticket.title == 'Test Ticket'
