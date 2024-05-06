import openvsp as vsp
import numpy as np

class Main_wing:
    def __init__(self):
        self.wing_id = vsp.AddGeom("WING")
        self.number_of_sections 


vsp.ClearVSPModel()


wing_id = vsp.AddGeom("WING")
vsp.SetParmVal(wing_id,"Span","XSec_1",2)
vsp.Update()
vsp.WriteVSPFile("blank.vsp3")






















