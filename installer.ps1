# Download Python 3.12.10 installer
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe" -OutFile "python-3.12.10-amd64.exe"
Write-Host "Python installer downloaded."

# Run the installer (silent install, add to PATH)
Start-Process -Wait -FilePath ".\python-3.12.10-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1"
Write-Host "Python installed successfully."

# Remove installer after installation (optional)
Remove-Item ".\python-3.12.10-amd64.exe"
Write-Host "Python installer removed."

# install paramiko libary for the script
Start-Process -Wait -FilePath "cmd.exe" -ArgumentList "/c python -m pip install paramiko"
Write-Host "Paramiko library installed successfully."
Read-Host "Press Enter to exit"