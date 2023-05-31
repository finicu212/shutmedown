# Makefile

default: app

app:
	pyinstaller --onefile --add-data "templates;templates" app.py

clean:
	rm -rf build dist *.spec

# set up Windows Task Scheduler. Inside a Makefile. Madness 
task:
        @APP_PATH=$(shell cd && pwd)/dist/app.exe; \
    schtasks /Create /TN "shutmedown" /TR $$APP_PATH /SC ONEVENT /EC System /MO "*[System[Provider[@Name='Microsoft-Windows-Kernel-Power'] and EventID=42]]" /RL HIGHEST
