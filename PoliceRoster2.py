from pprint import pprint

policeRoster = {}

policeRoster["Male"] = {}
policeRoster["Female"] = {}

policeRoster["Male"]["Bill"] = {"Name" : "Bill Tedderson", "Rank" : "Officer"}
policeRoster["Male"]["Ted"] = {"Name" : "Ted Billington", "Rank" : "Lieutenant"}
policeRoster["Male"]["Bob"] = {"Name" : "Robert Walker", "Rank" : "Officer"}
policeRoster["Female"]["Wendy"] = {"Name" : "Wendy Smith", "Rank" : "Sargeant"}
policeRoster["Female"]["Betty"] = {"Name" : "Betty Liu", "Rank" : "Officer"}
policeRoster["Female"]["Mae"] = {"Name" : "Mae Strait", "Rank" : "Sargeant"}


policeRosterNew = {}
for x in policeRoster:
    for y in policeRoster[x]:
        policeRosterNew[y] = policeRoster[x][y]
        policeRosterNew[y]["Gender"] = x

policeRoster = policeRosterNew.copy()
del policeRosterNew

order = ["Name", "Gender", "Rank"]

officer = input("Type An Officer's Name: ").capitalize()
if officer in policeRoster:
    for key in order:
        print("{0}: {1}".format(key, policeRoster[officer][key]))
else:
    print("Not In Roster. Check Spelling And Input Again.")