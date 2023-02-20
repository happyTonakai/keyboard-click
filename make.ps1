pyinstaller --windowed --onefile --clean --add-data 'switch-on.png;.' --add-data 'switch-off.png;.' keymouse.py
If (Test-Path ~/keymouse.exe) {
	Remove-Item ~/keymouse.exe
}
Copy-Item dist/keymouse.exe ~/keymouse.exe
Start-Process ~/keymouse.exe