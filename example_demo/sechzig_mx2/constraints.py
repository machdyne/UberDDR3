#!/usr/bin/env python3
ddr3_name = 'ddr3_top_inst.ddr3_phy_inst'
def get_cells(name_part):
    return list(map(lambda c: c.second, filter(lambda c: name_part in c.first, ctx.cells)))

def get_cell(name_part):
    return get_cells(name_part)[0]

c1=get_cell(ddr3_name + '.genblk5[0].ISERDESE2_train')
c3=get_cell(ddr3_name + '.genblk5[0].OSERDESE2_train')
c2=get_cell(ddr3_name + '.genblk5[1].ISERDESE2_train')
c4=get_cell(ddr3_name + '.genblk5[1].OSERDESE2_train')

c1.setAttr('BEL', 'ILOGIC_X0Y27/ISERDESE2')
c3.setAttr('BEL', 'OLOGIC_X0Y27/OSERDESE2')
c2.setAttr('BEL', 'ILOGIC_X0Y25/ISERDESE2')
c4.setAttr('BEL', 'OLOGIC_X0Y25/OSERDESE2')
