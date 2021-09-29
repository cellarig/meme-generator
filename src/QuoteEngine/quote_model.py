"""Represent a model for a quote."""


class QuoteModel:
    """Quote object that consists of a text and its author."""

    def __init__(self, body, author):
        """Construct a quote with given text body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return 'str(self)' "This is a quote body" - Author."""
        return f'"{self.body}" - {self.author}'
