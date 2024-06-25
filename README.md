To run the application please follow the instructions:

There are two options to run this applications based on OS.

First of all create venv and install requirements for the app.

```
python3 -m venv /path/to/new/virtual/environment
```
```
pip install -r requirements.txt
```

1. First options (Linux). Install chromedriver:
 a) Debian/Ubuntu
```
sudo dnf install chromedriver
```
b) Fedora/RedHat
```
sudo apt install chromedriver
```

2. Second option. Use it via Docker:
```
docker run -d -p 4444:4444 selenium/standalone-chrome
```



