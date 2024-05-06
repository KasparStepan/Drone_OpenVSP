import openvsp as vsp
import numpy as np

vsp.VSPRenew()
vsp.ClearVSPModel()

## Main wing 
main_wing = vsp.AddGeom("WING")
vsp.InsertXSec(main_wing,1,vsp.XS_FOUR_SERIES)

# Center section

section = "XSec_1"
vsp.SetParmVal(main_wing,"Span",section, 0.5 )
vsp.SetParmVal(main_wing,"Root_Chord",section, 0.07)
vsp.SetParmVal(main_wing,"Tip_Chord",section, 0.07)
vsp.SetParmVal(main_wing,"Sweep", section, 0)
vsp.SetParmVal(main_wing,"Dihedral", section, 0)
vsp.SetParmVal(main_wing,"Twist", section, 0)


vsp.Update()

# Tip section
section = "XSec_2"
vsp.SetParmVal(main_wing,"Span",section, 0.25 )
vsp.SetParmVal(main_wing,"Root_Chord",section, 0.07)
vsp.SetParmVal(main_wing,"Tip_Chord",section, 0.03)
vsp.SetParmVal(main_wing,"Sweep", section, 5)
vsp.SetParmVal(main_wing, "Dihedral", section, 10)
vsp.SetParmVal(main_wing, "Twist", section, 0)
vsp.SetParmVal(main_wing,"Sweep_Location", section, 0)
vsp.SetParmVal(main_wing,"Sec_Sweep_Location",section,1)
vsp.Update()


## Tail wing 
tail_wing = vsp.AddGeom("WING")
'''
xsec_tail_wing = vsp.GetXSecSurf(tail_wing,0)
print(xsec_tail_wing)
vsp.ChangeXSecShape(xsec_tail_wing,0,vsp.XS_FOUR_SERIES)
print(vsp.GetXSecParmIDs(xsec_tail_wing))
'''
section = "XSec_1"
vsp.SetParmVal(tail_wing,"Span",section, 0.25 )
vsp.SetParmVal(tail_wing,"Root_Chord",section, 0.1)
vsp.SetParmVal(tail_wing,"Tip_Chord",section, 0.03)
vsp.SetParmVal(tail_wing,"Sweep", section, 0)
vsp.SetParmVal(tail_wing, "Dihedral", section, 30)
vsp.SetParmVal(tail_wing, "X_Rel_Location", "XForm",0.65)

vsp.Update()


vsp.WriteVSPFile("test.vsp3")
