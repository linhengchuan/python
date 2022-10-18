rd /s /q dist
rd /s /q build
rd /s /q app.spec

python setup.py build_ext --inplace

pyinstaller --name="myapp" --onefile app.py