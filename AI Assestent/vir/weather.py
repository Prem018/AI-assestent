# https://www.google.com/search?q=weather+of+bengaluru
# user agent-----> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
# span id = wob_tm

# from requests_html import HTMLSession
# import speech_to_text

# s  =  HTMLSession()
# query = "Bengaluru"
# url = f'https://www.google.com/search?q=weather+{query}'
# r = s.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
# temp = r.html.find("span#wob_tm" , first= True).text
# print(temp)
# unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
# print(unit)
# desc = r.html.find('span#wob_dc' , first= True).text
# print(desc)




# from requests_html import HTMLSession
# import speech_to_text


# def weather():
#     s = HTMLSession()
#     query = "Bengaluru"
#     url = f'https://www.google.com/search?q=weather+{query}'
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
#     }

#     r = s.get(url, headers=headers)
#     # Try to locate elements safely
#     temp_el = r.html.find('span#wob_tm', first=True).text
#     unit_el = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
#     desc_el = r.html.find('span#wob_dc', first=True).text
#     return temp_el+" " + unit_el+" " + desc_el






# if not temp_el:
#     print("⚠️ Temperature not found — Google may have changed layout or blocked the request.")
# else:
#     temp = temp_el.text
#     print("Temperature:", temp)

# if unit_el:
#     unit = unit_el.text
#     print("Unit:", unit)
# else:
#     print("⚠️ Unit not found.")

# if desc_el:
#     desc = desc_el.text
#     print("Condition:", desc)
# else:
#     print("⚠️ Description not found.")




from requests_html import HTMLSession

def weather(city="Bengaluru"):
    s = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{city}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/141.0.0.0 Safari/537.36'
    }

    r = s.get(url, headers=headers)

    # Safely find elements
    temp_el = r.html.find('span#wob_tm', first=True)
    unit_el = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    desc_el = r.html.find('span#wob_dc', first=True)

    if not temp_el or not unit_el or not desc_el:
        print("⚠️ Could not fetch weather details — Google blocked or changed layout.")
        return "Sorry, I couldn't fetch the weather right now."

    temp = temp_el.text
    unit = unit_el.text
    desc = desc_el.text

    result = f"The temperature in {city} is {temp}{unit} with {desc.lower()}."
    print(result)
    return result
