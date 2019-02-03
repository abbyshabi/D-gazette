from .models import Sources,Articles
import urllib.request,json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#Sources = source.Sources

api_key = None
base_url = None
source_url = None

def configure_request(app):
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEWS_API_URL'] 
    sources_url = app.config['SOURCE_NEWS_URL'] 

def get_sources(source):
    '''
     The get_sources function fetches the various news sources from the API

    '''

    get_sources_url = 'https://newsapi.org/v1/sources'.format(source,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function that process the source results list and transforms them into a list of objects

    Args: 
        sources_list: A list of dictionaries that contains sources details
    
    Returns:
        sources_results: a list of sources objects
    '''

    sources_results = []
    for source_item in sources_list:
        source_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        

        source_object = Sources(id, name, description, url, category,country)
        sources_results.append(source_object)

    return sources_results

def get_articles(source):
    '''
    The get articles function gets the listed articles for a selected source
    '''

    get_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(source, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_result = None

        if get_articles_response['articles']:
            articles_result_list = get_articles_response['articles']
            print(articles_result_list)
            articles_result = process_article_results(articles_result_list)
    return articles_result

def process_article_results(articles_list):
    '''
    Function that process the article results list and displays on the html as a list.

    Args: 
        sources_list: A list of dictionaries that contains sources details
    
    Returns:
        sources_results: a list of sources objects
    '''
    articles_result = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result.get['source']['id']
        author = result.get('author')
        title = result.get('title')
        description =result.get('description')
        urlToImage =result.get('urlToImage')
        url = result.get('url')
        publishedAt =result.get('publishedAt')

        if urlToImage:
            source_object = Sources(source_id,author,title,description,urlToImage,url,publishedAt)
            articles_result.append(source_object)
    
    return articles_result


