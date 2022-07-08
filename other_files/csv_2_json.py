import pandas as pd

f = 'ApiTimeout-Service.csv'
df = pd.read_csv(f)

col = df.columns.to_list
dict_ = {'url': None, 'apis': None}
urls = []
api_ep = {}
for index, val in enumerate(df['UI URL']):
    urls.append(val)
    api_ep[index] = [df.iloc[index][1], df.iloc[index][2], df.iloc[index][3]]
    print(urls[len(urls)-1])
    print(api_ep[list(api_ep.keys())[len(list(api_ep.keys()))-1]])

dict_['url'] = urls
dict_['apis'] = api_ep

print("success...")

# urls = []
# api_ep = []
# print(col)
# for index, val in enumerate(df[]):
#     urls.append(val)
#     i_ = {}
#     i_[df.iloc[index][1]] = [df.iloc[index][2], df.iloc[index][3]]
#     print(i_)
