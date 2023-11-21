import json

with open ("homework\\try_json.json") as f:
    d=json.load(f)

d["hi"]=456

with open ("hi_dict.json","x") as a:
    json.dump(d,a)

print (d)