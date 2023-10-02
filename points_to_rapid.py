import numpy as np

INPUT = open("example_paths.txt", "r").read()
HOME = "\tCONST robtarget home:=[[647.048869176,0,659.200917087],[0.608761434,-0.000000006,0.793353337,-0.000000005],[0,-1,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n"
OUTPUT = open("RAPID.txt", "w")

def main():
    OUTPUT.write("MODULE Module1\n")
    OUTPUT.write(HOME)
    points = define_constants()
    paths = input_to_paths(points)
    path_names = define_paths(paths)
    OUTPUT.write("\tPROC main()\n")
    OUTPUT.write("\t\tMoveJ home,v100,z1,pen\WObj:=wobj0;\n")
    for name in path_names:
        OUTPUT.write(f"\t\t{name};\n")
    OUTPUT.write("\t\tMoveJ home,v100,z1,pen\WObj:=wobj0;\n")
    OUTPUT.write("\tENDPROC\nENDMODULE")

def target_string(name, x, y):
    return f"\tCONST robtarget {name}:=[[{x},{y},0],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n"

def define_constants():
    point_input = [tuple(row.split(" ")) for row in INPUT.split("\n") if row]
    points = dict()
    for i, p in enumerate(point_input):
        name = f"p{i}"
        points[p] = name
        OUTPUT.write(target_string(name, p[0], p[1]))
    return points

def input_to_paths(points):
    "creates a list of lists containing paths with points"
    paths = INPUT.split("\n\n")
    return [[points[tuple(p.split(" "))] for p in path.split("\n")] for path in paths]

def define_paths(paths):
    path_names = []
    for i, path in enumerate(paths):
        name = f"path{i}"
        path_names.append(name)
        OUTPUT.write(f"\tPROC {name}()\n")
        OUTPUT.write(f"\t\tMoveJ {path[0]},v100,z5,pen\WObj:=Workobject_1;\n")
        for p in path:
            OUTPUT.write(f"\t\tMoveL Offs({p},0,0,15),v100,z1,pen\WObj:=Workobject_1;\n")
        OUTPUT.write(f"\t\tMoveL {path[-1]},v100,z1,pen\WObj:=Workobject_1;\n")
        OUTPUT.write(f"\tENDPROC\n")
    return path_names

if __name__ == "__main__":
    main()
