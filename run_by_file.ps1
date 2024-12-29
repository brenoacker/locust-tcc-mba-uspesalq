param (
    [Boolean] $fiddler=$true
)

$env:REDIS_PRIMARY_SENIOR_USER_TABLE = "senior_users_primary"
$env:REDIS_SECONDARY_SENIOR_USER_TABLE = "senior_users_secondary"

$env:REDIS_PRIMARY_MID_AGE_USER_TABLE = "mid_users_primary"
$env:REDIS_SECONDARY_MID_AGE_USER_TABLE = "mid_users_secondary"

$env:REDIS_PRIMARY_YOUNG_USER_TABLE = "young_users_primary"
$env:REDIS_SECONDARY_YOUNG_USER_TABLE = "young_users_secondary"

$vUsers = 1
$rampUp = 1
$runTime = "10m"



docker-compose up -d

# Esperar alguns segundos para garantir que os serviços estejam prontos
Start-Sleep -Seconds 10

# locust -f tests\collection.py --host "http://localhost" -u 0 -r 0 --autostart --html $reportFileName --headless --autoquit 1

python utils/db/add_users_redis.py

# Executar o Locust
locust -f tests\order\delivery\delivery_order_senior_user_without_offer_and_card.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_product\create_burger.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_amount_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_percentage_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_user\create_senior_user.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime


# Parar e remover os containers do Docker Compose após o teste
docker-compose down