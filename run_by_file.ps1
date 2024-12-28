param (
    [Boolean] $fiddler=$true
)

$vUsers = 1
$rampUp = 1
$runTime = "10m"


locust -f tests\order\delivery\delivery_order_senior_user_without_offer_and_card.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_product\create_burger.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_amount_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_percentage_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_user\create_senior_user.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime