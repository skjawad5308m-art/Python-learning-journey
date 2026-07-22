info = {
    "name" : "Jawad",
    "age" : 17,
    "nationality" : "Bangladeshi"

}

print(info)
print(list(info))
print(len(list(info)))
print(len(info))
print(type(info))
info["name"] = "MD.Sujnain Jawad"
print(info)
print(list(info))
print(len(info))
print(len(list(info)))
info.keys()
print(info.keys())
print(list(info.keys()))
print(len(info.keys()))
print(len(list(info.keys())))
info.values()
print(info.values())
print(list(info.values()))
print(len(info.values()))
print(len(list(info.values())))
info.items()
print(info.items())
print(list(info.items()))
print(len(info.items()))
print(len(list(info.items())))
info.get("name")
print(info.get('name'))
print(list(info.get("name")))
print(len(info.get("name")))
print(len(list(info.get("name"))))
info.update({"city" : "Dhaka"})
print(info)
print(list(info))
print(len(info))
print(len(list(info)))