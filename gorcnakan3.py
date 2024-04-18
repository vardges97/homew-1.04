# def letterfrequency(ls):
#     di = {}
#     for i in ls:
#         if di.get(i):
#             di[i]+=1
#         else:
#             di[i]=1
#     return di
#
# ls1=('Hello There Thane Andrew Holmes')
# x=letterfrequency(ls1)
# print(x)

# def wordchecker(ls):
#     res = set(ls)
#     if len(ls)==len(res):
#         print('all words are unique')
#     else:
#         print('not all words are unique')
#     return res
# ls1 = ['hello','hi','bye','hi','die']
# print(wordchecker(ls1))


# groce={'ham':8,'cheese':3.5,'egg':0.5,'bread':1.3}
# del groce['ham']
# print(groce)

# set1 = {'apple','pear','banana'}
# set2 = {'apple','microsoft','linux'}
#
# res = set1 ^ set2
# print(res)


# def letterfrequency(word,key):
#     di = {}
#     for i in word:
#         if i == key:
#             if di.get(i):
#                 di[i]+=1
#             else:
#                 di[i]=1
#     return di
#
# sent='Hello There Thane Andrew Holmes'
# x=letterfrequency(sent,'l')
# print(x)

# my_list = [1, 2, 3, 3, 4, 5, 5]
# # my_set = set(my_list)
# # print(my_set)
# my_set= {x for x in my_list}
# print(my_set)

# def dictchecker(dict,item):
#     if item in dict:
#         print('item exists in dict')
#     else:
#         print('item doesnt exist in dict')
#
# dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# print(dictchecker(dict1,'key1'))

# fruit = {'apple','pear','peach','cherry','plum'}
# pies = {'apple','cherry','pecan','strawberry'}
#
# res = fruit ^ pies
# print(res)

# dict1={"a":4,'b':5,'c':3}
# dict1.update({'a':1,'b':2})
# print(dict1)

fruit = {'apple','pear','peach','cherry','plum'}
pies = {'apple','cherry'}

# def setchecker(set1,set2):

# def setcomp(set1,set2):
#     if len(set1)>len(set2):
#         print (f'first set is larger than the second')
#     else:
#         print (f'second set is larger than the first')
# print(setcomp(pies,fruit))

dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
def dictkeys(dict):
    ls=[]
    for key in dict.keys():
        ls.append(key)
    return ls
print(dictkeys(dict1))

def dictvalues(dict):
    ls=[]
    for val in dict.values():
        ls.append(val)
    return ls
print(dictvalues(dict1))

dict1['key4']='value4'
print(dict1)