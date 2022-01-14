$url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

$headers = @{
    'Accept' = 'application/json'
}

$payload = @{
    aaaUser = @{
        attributes= @{
            name = "admin"
            pwd = "!v3G@!4@Y"
        }
    }
}

$response = Invoke-RestMethod -Uri $url `
    -Method Post `
    -Body ($payload | ConvertTo-Json) `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s

# Print Token
Write-Host "Token: " -ForegroundColor Red -NoNewline
Write-Host $response.imdata.aaaLogin.attributes.token

$uri = "https://sandboxapicdc.cisco.com:443/api/class/fvAp.json"

$ap = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -WebSession $s

Write-Host "Applications: " -ForegroundColor Red
$ap.imdata.fvAp.attributes
