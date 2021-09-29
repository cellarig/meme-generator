"""Flask app to run meme generator as web service."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine import MemeGenerator
from QuoteEngine import QuoteModel, Ingestor

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = [images_path + file for file in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    quote_body = request.form.get('body')
    quote_author = request.form.get('author')

    if quote_body == '' or quote_author == '':
        quote = random.choice(quotes)
    else:
        quote = QuoteModel(quote_body, quote_author)

    r = requests.get(image_url)
    ext = image_url.split('.')[-1]
    img_tmp_path = f'./tmp/downloaded.{ext}'

    try:
        with open(img_tmp_path, 'wb') as f:
            f.write(r.content)
        path = meme.make_meme(img_tmp_path, quote.body, quote.author)
    finally:
        os.remove(img_tmp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
