# Designer
# -UX Designer
# Engineer
# -Mechanical Engineer
# -Software Engineer
# --Front-End Engineer
import pprint

positions = [ {"id":1, "name":"Engineer", "parent_id":None},
              {"id":2, "name":"Front-End Engineer", "parent_id":3},
              {"id":3, "name":"Software Engineer", "parent_id":1},
              {"id":4, "name":"Mechanical Engineer", "parent_id":1},
              {"id":5, "name":"UX Designer", "parent_id":6},
              {"id":6, "name":"Designer", "parent_id":None}]


helper_dict = {}

def recursion(level: int, item):
    prefix = "-" * level
    print(f"{prefix}{item['name']}")
    if item["id"] not in helper_dict: 
        return
    helper_dict[item["id"]].sort(key=lambda item: item['name'])
    for children in helper_dict[item["id"]]:
        recursion(level+1, children)
    

for p in positions:
    _id = p.get("id", None)
    _parent = p.get("parent_id", None)

    if _parent not in helper_dict:
        helper_dict[_parent] = [p]
    else:
        helper_dict[_parent].append(p)

root = helper_dict.get(None, [])
root.sort(key=lambda item: item['name'])
#print(root)
#root = sorted(helper_dict.keys(), key=lambda x:x.lower())
# sorted(dictUsers.keys(), key=lambda x:x.lower())
for edge in root:
    prefix_count = 0
    # get name
    # if child is key -> recursive
    recursion(prefix_count, edge)
    prefix_count += 1
    



    
