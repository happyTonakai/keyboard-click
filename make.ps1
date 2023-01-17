pyinstaller --onefile keymouse.py
If (Test-Path ~/keymouse.exe) {
	Remove-Item ~/keymouse.exe
}
Move-Item dist/keymouse.exe ~/keymouse.exe