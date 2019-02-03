class Sources:
    '''
    source class to define source objects
    '''
    def __init__(self,source_id,name,description,url,category,country,):
        self.source_id = id
        self.name = name 
        self.description = description
        self.url = url 
        self.category = category
        self.country = country 

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

     