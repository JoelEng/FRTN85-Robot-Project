MODULE Module1
	CONST robtarget home:=[[647.048868563,0,659.200914799],[0.608761429,0,0.79335334,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget paper_1:=[[0,50,15],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget paper_2:=[[100,100,15],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget paper_3:=[[0,150,15],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget air_1:=[[0,50,-100],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget air_2:=[[100,100,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget air_3:=[[0,150,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget L1:=[[100,0,0],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget L2:=[[0,0,0],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget L3:=[[0,50,0],[1,0,0,0],[0,0,-2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    VAR robtarget sp_1;
    VAR robtarget sp_2;
    VAR robtarget sp_3;
    !***********************************************************
    !
    ! Module:  Module1
    !
    ! Description:
    !   <Insert description here>
    !
    ! Author: el4271ba-s
    !
    ! Version: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedure main
    !
    !   This is the entry point of your program
    !
    !***********************************************************
    PROC main()
        MoveJ air_1,v10,z1,tool1\WObj:=Workobject_1;
        SearchL \Stop, DI10_0, sp_1, paper_1, v10, tool1\WObj:=Workobject_1;
        MoveJ air_2,v10,z1,tool1\WObj:=Workobject_1;
        SearchL \Stop, DI10_0, sp_2, paper_2, v10, tool1\WObj:=Workobject_1;
        MoveJ air_3,v10,z1,tool1\WObj:=Workobject_1;
        SearchL \Stop, DI10_0, sp_3, paper_3, v10, tool1\WObj:=Workobject_1;
        MoveJ air_3,v10,z1,tool1\WObj:=Workobject_1;
        Workobject_1.oframe := DefDframe (paper_1, paper_2, paper_3, sp_1, sp_2, sp_3);
        !PDispSet Workobject_1.oframe;
        Path_L;
    ENDPROC
    
    PROC Path_L()
	    MoveJ Offs(L1,0,0,4),v10,z1,tool1\WObj:=Workobject_1;
        MoveL Offs(L2,0,0,4),v10,z1,tool1\WObj:=Workobject_1;
	    MoveL Offs(L3,0,0,4),v10,z1,tool1\WObj:=Workobject_1; 
        MoveJ home,v10,z100,tool1\WObj:=Workobject_1;
	ENDPROC
ENDMODULE