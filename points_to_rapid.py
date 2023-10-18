import numpy as np

def points_to_rapid(path_list):
    OUTPUT = open("RAPID.txt", "w")
    OUTPUT.write("MODULE Module1\n")
    OUTPUT.write("\tCONST robtarget home:=[[647.048869176,0,659.200917087],[0.608761434,-0.000000006,0.793353337,-0.000000005],[0,-1,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    points = define_constants(path_list, OUTPUT)
    write_plane_calibration()
    path_names = define_paths(path_list, OUTPUT, points)
    OUTPUT.write("\tPROC main()\n")
    OUTPUT.write("\t\tMoveJ home,v100,z1,tool1\WObj:=wobj0;\n")
    OUTPUT.write("\t\tplane;\n")
    for name in path_names:
        OUTPUT.write(f"\t\t{name};\n")
    OUTPUT.write("\t\tMoveJ home,v100,z1,tool1\WObj:=wobj0;\n")
    OUTPUT.write("\tENDPROC\nENDMODULE")

def write_plane_calibration():
    OUTPUT.write("\tPROC plane()\n")
    OUTPUT.write("\t\tMoveJ air_1,v50,z1,tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tSearchL \Stop, DI10_0, sp_1, paper_1, v20, tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tMoveJ air_2,v50,z1,tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tSearchL \Stop, DI10_0, sp_2, paper_2, v20, tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tMoveJ air_3,v50,z1,tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tSearchL \Stop, DI10_0, sp_3, paper_3, v20, tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tMoveJ air_3,v50,z1,tool1\WObj:=Workobject_1;\n")
    OUTPUT.write("\t\tWorkobject_1.oframe := DefDframe (paper_1, paper_2, paper_3, sp_1, sp_2, sp_3);\n")
    OUTPUT.write("\tENDPROC\n")

def target_string(name, x, y):
    return f"\tCONST robtarget {name}:=[[{x},{y},0],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n"

def define_constants(path_list, OUTPUT):
    flattened = set([item for sublist in path_list for item in sublist])
    points = dict()
    for i, p in enumerate(flattened):
        name = f"p{i}"
        points[p] = name
        OUTPUT.write(target_string(name, p[0], p[1]))

    # Constants and vars for plane calibration
    OUTPUT.write("\tCONST robtarget paper_1:=[[0,50,15],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tCONST robtarget paper_2:=[[100,100,15],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tCONST robtarget paper_3:=[[0,150,15],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tCONST robtarget air_1:=[[0,50,-100],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tCONST robtarget air_2:=[[100,100,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tCONST robtarget air_3:=[[0,150,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n")
    OUTPUT.write("\tVAR robtarget sp_1;\n")
    OUTPUT.write("\tVAR robtarget sp_2;\n")
    OUTPUT.write("\tVAR robtarget sp_3;\n")
    return points

def define_paths(paths, OUTPUT, points):
    path_names = []
    for i, path in enumerate(paths):
        name = f"path{i}"
        path_names.append(name)
        OUTPUT.write(f"\tPROC {name}()\n")
        OUTPUT.write(f"\t\tMoveJ Offs({points[path[0]]},0,0,5),v100,z5,tool1\WObj:=Workobject_1;\n")
        for p in path:
            if(p != 0):
                OUTPUT.write(f"\t\tMoveL Offs({points[p]},0,0,5),v100,z1,tool1\WObj:=Workobject_1;\n")
        OUTPUT.write(f"\t\tMoveL {points[path[-1]]},v100,z1,tool1\WObj:=Workobject_1;\n")
        OUTPUT.write(f"\tENDPROC\n")
    return path_names