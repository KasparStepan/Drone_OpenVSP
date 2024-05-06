import openvsp as vsp
import numpy as np
import os

vsp.VSPRenew()
vsp.ClearVSPModel()

## Main wing 
main_wing = vsp.AddGeom("WING")
xsec_main_wing = vsp.GetXSecSurf(main_wing, 0 )

## Split wing into two sections
vsp.InsertXSec(main_wing,1,vsp.XS_FILE_AIRFOIL)


## Set crossection to use dat file for airfoil import

vsp.ChangeXSecShape(xsec_main_wing,0,vsp.XS_FILE_AIRFOIL)
xsec_1 = vsp.GetXSec(xsec_main_wing, 0)
vsp.ReadFileAirfoil(xsec_1, 'airfoil_database/rg15.dat')
vsp.Update()



vsp.ChangeXSecShape(xsec_main_wing,1,vsp.XS_FILE_AIRFOIL)
xsec_2 = vsp.GetXSec(xsec_main_wing, 1)
vsp.ReadFileAirfoil(xsec_2, "airfoil_database/rg15.dat")
vsp.Update()



vsp.ChangeXSecShape(xsec_main_wing,2,vsp.XS_FILE_AIRFOIL)
xsec_3 = vsp.GetXSec(xsec_main_wing, 2)
vsp.ReadFileAirfoil(xsec_3, "airfoil_database/rg15.dat")
vsp.Update()


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

xsec_tail_wing = vsp.GetXSecSurf(tail_wing,0)
vsp.ChangeXSecShape(xsec_tail_wing,0,vsp.XS_FOUR_SERIES)
vsp.Update()

# Airfoil parameters
vsp.SetParmVal(tail_wing,"ThickChord","XSecCurve_0",0.12)
vsp.SetParmVal(tail_wing,"Camber","XSecCurve_0",0)

vsp.Update()

vsp.SetParmVal(tail_wing,"ThickChord","XSecCurve_1",0.12)
vsp.SetParmVal(tail_wing,"Camber","XSecCurve_1",0)

vsp.Update()


section = "XSec_1"
vsp.SetParmVal(tail_wing,"Span",section, 0.25 )
vsp.SetParmVal(tail_wing,"Root_Chord",section, 0.1)
vsp.SetParmVal(tail_wing,"Tip_Chord",section, 0.03)
vsp.SetParmVal(tail_wing,"Sweep", section, 0)
vsp.SetParmVal(tail_wing, "Dihedral", section, 30)
vsp.SetParmVal(tail_wing, "X_Rel_Location", "XForm",0.65)
vsp.SetParmVal(tail_wing,"Sec_Sweep_Location",section,0.01)
vsp.SetParmVal(tail_wing,"Sweep_Location", section, 1)





vsp.Update()


vsp.WriteVSPFile("test.vsp3")
