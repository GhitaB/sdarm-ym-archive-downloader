import requests

prefix = "http://sdarmorg.listentosermon.net/files/publications/periodicals/ym/pdf/"
languages = ["en"]
location = "/home/ghitabizau/Backups/"
# ym1997_2_en.pdf


def download_file(url, filename):
    result = True
    try:
        r = requests.get(url)
        open(filename, 'wb').write(r.content)
    except:
        result = False
    return result

for year in range(1996, 2020):
    for number in range(1, 5):
        for lang in languages:
            sufix = "ym" + str(year) + "_" + str(number) + "_" + lang + ".pdf"
            url = prefix + sufix
            filename = location + sufix
            print "Downloadind " + url
            result = download_file(url, filename)
            print result
