import requests
from bs4 import BeautifulSoup

url_to_parse = "https://stardewvalleywiki.com/Crops"
response = requests.get(url_to_parse)
page = response.text
soup = BeautifulSoup(page, 'lxml')

#find the rows containing the list of seasonal crops, and separate them, put into dict
crop_table = soup.find('table', id="navbox")
second_row = crop_table.select("tr:nth-of-type(2) > td > a")
third_row = crop_table.select("tr:nth-of-type(3) > td > a")
fourth_row = crop_table.select("tr:nth-of-type(4) > td > a")

spring_crop_list = []
summer_crop_list = []
fall_crop_list = []

crop_id_list = []


for crop in second_row:
    spring_crop_list.append(crop.text)
    crop_id_list.append((crop.text).replace(" ", "_"))
for crop in third_row:
    summer_crop_list.append(crop.text)
    crop_id_list.append((crop.text).replace(" ", "_"))
for crop in fourth_row:
    fall_crop_list.append(crop.text)
    crop_id_list.append((crop.text).replace(" ", "_"))

seasonal_crops = {"spring" : spring_crop_list,
                  "summer" : summer_crop_list,
                  "fall" : fall_crop_list}

#find each crop's repsective base profit and put into dict
crop_profit = {}
outside_counter = 0
def find_crop_profit(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        profit = big_table.select_one("tr:nth-of-type(2) > td > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)")
        crop_profit[name.lower()] = (profit.text).rstrip()
        i+=1
        count += 1
    return count
outside_counter = find_crop_profit(spring_crop_list, outside_counter)
outside_counter = find_crop_profit(summer_crop_list, outside_counter)
outside_counter = find_crop_profit(fall_crop_list, outside_counter)

#find crop's cost and put into and put into dict
crop_cost = {}
outside_counter = 0
def find_crop_cost(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        cost = big_table.select_one("tr:nth-of-type(2) > td > div:nth-of-type(2) > span:nth-of-type(2)")
        crop_cost[name.lower()] = (cost.text).rstrip()
        i+=1
        count+=1
    return count

outside_counter = find_crop_cost(spring_crop_list, outside_counter)
outside_counter = find_crop_cost(summer_crop_list, outside_counter)
outside_counter = find_crop_cost(fall_crop_list, outside_counter)

#find crop's energy and put into dict
crop_energy = {}
outside_counter = 0
def find_crop_energy(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        try:
            energy = big_table.select_one("tr:nth-of-type(2) > td > table > tbody > tr > td:nth-of-type(2)[style]")
            crop_energy[name.lower()] = (energy.text).rstrip()
        except AttributeError:
            crop_energy[name.lower()] = 0
            
        i+=1
        count+=1
    return count
outside_counter = find_crop_energy(spring_crop_list, outside_counter)
outside_counter = find_crop_energy(summer_crop_list, outside_counter)
outside_counter = find_crop_energy(fall_crop_list, outside_counter)

#find crop's health and put into dict
crop_health = {}
outside_counter = 0
def find_crop_health(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        try:
            health = big_table.select_one("tr:nth-of-type(2) > td > table > tbody > tr > td:last-of-type[style]")
            crop_health[name.lower()] = (health.text).rstrip()
        except AttributeError:
            crop_health[name.lower()] = 0
            
        i+=1
        count+=1
    return count
outside_counter = find_crop_health(spring_crop_list, outside_counter)
outside_counter = find_crop_health(summer_crop_list, outside_counter)
outside_counter = find_crop_health(fall_crop_list, outside_counter)

#find total time to grow crop and put into dict
growth_time = {}
outside_counter = 0
def find_growth_time(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        time = big_table.select_one("tr:last-of-type > td:nth-of-type(5)")
        if "Total" not in (time.text):
            time = big_table.select_one("tr:last-of-type > td:nth-of-type(6)")
        growth_time[name.lower()] = (time.text).rstrip()
        if name=="Unmilled Rice":
            growth_time[name.lower()] = (time.text)[0:13] + " (Unirrigated); " + (time.text)[15:28] + " (Irrigated)"
        i+=1
        count+=1
    return count
outside_counter = find_growth_time(spring_crop_list, outside_counter)
outside_counter = find_growth_time(summer_crop_list, outside_counter)
outside_counter = find_growth_time(fall_crop_list, outside_counter)

#find all of the crop's uses
crop_uses = {}
outside_counter = 0
def find_uses(lst, count):
    i = 0
    while i <= len(lst)-1:
        name = lst[i]
        crop_span = soup.find("span", class_="mw-headline", id=crop_id_list[count])
        big_table = crop_span.find_parent().find_next_sibling("table")
        uses = big_table.select("tr:nth-of-type(2) > td:last-of-type a")
        uses_list = []
        for x in uses:
            uses_list.append(x.text)
        crop_uses[name.lower()] = uses_list
        i+=1
        count+=1
    return count
outside_counter = find_uses(spring_crop_list, outside_counter)
outside_counter = find_uses(summer_crop_list, outside_counter)
outside_counter = find_uses(fall_crop_list, outside_counter)

crop_info = {"Seasonal Crops" : seasonal_crops,
             "Profits" : crop_profit,
             "Costs" : crop_cost,
             "Energy" : crop_energy,
             "Health" : crop_health,
             "Growth Time" : growth_time,
             "Uses" : crop_uses}
        
