
echo "🚀building and starting containers."

docker compose up -d --build 
# docker ps 
# #############################



# #############################

# # echo "📦running  makemigrations....."

# # docker compose exec api python manage.py makemigrations 

# #############################

# # echo "📦applying   migrations....."
# # docker compose exec api python manage.py migrate
# #docker compose exec db psql -U postgres -d market
# # docker compose exec api env | grep DJANGO
# # docker compose logs api
# docker compose restart api

docker compose exec api python manage.py shell

from django.contrib.auth.models import User
from apps.market.models import Store, Category, Product

user = User.objects.create_user(
    username="owner1",
    password="1234"
)

store = Store.objects.create(
    name="Mini Market Central",
    owner=user
)



beverages = Category.objects.create(
    store=store,
    name="Beverages"
)

snacks = Category.objects.create(
    store=store,
    name="Snacks"
)




Product.objects.create(
    store=store,
    category=beverages,
    name="Coca Cola 1L",
    price=4000,
    stock_quantity=50
)

Product.objects.create(
    store=store,
    category=snacks,
    name="Doritos",
    price=3500,
    stock_quantity=30
)



http://localhost:8000/api/products/

docker compose exec api python manage.py createsuperuser
docker compose exec db psql -U postgres -d market
SELECT id, username, is_superuser FROM auth_user;

#########################################

Database
   ↓
Django Auth
   ↓
Django REST Framework
   ↓
Token Authentication
   ↓
Frontend

#########################################
🔥 Important: They Are NOT Competing

You can use:

Admin for internal management

Token for frontend

Auth as foundation

They work together.

#########################################
