def get_num_words(text):
    words = text.split()
    return len(words)

def new_func(text):
    dict={}
    for i in text.lower():
        if i in dict:
            dict[i] +=1
        else:
            dict[i]= 1
    return dict
    
def sortnas(list):
    return list["num"]
def sorting(dict):
    liste=[]
    for i in dict:
        if i.isalpha():
            newdic = {}
            newdic["char"] = i
            newdic["num"] = dict[i]
            liste.append(newdic)
    liste.sort(reverse = True,key = sortnas)
    return liste