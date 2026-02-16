
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



#################################

