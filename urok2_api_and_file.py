import json
import urllib.request

def read_albums_by_userid(userid):
    url = "https://jsonplaceholder.typicode.com/albums"
    response = urllib.request.urlopen(url)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    list_of_albums_by_id = []
    for item in json_obj:
        if item['userId'] == userid:
            # print("\t", item['id'], "\t", item['title'])
            list_of_albums_by_id.append(item)
    return list_of_albums_by_id

list_from_function = read_albums_by_userid(2)
fo = open('myfile', 'w')
for item in list_from_function:
    new_line = "\t", item['id'], "\t", item['title']
    fo.write(new_line.__str__() + "\n")
fo.close()

with open('myfile') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

