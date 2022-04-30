$uri = 'https://ios-xe-mgmt-latest.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet2'

# $cred = Get-Credential

$password = ConvertTo-SecureString 'C1sco12345' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('developer', $password)
$headers = @{'Accept' = 'application/yang-data+json'}

$response = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -Authentication Basic `
    -Credential $cred `
    -ContentType 'application/yang-data+json' `
    -Headers $headers `
    -SkipCertificateCheck

$response | ConvertTo-Json | Write-Output

#$response.'Cisco-IOS-XE-interfaces-oper:interface'.name

if($response.'Cisco-IOS-XE-interfaces-oper:interface'.'admin-status' -eq 'if-state-up'){
    Write-Host ($response.'Cisco-IOS-XE-interfaces-oper:interface'.name)'is up!'
}
else{
    Write-Host ($response.'Cisco-IOS-XE-interfaces-oper:interface'.name)'is down!'
}
