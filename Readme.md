# Meme Generator
This project showcases building a multimedia application for generating meme. 
Consuming existing python libraries, sub processing non python application and package it as cli tool and web service.

## Project Structure
``` 
    Readme.md
    │
    src
    ├── app.py
    ├──fonts
    │  ├── RobotoMono-Italic.ttf
    │  └── RobotoMono-Regular.ttf
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
    ├── requirements.txt
    ├── static
    ├── temp
    └── templates
        ├── base.html
        ├── meme_form.html
        └── meme.html
```

## Requirements
### Python 3.6
```bash
$ python3 --version
Python 3.6.10

$ pip3 install requirements.txt
```
### pdftotext
[pdftotext](https://www.xpdfreader.com/pdftotext-man.html) CLI utility

## Modules
### Quote Engine
The module is responsible to load and parse quotes from files. Utilizing object-oriented principles, it provides the functionality for ingesting quote from different kinds of file formats (*csv*, *docx*, *pdf*, *txt*).
#### Classes
 * ```QuoteModel```: a quote representation which consists of a body and its author
 * ```IngestorInterface```: interface that define strategy pattern for quote ```Ingestor```.
 * ```CSVIngestor```: ingestor for csv format
 * ```DocxIngestor```: ingestor for docx format
 * ```PDFIngestor```: ingestor for pdf format
 * ```TextIngestor```: ingestor for txt format
 * ```Ingestor```: ingestor that can read supported file formats
#### Dependencies
 ```
pandas==1.1.5
python-docx==0.8.11
pdftotext version 0.86.1
```
### Meme Generator
The module is responsible for manipulating and drawing text onto images. Consuming advanced third party library to handle the image manipulation.
#### Classes
* ```MemeGenerator```: handles image manipulation, text drawing and output the generated image file
#### Dependencies
 ```
Pillow==8.3.2
```
### Application Starter
* ```meme.py```: provides the cli tool for meme generator
* ```app.py```: provides a flask app, to run meme generator in a browser
#### Dependencies
 ```
Flask==2.0.1
```

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