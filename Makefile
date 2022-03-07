
dist/resize.app: resize.py resize.spec
	-rm -rf build/ dist/
	pyinstaller -F --windowed resize.spec
