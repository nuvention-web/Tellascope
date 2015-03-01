import urlparse

def clean_url(url):
	parse = urlparse.urlparse(url)
	url = parse.scheme + "://" + parse.netloc + parse.path
	return url
