# # import pandas as pn
# # data=[
# #   {
# #     'name':'John',
# #     'age':25,
# #     'city':'New York'
# #   },
# #   {
# #     'name':'Jane',
# #     'age':28,
# #     'city':'Los Angeles'
# #   },
# #   {
# #     'name':'Bob',
# #     'age':30,
# #     'city':'Chicago'
# #   }
# # ]
# # # print(data)

# # res=pn.DataFrame(data)
# # print(res)
# # print("--------------------------------")
# # data2=[1,2,3,4,5]
# # res2=pn.DataFrame(data2,index=['a','b','c','d','e'])
# # print(res2)
# # print("--------------------------------")
# # res3=pn.Series(data2,index=['a','b','c','d','e'])

# # print(res3)

# import pandas as pn

# data=pn.read_csv('makeup.csv')
# # print(data)
# print(data.head())
# print("\n================================")
# print(data.tail())

import time
print("please wait ....")
time.sleep(5)
print("done")