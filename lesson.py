def main():
    dict_1 = {1:"1",2:"2",3:"3"}
    dict_2 = {4:"4",5:"5",6:"6"}

    list_1 = [1,2,3,4]
    list_2 = [5,6,7,8]

    dict3 = {**dict_1,**dict_2}

    return dict3, list_1 +list_2
print(main())
print(dir(dict))


# def merge_twoDict(a, b): 
#     return(a.update(b)) 
# a = {1:"1",2:"2",3:"3"} 
# b = {4:"4",5:"5",6:"6"}           
# merge_twoDict(a, b)  
# print(a)

