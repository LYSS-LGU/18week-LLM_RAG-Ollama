import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700', '4L6ODo1rTEROnXZg_MN6YQFtUl6REBZlEyWeQ4KyxLA') 

def stock_search(query):
  return client.index('nasdaq').search(query)