param (
    [Boolean] $fiddler=$true
)

$vUsers = 100
$rampUp = 1
$runTime = "6m"

locust -f tests\create_product\create_burger.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_amount_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_offer\create_percentage_offer.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
# locust -f tests\create_user\create_senior_user.py --host "https://localhost:8000" -u $vUsers -r $rampUp --autostart --run-time $runTime
