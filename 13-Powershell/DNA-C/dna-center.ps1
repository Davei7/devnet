$url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

$user = 'devnetuser'
$pw = ConvertTo-SecureString 'Cisco123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ($user, $pw)

$headers = @{
    'Accept' = 'application/json'
}

$response = Invoke-RestMethod -Uri $url `
    -Method Post `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

$response | ConvertTo-Json | Write-Output
$token = $response.token

$uri = "https://sandboxdnac.cisco.com/dna/system/api/v1/client-health?timestamp="

$headers = @{
    'Accept' = 'application/json'
    'X-auth-token' = $token
}

$response = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -Authentication Basic `
    -Credential $Cred `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

$details = $response.response.scoreDetail

ForEach ($detail in $details) {
    Write-Host "Object " -ForegroundColor Blue -NoNewline
    Write-Host "$($detail.scoreCategory.value)" -ForegroundColor Red
}