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

positions = sorted(positions, key=lambda x: x["name"])
helper = {}

def recursion(edge, level):
    prefix = "-"*level
    print(f"{prefix}{edge['name']}")
    for child in helper.get(edge["id"], []):
        recursion(child, level+1)


for p in positions:
    parent_id = p.get("parent_id", -1)
    if parent_id not in helper: helper[parent_id] = [p]
    else: helper[parent_id].append(p)

pprint.pprint(helper)

roots = helper.get(None, [])
for edge in roots:
    level = 0
    recursion(edge, 0)

