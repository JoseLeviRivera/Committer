$downloadUrl = "https://github.com/JoseLeviRivera/Committer/releases/latest/download/gcz-windows.exe"
$installPath = "C:\gcz"

# Create the installation directory if it doesn't exist
New-Item -Path $installPath -ItemType Directory -Force

# Download the file from GitHub Releases and save it as 'gcz.exe'
Invoke-WebRequest -Uri $downloadUrl -OutFile "$installPath\gcz.exe" -UseBasicParsing

# Get the current 'Path' environment variable at the machine level
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)

# Add 'C:\gcz' to the 'Path' if it's not already included
if ($oldPath -notlike "*$installPath*") {
    [Environment]::SetEnvironmentVariable('Path', "$oldPath;$installPath", [EnvironmentVariableTarget]::Machine)
}

# Apply the new PATH immediately (optional, avoids system restart)
$env:Path = "$installPath;$env:Path"

# Confirm successful installation
if (Test-Path "$installPath\gcz.exe") {
    Write-Host "gcz installed successfully! You can now use 'gcz' from any terminal."
} else {
    Write-Host "Error: gcz.exe was not downloaded."
}
