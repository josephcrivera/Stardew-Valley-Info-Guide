from webscrape import crop_info

def crop_search(string, big_list, lil_list_name):
    for i in big_list.get(lil_list_name):
        if i in string:
            return big_list.get(lil_list_name).get(i)
    return "ERROR"

def process(string):
    split_string = string.split(" ")
    print(split_string[0])
    answer = ""
    if split_string[0] == "what":
        if "grow" in split_string: #What crops grow during <season>?
            full_word = split_string[len(split_string)-1]
            season = full_word[:len(full_word)-1].lower()
            answer = crop_info.get("Seasonal Crops").get(season)
        elif "used" in split_string: #What is <crop> used in?
            answer = crop_search(string, crop_info, "Uses")
        else:
            answer = "I'm having trouble understanding your question.\nMake sure that all crops are spelled correctly and refer to the question list"
    elif split_string[0] == "how": 
        if "long" in string: # How long does <crop> take to grow?
            answer = crop_search(string, crop_info, "Growth Time")
        elif "cost" in string: #How much does <crop> cost?
            answer = crop_search(string, crop_info, "Costs")
        elif "sell" in string: #How much does <crop> sell for?
            answer = crop_search(string, crop_info, "Profits")
        elif "energy" in string: #How much energy does <crop> give?
            answer = crop_search(string, crop_info, "Energy")
        elif "health" in string: #How much health does <crop> give?
            answer = crop_search(string, crop_info, "Health")
        else:
            answer = "I'm having trouble understanding your question.\nMake sure that all crops are spelled correctly and refer to the question list"
    else:
        answer = "I'm having trouble understanding your question.\nMake sure that all crops are spelled correctly and refer to the question list"
    return answer

