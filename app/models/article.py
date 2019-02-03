class Articles:
    """Articles class to define the articles object"""

    def __init__(self, source_id, author, title, description, urlToImage, url, publishedAt):

        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt
