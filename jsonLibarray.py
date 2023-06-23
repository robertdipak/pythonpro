import json
datas='{"name":"John", "age":30}'
x = {
  "name": "John",
  "age": 30,
  "city": "123"
}
json.loads(x)
json.loads(datas)


# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# data ='{
#     "user":["user1", "user2","user3"],
#     "password":["123","456","121"]
# }'
# jsonget= j.loads(data)