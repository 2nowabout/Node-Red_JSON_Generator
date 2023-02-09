import json

newTopic = input("Type new ID from sensor. Export will be smartys-{ID}/topic")

file = open("flows.json")

data = json.load(file)

for i in data:
    print(i)
    for k,v in i.items():
        if k == "topic":
            i[k] = v.replace("17884B000DFD", newTopic)
    print(i)

json_object = json.dumps(data)

# Writing to sample.json
with open(newTopic +".json", "w") as outfile:
    outfile.write(json_object)