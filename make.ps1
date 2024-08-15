<#
Author: Zerui Han <hanzr.nju@outlook.com>
Date: 2023-01-17 12:54:37
Description: 
FilePath: /keyboard-click/make.ps1
LastEditTime: 2024-08-15 13:11:16
#>
pyinstaller --windowed --onefile --clean --add-data 'switch-on.png;.' --add-data 'switch-off.png;.' --version-file=file_version_info.txt keymouse.py
# If (Test-Path ~/keymouse.exe) {
	# Remove-Item ~/keymouse.exe
# }
# Copy-Item dist/keymouse.exe ~/keymouse.exe
# Start-Process ~/keymouse.exe