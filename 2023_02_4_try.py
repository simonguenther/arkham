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

# None -> [1,6]
# 1 -> [3,4]
# 2 -> []
# 3 -> [2]
# 4 -> []
# 5 -> []
# 6 -> [5]

helper = {}
def run() -> None:
    for p in positions:
        parent_id = p.get("parent_id", None)
        if parent_id not in helper: helper[parent_id] = [p]
        else: helper[parent_id].append(p)

    pprint.pprint(helper)
    root = helper.get(None, [])
    for edge in root:
        level = 0
        recursion(edge, level)

def recursion(edge, level):
    prefix = level * "-"
    print(f"{prefix}{edge['name']}")
    for edge2 in helper.get(edge["id"], []):
        recursion(edge2, level+1)

if __name__ == "__main__":
    positions = sorted(positions, key=lambda x:x["name"])
    #pprint.pprint(positions)
    run()