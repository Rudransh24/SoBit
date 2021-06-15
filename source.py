import csv, sys, pandas as pd

#df -> dataframe with 4 columns
df = pd.read_csv('mempool.csv')

#filling empty parent ids with string "na"
df = df.fillna("na")
#sys.stdout = open('source_sol/block.txt', 'w')

#converting all columns into separate lists
txt_id = df["tx_id"].tolist()
fees = df["fee"].tolist()
weight = df["weight"].tolist()
parent_id = df["parents "].tolist()

#final list of all transanctions to be stored inside a block
f_fee = []
f_weight = []
f_txt = []

#converting parent ids(strings) into list of strings separated by semi-colon
#using list comprehension to reduce time...
parent_id = [item.split(';') for item in parent_id]

#using dictionary to keep track of parent ids if they occur before tx_id(child)
dict = {}
n = len(parent_id)

for i in range(0, n):

    y = txt_id[i]
    if y not in dict:
        dict[y] = 1
    flag = 0
    x = parent_id[i]
    for j in range(0, len(x)):
        if x[j] == 'na':
            break
        else:
            if x[j] not in dict:
                flag = 1
                break
    
    if flag == 0:
        f_fee.append(fees[i])
        f_weight.append(weight[i])
        f_txt.append(txt_id[i])

#Now, we have f_fee, f_weight and f_txt as final fees, weight and ids that can be a part of the BLOCK.
#Converting f_fee, f_weight and f_txt into dataframe, then sort them according to their weights/fees/fee_by_weight --> greedy knapsack approach....

#data frame final which sorts the data in descending order in terms of fee
df_final = pd.DataFrame({"tx_id": f_txt, "fee": f_fee,
                        "weight": f_weight})
df_final = df_final.sort_values(by="fee", ascending=False)

W1 = 4000000 #by fees
W2 = 4000000 #by weight
W3 = 4000000 #by fees/weight

dict1 = {} #fees
dict2 = {} #weight
dict3 = {} #fees/weight

sol1 = 0 #maximum amount greedy by fees
sol2 = 0 #maximum amount greedy by weight
sol3 = 0 #maximum amount greedy by fees/weight

f_list1 = [] #final list of all chosen ids using greedy knapsack -> fees
f_list2 = [] #final list of all chosen ids using greedy knapsack -> weight
f_list3 = [] #final list of all chosen ids using greedy knapsack -> fees/weight

#by fees
for i in df_final.index:

    if df_final.at[i, "weight"] <= W1:
        W1 -= df_final.at[i, "weight"]
        sol1 += df_final.at[i, "fee"]
        dict1[df_final.at[i, "tx_id"]] = 1


for i in range(0, len(f_txt)):
    if f_txt[i] in dict1:
        f_list1.append(f_txt[i])

#by weight
#data frame final which sorts the data in ascending order in terms of weight
df_final = df_final.sort_values(by="weight", ascending=True)

for i in df_final.index:

    if df_final.at[i, "weight"] <= W2:
        W2 -= df_final.at[i, "weight"]
        sol2 += df_final.at[i, "fee"]
        dict2[df_final.at[i, "tx_id"]] = 1


for i in range(0, len(f_txt)):
    if f_txt[i] in dict2:
        f_list2.append(f_txt[i]) 

#data frame final which sorts the data in descending order in terms of fee/weight
df_final["fee_by_weight"] = df_final.apply(lambda x: x["fee"]/x["weight"], axis=1)
df_final = df_final.sort_values(by="fee_by_weight", ascending=False)

for i in df_final.index:

    if df_final.at[i, "weight"] <= W3:
        W3 -= df_final.at[i, "weight"]
        sol3 += df_final.at[i, "fee"]
        dict3[df_final.at[i, "tx_id"]] = 1


for i in range(0, len(f_txt)):
    if f_txt[i] in dict3:
        f_list3.append(f_txt[i])


#checking which value is maximum and storing corresponding list of all transaction ids in block.txt
x = max(sol1, sol2, sol3)

if x == sol1:
    for item in f_list1:
        print(item)
elif x == sol2:
    for item in f_list2:
        print(item)
else:
    for item in f_list3:
        print(item)


