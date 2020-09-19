import bs4
import requests
import csv 

#base_address = "https://www.kalerkantho.com"
base_address = "https://www.jugantor.com"
category = "national"


national_category = ["","government","crime","law-justice","media","accident","mourning","others"]
all_url = []
i = 0
for page_index in national_category:
    i = i + 1
    if i==1:
        complete_url = base_address+'/'+category
        print(complete_url)
    else:
        complete_url = base_address+'/'+category+'/'+str(page_index)
        print(complete_url)

    all_url.append([complete_url])

    pass

with open('national_main_page_url.csv', mode='w', newline='') as main_url_list:
    main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for url in all_url:
        print(url)
        main_url_writer.writerow(url)

main_url_list.close()