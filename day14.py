import requests



# online_url = "https://markets.onlinekhabar.com/smtm/home/advance-decline/nepse"


# r = requests.get(url=online_url)
# if r.status_code == 200:
#     data = r.json()
#     final_data = data["response"]
#     for i in final_data:
#         print(f'{i["indices"]}   {i["turnover"]} ')
    

# else:
#     print("something went wrong")


# url = "https://markets.onlinekhabar.com/smtm/home/market-status"

# r = requests.get(url=url)
# if r.status_code == 200 :
#     data = r.json()
#     # print(type(data))
#     # print(data.keys())
#     final_data = data['response']
#     # print(type(final_data))
#     for i in final_data:
#         print(i['market_live'])
# else:
#     print(f'Error')



url = "https://www.fotmob.com/api/data/matchDetails?matchId=4653848"
r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()
    print(type(data))
    print(data.keys())
    data_final = data["header"]
    print(type(data_final))
    final_data = data_final["teams"]
    print(type(final_data))
    for i in final_data:
        print(f''' {i["name"] } {i["score"]} ''')

else:
    print("ERROR")