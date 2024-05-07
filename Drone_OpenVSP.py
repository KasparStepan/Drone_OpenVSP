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



fuselage = vsp.AddGeom("FUSELAGE")
fuselage_length  = 0.9
## Setting of overall length
vsp.SetParmVal(fuselage,"Length","Design",fuselage_length)
vsp.SetParmVal(fuselage, "X_Rel_Location", "XForm",-0.1)
vsp.SetParmVal(fuselage, "Z_Rel_Location", "XForm",-0.035/1.2)
vsp.Update()

## Setting of crossections
xsec_fuselage = vsp.GetXSecSurf(fuselage, 0)
vsp.ChangeXSecShape(xsec_fuselage,1,vsp.XS_GENERAL_FUSE)

vsp.ChangeXSecShape(xsec_fuselage,2,vsp.XS_GENERAL_FUSE)

vsp.ChangeXSecShape(xsec_fuselage,3,vsp.XS_GENERAL_FUSE)
vsp.Update()

## number of cross sections: 5
## adding one cross section
vsp.InsertXSec(fuselage,3, vsp.XS_GENERAL_FUSE)
vsp.InsertXSec(fuselage,3, vsp.XS_GENERAL_FUSE)
vsp.Update()
## Fuselage crossection: 0
fuselage_section = "XSec_0"
vsp.SetParmVal(fuselage, "TopLAngle", fuselage_section, 85)
vsp.SetParmVal(fuselage, "TopLStrength",fuselage_section,0.75)
vsp.SetParmVal(fuselage, "RightLAngle", fuselage_section, 85)
vsp.SetParmVal(fuselage, "RightLStrength",fuselage_section,0.75)
vsp.Update()


## Fuselage crossection: 1
fuselage_section = "XSec_1"
vsp.SetParmVal(fuselage, "XLocPercent", fuselage_section, 0.05/fuselage_length)
vsp.SetParmVal(fuselage, "SectTess_U", fuselage_section, 10)
vsp.Update()
fuselage_section_shape = "XSecCurve_1"
vsp.SetParmVal(fuselage,"Width",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage,"Height",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage, "TopStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "BotStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "UpStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "LowStr",fuselage_section_shape,1)
vsp.Update()
## Fuselage crossection: 2
fuselage_section = "XSec_2"
vsp.SetParmVal(fuselage, "XLocPercent", fuselage_section, 0.1/fuselage_length)
vsp.SetParmVal(fuselage, "SectTess_U", fuselage_section, 10)
vsp.Update()
fuselage_section_shape = "XSecCurve_2"
vsp.SetParmVal(fuselage,"Width",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage,"Height",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage, "TopStr",fuselage_section_shape,1.5)
vsp.SetParmVal(fuselage, "BotStr",fuselage_section_shape,0.83)
vsp.SetParmVal(fuselage, "UpStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "LowStr",fuselage_section_shape,0.75)
vsp.Update()
## Fuselage crossection: 3
fuselage_section = "XSec_3"
vsp.SetParmVal(fuselage, "XLocPercent", fuselage_section, 0.25)
vsp.SetParmVal(fuselage, "SectTess_U", fuselage_section, 10)
vsp.Update()
fuselage_section_shape = "XSecCurve_3"
vsp.SetParmVal(fuselage,"Width",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage,"Height",fuselage_section_shape,0.07)
vsp.SetParmVal(fuselage, "TopStr",fuselage_section_shape,1.5)
vsp.SetParmVal(fuselage, "BotStr",fuselage_section_shape,0.83)
vsp.SetParmVal(fuselage, "UpStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "LowStr",fuselage_section_shape,0.75)
vsp.Update()

## Fuselage crossection: 4
fuselage_section = "XSec_4"
vsp.SetParmVal(fuselage, "XLocPercent", fuselage_section, 0.45)
vsp.SetParmVal(fuselage, "ZLocPercent", fuselage_section, 0.035/1.5)
vsp.SetParmVal(fuselage, "SectTess_U", fuselage_section, 20)
vsp.Update()
fuselage_section_shape = "XSecCurve_4"
vsp.SetParmVal(fuselage,"Width",fuselage_section_shape,0.02)
vsp.SetParmVal(fuselage,"Height",fuselage_section_shape,0.035/2)
vsp.SetParmVal(fuselage, "TopStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "BotStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "UpStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "LowStr",fuselage_section_shape,1)
vsp.Update()
## Fuselage crossection: 5
fuselage_section = "XSec_5"
vsp.SetParmVal(fuselage, "XLocPercent", fuselage_section, 0.9)
vsp.SetParmVal(fuselage, "ZLocPercent", fuselage_section, 0.035/1.5)
vsp.SetParmVal(fuselage, "SectTess_U", fuselage_section, 10)
vsp.Update()
fuselage_section_shape = "XSecCurve_5"
vsp.SetParmVal(fuselage,"Width",fuselage_section_shape,0.02)
vsp.SetParmVal(fuselage,"Height",fuselage_section_shape,0.035/2)
vsp.SetParmVal(fuselage, "TopStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "BotStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "UpStr",fuselage_section_shape,1)
vsp.SetParmVal(fuselage, "LowStr",fuselage_section_shape,1)
vsp.Update()

## Fuselage crossection: 6
fuselage_section = "XSec_6"
vsp.SetParmVal(fuselage, "ZLocPercent", fuselage_section, 0.035/1.5)
vsp.SetParmVal(fuselage, "TopLAngle", fuselage_section, -85)
vsp.SetParmVal(fuselage, "TopLStrength",fuselage_section,0.45)
vsp.SetParmVal(fuselage, "RightLAngle", fuselage_section, -85)
vsp.SetParmVal(fuselage, "RightLStrength",fuselage_section,0.45)
vsp.Update()





vsp.WriteVSPFile("test.vsp3")
