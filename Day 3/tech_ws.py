def tech_ws(d1,d2,d3):
    d1=normalize(d1)
    d2=normalize(d2)
    d3=normalize(d3)
    print("Total number of unique attendees: ",len(d1)+len(d2)+len(d3))
    print("Attendees who attended all three days: ",d1&d2&d3)
    print("The list of attendees who attended exactly one day: ",(d1-d2-d3)|(d2-d1-d3)|(d3-d2-d1))
    print("Pairwise overlap counts are: ",len(d1&d2),len(d2&d3),len(d1&d3))
    print("Sorted lists: ",sorted(d1),sorted(d2),sorted(d3))
def normalize(d):
    for i in d:
        i=i.lower()
    return set(d)
tech_ws(['ab','bc','cd','ef'],['ab','eo','rp','fi'],['ab','bc','cd','xy'])