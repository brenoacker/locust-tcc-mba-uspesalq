param (
    [Boolean] $fiddler=$true
)
# Obter a data e hora atual no formato desejado
$date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

# Gerar o nome do arquivo de relatório
$reportFileName = "reports/report_$date.html"

# locust -f tests\collection.py --host "http://localhost" -u 0 -r 0 --autostart --html $reportFileName --headless --autoquit 1

locust -f tests\collection.py --host "http://localhost" -u 0 -r 0 --autostart --html $reportFileName --autoquit 1