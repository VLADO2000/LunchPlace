import pytest
from restaurant.models import Restaurant
from authentication.models import CustomUser

from restaurant.serializers import RestaurantSerializer
from rest_framework.test import APIRequestFactory, force_authenticate

from restaurant.views import RestaurantViewSet

@pytest.mark.django_db
def test_create_restaurant():
    restaurant = Restaurant.objects.create(name='Test Restaurant')
    assert str(restaurant) == f"{restaurant.id}-{restaurant.name}"


@pytest.mark.django_db
def test_restaurant_serializer():
    user = CustomUser.objects.create_user(email='test@example.com', password='testpassword', role=1)
    data = {'name': 'Test Restaurant'}
    serializer = RestaurantSerializer(data=data, context={'request': user})
    assert serializer.is_valid()
    restaurant = serializer.save()

    assert restaurant.name == data['name']
    assert restaurant.users_emails == [user.email]

@pytest.mark.django_db
def test_create_restaurant_view():
    user = CustomUser.objects.create_user(email='test@example.com', password='testpassword', role=1)
    factory = APIRequestFactory()
    view = RestaurantViewSet.as_view({'post': 'create'})
    data = {'name': 'Test Restaurant'}

    request = factory.post('/api/v1/restaurant/', data, format='json')
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == 201
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.first().name == data['name']

@pytest.mark.django_db
def test_get_restaurant_list_view():
    user = CustomUser.objects.create_user(email='test@example.com', password='testpassword', role=1)
    restaurant = Restaurant.objects.create(name='Test Restaurant')
    factory = APIRequestFactory()
    view = RestaurantViewSet.as_view({'get': 'list'})

    request = factory.get('/api/v1/restaurant/')
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == restaurant.name