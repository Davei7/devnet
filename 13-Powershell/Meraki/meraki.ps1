$uri = "https://dashboard.meraki.com/api/v0/organizations"

$headers = @{
    'Accept' = 'application/json'
    'X-Cisco-Meraki-API-Key' = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

$orgs = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

ForEach ($org in $orgs){
    if ($org.name -eq 'DevNet Sandbox'){
        $orgId = $org.id
    }
}

#$orgs | ConvertTo-Json | Write-Output

$url_net = "https://dashboard.meraki.com/api/v0/organizations/$($orgId)/networks"

$networks = Invoke-RestMethod -Uri $url_net `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

ForEach ($network in $networks){
    if ($networks.name -eq 'DNSMB2'){
        $netId = $network.id
    }
}

#$networks | ConvertTo-Json | Write-Output

$devices_url = "https://dashboard.meraki.com/api/v0/organizations/$($orgId)/networks/$($netId)/devices"

$devices = Invoke-RestMethod -Uri $devices_url `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck

$devices | ConvertTo-Json | Write-Output