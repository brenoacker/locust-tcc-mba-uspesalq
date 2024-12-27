param (
    [Boolean] $fiddler=$true
)

$env:REDIS_PRIMARY_USER_TABLE = "users_primary"
$env:REDIS_SECONDARY_USER_TABLE = "users_secondary"

docker-compose up -d

# Esperar alguns segundos para garantir que os serviços estejam prontos
Start-Sleep -Seconds 10

python utils\postgres\add_users.py

# Parar e remover os containers do Docker Compose após o teste
docker-compose down