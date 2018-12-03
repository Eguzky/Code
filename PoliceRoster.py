from pprint import pprint

policeRoster = {}

policeRoster["Male"] = {}
policeRoster["Female"] = {}

policeRoster["Male"]["Bill"] = {"Name" : "Bill Tedderson", "Rank" : "Officer"}
policeRoster["Female"]["Wendy"] = {"Name" : "Wendy Smith", "Rank" : "Sargeant"}
pprint(policeRoster)
#print(policeRoster["Male"])
#print(policeRoster["Male"]["Bill"])
#print(policeRoster["Male"]["Bill"]["Rank"])

officer = input("Type An Officer's Name: ").capitalize()
gender = ''
if officer in policeRoster["Male"]:
    #check if male, if found in males, then
    gender = "Male"
elif officer in policeRoster["Female"]:
    #check if female, if found in female, then
    gender = "Female"
else:
    print("Not In Roster. Check Spelling And Input Again.")
if gender != "":
    pprint(policeRoster[gender][officer])