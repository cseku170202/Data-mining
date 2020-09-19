import bs4
import requests
import csv

all_unit_link = []
main_page_links = []

base_address = "https://www.jugantor.com"
category = "national"


def get_sub_links(main_page_link):

    global all_unit_link
    #print(main_page_link)
    page = requests.get(main_page_link)
    #print(page)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    #newsArticleDivs = soup.find_all("div", {"class": "col-xs-12 col-sm-6 col-md-6 n_row"})
    newsArticleDivs = soup.find_all("div", {"class": "col-md-4 col-sm-4 col-xs-4"})

    for newsArticle in newsArticleDivs:
        a_tag = newsArticle.find("a")
        news_link = a_tag['href']
        #print(news_link)
        #complete_url = base_address + news_link[1:]
        complete_url = news_link[0:]
        print(complete_url)
        all_unit_link.append([complete_url])
        #print(all_unit_link)

    pass



def write_csv(list_to_be_inserted):
    with open('national_unit_page_url.csv', mode='w', newline='',encoding='utf-8') as unit_url_list:
        unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in list_to_be_inserted:
            print(url)
            unit_url_writer.writerow(url)

    unit_url_list.close()

    pass



with open('national_main_page_url.csv') as main_url_csv:
    readCSV = csv.reader(main_url_csv)

    for row in readCSV:
        main_page_links.append(row[0])

print('+---------------------------------------------------------+')

for main_link in main_page_links:
    get_sub_links(main_link)
    pass

write_csv(all_unit_link)

print(len(all_unit_link))


