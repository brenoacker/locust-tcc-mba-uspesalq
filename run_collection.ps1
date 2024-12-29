param (
    [Boolean] $fiddler=$true
)

# $env:REDIS_PRIMARY_USER_TABLE = "users_primary"
# $env:REDIS_SECONDARY_USER_TABLE = "users_secondary"

$env:REDIS_PRIMARY_SENIOR_USER_TABLE = "senior_users_primary"
$env:REDIS_SECONDARY_SENIOR_USER_TABLE = "senior_users_secondary"

$env:REDIS_PRIMARY_MID_AGE_USER_TABLE = "mid_users_primary"
$env:REDIS_SECONDARY_MID_AGE_USER_TABLE = "mid_users_secondary"

$env:REDIS_PRIMARY_YOUNG_USER_TABLE = "young_users_primary"
$env:REDIS_SECONDARY_YOUNG_USER_TABLE = "young_users_secondary"

# Obter a data e hora atual no formato desejado
$date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

# Gerar o nome do arquivo de relatório
$reportFileName = "reports/report_$date.html"



docker-compose up -d

# Esperar alguns segundos para garantir que os serviços estejam prontos
Start-Sleep -Seconds 10

# locust -f tests\collection.py --host "http://localhost" -u 0 -r 0 --autostart --html $reportFileName --headless --autoquit 1

python utils/db/add_users_redis.py

# Executar o Locust
locust -f tests\collection.py --host "http://localhost" -u 0 -r 0 --autostart --html $reportFileName --autoquit 1

# Parar e remover os containers do Docker Compose após o teste
docker-compose down