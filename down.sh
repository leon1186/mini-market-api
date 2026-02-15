

docker stop $(docker ps -q) 2>/dev/null
docker rm $(docker ps -aq) 2>/dev/null
docker compose down --rmi all -v

# docker compose down -v 
