import urllib2
from BeautifulSoup import BeautifulSoup

def lookupCVR(cvr):
    url = "http://cvr.dk/Site/Forms/PublicService/DisplayCompany.aspx?cvrnr=" + cvr

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    names = soup.findAll('td', {"class" : "fieldname"})
    values = soup.findAll('td', {"class" : "fieldvalue"})

    result = {}

    for i in range(0, 14):
        result[names[i].text.lower().rstrip(':')] = values[i].text

    result['adresse'] = values[4].contents[0].lstrip()
    adresse2 = values[4].contents[2].rstrip()

    result['postnummer'] = adresse2.split(' ')[0]
    result['by'] = adresse2.split(' ')[1]
    return result

if __name__ == '__main__':
    info = lookupCVR('44623528')
    print info['by']


