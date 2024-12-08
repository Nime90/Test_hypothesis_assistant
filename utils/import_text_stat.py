def import_text_stat(url = 'https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/'):
    import requests
    from bs4 import BeautifulSoup

    # URL of the website to scrape

    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text (for example, all paragraph text)
        if 'spss' not in str(url):
            paragraphs = soup.find_all('table')
            source_text=''
            for para in paragraphs:
                source_text += str(para.get_text())
        else:
            paragraphs = soup.find_all('article')
            source_text=''
            for para in paragraphs:
                source_text += str(para.get_text())

    else:
        print("Failed to retrieve the webpage")
    return source_text

def import_text_stat_standard(url = 'https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1116-1-199710-S!!PDF-E.pdf'):
    import PyPDF2
    import requests, os

    response = requests.get(url)

    # Save the PDF to a local file
    with open('sample.pdf', 'wb') as f:
        f.write(response.content)
    Full_text = ''
    # Open the downloaded PDF file
    with open('sample.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract text from the first page
        for p in range(len(reader.pages)):
            page = reader.pages[0]
            text = page.extract_text()
            Full_text = Full_text + text
    if os.path.exists('sample.pdf'): os.remove('sample.pdf')

    return Full_text

def all_stat_page(url = 'https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/'):
    import requests
    from bs4 import BeautifulSoup

    # URL of the website to scrape

    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        all_stat = soup.get_text()
    return all_stat