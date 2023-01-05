import json
dicc = [
    {
        "id": 1,
        "title": "Silmarillion",
        "author": "J. R. R. Tolkien",
        "availablity": True
    },

   {
        "id": 2,
        "title": "Voina i mir",
        "author": "L.N. Tolstoi",
        "availablity": True
    },
   {
        "id": 3,
        "title": "Skazki",
        "author": "A.S. Pushkin",
        "availablity": True
    }
]

def proverka_tok(func):
    def wrapper(dic):
        for k,v in dic.items():
            if dic[k]=="testtoken":
                print('Проверка прошла. Токен верный')
                return func(dic)
            elif dic[k] != "testtoken":
                print('Нет права пользования библиотекой')
                break

    return wrapper

@proverka_tok
def f_vid_book(dic):##Функция проверяет наличие книги и меняет флаг в файле library.json
    global key
    query = {}
    for i,v in dic.items():
        if i == 'data':
            query = v
        # print(query)#Sozdali slovar-kluch s id knigi
        for k in query:
            key = query[k]
            # print(key)

        #print(i)#token, action, data
        # print(v)#testtoken, getbook, {'id': 2}

    with open('library.json', 'w', encoding='utf-8') as f:
        json.dump(dicc, f)

    with open('library.json', 'r', encoding='utf-8') as f:

       d = []
       read = json.load(f)#, ensure_ascii=False
       for i in read:
           d.append(i)
       # print(d)
       # [{'id': 1, 'title': 'Silmarillion', 'author': 'J. R. R. Tolkien', 'availablity': True},
       #  {'id': 2, 'title': 'Voina i mir', 'author': 'L.N. Tolstoi', 'availablity': True},
       #  {'id': 3, 'title': 'Skazki', 'author': 'A.S. Pushkin', 'availablity': True}]

       keys = []
       for i in d:
           if key == i.get('id'):
               keys.append(i.get('id'))
               # print('keys_ = ', keys)

               ff = i.get('title')
               print(f'Книга {ff} с id {key} доступна')#Книга Voina i mir с id 2 доступна
    #        print(i.get('id'))#1,2,3
               #Smenim flag v library.json na False
               for i in dicc:
                   #print(i)#{'id': 1, 'title': 'Silmarillion', 'author': 'J. R. R. Tolkien', 'availablity': True}
                   if i.get('id') == key:#1,2,3
                        i["availablity"] = False
                        # print(i.get("availablity"))#False
                        #############Zapishem v library.json

                        with open('library.json', 'w', encoding='utf-8') as f:
                            json.dump(dicc, f)
           if key != i.get('id'):
               keys.append(i.get('id'))
               # print('keys', keys)

       if key not in keys:
           print('Такой книги нет')


f_vid_book({
    "token": "testtoken",# // уникальный токен пользователя
    "action": "getbook", #// действие взять книгу
    "data": { #// набор данных, которые передает пользователь
        "id": 2 #// уникальный идентификатор книги
    }
})
