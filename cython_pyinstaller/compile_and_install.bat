rd /s /q dist
rd /s /q build
del app.spec
del .spec

python setup.py build_ext --inplace

pyinstaller --name="app" --onefile app.py