def import_text_stat():
    import requests
    from bs4 import BeautifulSoup

    # URL of the website to scrape
    url = 'https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/'

    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text (for example, all paragraph text)
        paragraphs = soup.find_all('table')
        source_text=''
        for para in paragraphs:
            source_text += str(para.get_text())
    else:
        print("Failed to retrieve the webpage")
    return source_text