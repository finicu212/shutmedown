# Makefile

default: app

app:
    pyinstaller --onefile --add-data "templates;templates" app.py

clean:
    rm -rf build dist *.spec
