# Makefile

default: app

app:
    pyinstaller --onefile --add-data "templates;templates" app.py

clean:
    rm -rf build dist *.spec

# Windows Task Scheduler ?? Inside a Makefile ??? MADNESS
task:
    schtasks /Create /TN "MyAppOnIdle" /TR "C:\path\to\your\app.exe" /SC ONEVENT /EC System /MO "*[System[Provider[@Name='Microsoft-Windows-Kernel-Power'] and EventID=42]]" /RL HIGHEST
