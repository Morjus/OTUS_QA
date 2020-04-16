import json
from csv import DictReader

result_list = []

with open("books.csv", "r") as books, \
    open("users.json", "r") as users, \
        open("result.json", "w") as res_file:

    books = DictReader(books)
    users = json.loads(users.read())
    for user in users:
        try:
            book = (next(books))
            result = {"name": user["name"],
                      "gender": user["gender"],
                      "address": user["address"],
                      "books": [
                {
                    "title": book["Title"],
                    "author": book["Author"],
                    "height": book["Height"]
                }
            ]}
            result_list.append(result)
        except StopIteration:
            break
    json.dump(result_list, res_file, indent=4)
