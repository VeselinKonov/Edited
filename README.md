To run the application please follow the instructions:

There are two options to run this applications based on OS.

First of all create venv and install requirements for the app. 

Create new venv and activate it. `python3 -m venv <name_of_venv>` `source <venv_name>/bin/activate` 

Run `pip install -r requirement.txt`  

1. First options (Linux). Install chromedriver:
   
  a) Debian/Ubuntu
```
sudo dnf install chromedriver
```
  b) Fedora/RedHat
```
sudo apt-get install chromium-chromedriver
```

2. Second option. Use it via Docker:
```
docker run -d -p 4444:4444 selenium/standalone-chrome
```

Finally to run the scrapy spider:
Navigate to dir `edited`

then run: 

```
scrapy crawl marksandspencer -o data.json
```
where `data.json` is the name of the file for the output


