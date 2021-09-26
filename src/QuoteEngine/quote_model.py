"""Represent a model for a quote

A quote consists of a body and its author
e.g  "This is a quote body" - Author
"""


class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" - {self.author}'
