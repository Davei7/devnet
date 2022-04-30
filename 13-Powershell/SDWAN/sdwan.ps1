$url = "https://sandbox-sdwan-1.cisco.com/j_security_check"

$login_body = @{
    j_username = 'devnetuser'
    j_password = 'RG!_Yw919_83'
}

$headers = @{
    'Accept' = 'application/json'
}

Invoke-RestMethod -Uri $url `
    -Method Post `
    -Body ($login_body) `
    -ContentType 'application/x-www-form-urlencoded' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s

$uri = "https://sandbox-sdwan-1.cisco.com/dataservice/device"

$devices = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -WebSession $s

Write-Host "Output!!!!!!"
$devices = $devices.data | ConvertTo-Json

ForEach ($device in $devices) {
    Write-Host "Device " -ForegroundColor Blue -NoNewline
    Write-Host "$($device)" -ForegroundColor Green
}