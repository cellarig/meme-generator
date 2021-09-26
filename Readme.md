# Meme generator
This project showcases building a multimedia application for generating meme. 
Consuming existing python libraries, sub processing non python application and package it as cli tool and web service.  
___
## Project Structure
``` 
    fonts
    ├── RobotoMono-Italic.ttf
    ├── RobotoMono-Regular.ttf
    │
    requirements.txt
    │
    Readme.md
    │
    src
    ├── app.py
    ├── _data
    │   ├── DogQuotes
    │   │   ├── DogQuotesCSV.csv
    │   │   ├── DogQuotesDOCX.docx
    │   │   ├── DogQuotesPDF.pdf
    │   │   └── DogQuotesTXT.txt
    │   ├── photos
    │   │   └── dog
    │   │       ├── xander_1.jpg
    │   │       ├── xander_2.jpg
    │   │       ├── xander_3.jpg
    │   │       └── xander_4.jpg
    │   └── SimpleLines
    │       ├── SimpleLines.csv
    │       ├── SimpleLines.docx
    │       ├── SimpleLines.pdf
    │       └── SimpleLines.txt
    │
    ├── MemeEngine
    │   ├── __init__.py
    │   └── meme_generator.py
    │     
    ├── meme.py
    ├── QuoteEngine
    │   ├── csv_ingestor.py
    │   ├── docx_ingestor.py
    │   ├── ingestor.py
    │   ├── ingestor_interface.py
    │   ├── __init__.py
    │   ├── pdf_ingestor.py
    │   ├── quote_model.py
    │   └── txt_ingestor.py
    │
    ├── requirement.txt
    └── templates
        ├── base.html
        ├── meme_form.html
        └── meme.html
```

## Requirements
___
### Python 3.6
```bash
$ python3 --version
Python 3.6.10

$ pip install requirements.txt
```
### pdftotext
[pdftotext](https://www.xpdfreader.com/pdftotext-man.html) CLI utility


## Modules
___
### Quote Engine
### Meme Generator

## How to run
### CLI
```bash
$ python meme.py --help
optional arguments:
  -h, --help       show this help message and exit
  --body BODY      a quote body text
  --author AUTHOR  an author of quote
  --path PATH      a path of image directory
```

### Flask App
```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```