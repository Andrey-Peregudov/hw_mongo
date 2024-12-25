
lst = [{"_id": {"$oid": "6764524967010a3f52658667"}, "name": "Vasiliy", "age": "56"},
       {"_id": {"$oid": "676452f3684eca71e31bdd93"}, "name": 1},
       {"_id": {"$oid": "6764536d36237cfa5cdeeed5"}, "name": 1},
       {"_id": {"$oid": "676453df93fa6d46ff4fae21"}, "name": 1},
       {"_id": {"$oid": "6764542712d534cc6123136a"}, "name": 1},
       {"_id": {"$oid": "6764547f379db2ad7b317e11"}, "name": 1},
       {"_id": {"$oid": "676454abf87f6c7be4312fac"}, "name": 1},
       {"_id": {"$oid": "67645b4151a9a3eec8caa179"}, "name": 1},
       {"_id": {"$oid": "67645b93394ef1a52b5abfa4"}, "name": "Kolian", "age": "34"},
       {"_id": {"$oid": "67645b96394ef1a52b5abfa5"}, "name": "Kolian", "age": "34"}]

for i in lst:
    for k, v in i.items():
        print(v)
    # print(i.items())
