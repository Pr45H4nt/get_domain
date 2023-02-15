def get_domain_name(url):
    """Extracts the domain name from a given URL."""
    if url.startswith("https://"):
        url = url.replace("https://", "")
    elif url.startswith("http://"):
        url = url.replace("http://", "")

    if url.startswith("www."):
        url = url.replace("www.", "")

    if '/' in url:
        #if url contains '/' after removal of prefixes then it slices to the point of '/'
        url = url[:url.index('/')]

    return url
