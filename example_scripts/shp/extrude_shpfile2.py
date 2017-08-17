import pyliburo
import shapefile

#specify all the shpfiles
shpfile = "C:\\Users\\smrckwe\\Desktop\\for_omar\\shentonway.shp"
collada_filepath = "C:\\Users\\smrckwe\\Desktop\\for_omar\\shentonway.dae"
stl_filepath = "C:\\Users\\smrckwe\\Desktop\\for_omar\\shentonway.stl"
sf = shapefile.Reader(shpfile)
shapeRecs=sf.shapeRecords()
attrib_name_list = pyliburo.shp2citygml.get_field_name_list(sf)
solid_list = []
cnt = 0
for rec in shapeRecs:
    poly_attribs=rec.record
    height = 70#poly_attribs[0]
    pypolygon_list2d = pyliburo.shp2citygml.get_geometry(rec)
    if pypolygon_list2d:
        pypolygon_list3d = pyliburo.shp2citygml.pypolygon_list2d_2_3d(pypolygon_list2d, 0.0)
        occface_list = pyliburo.py3dmodel.construct.make_occfaces_frm_pypolygons(pypolygon_list3d)
        for occface in occface_list:
            if height >0:
                occsolid = pyliburo.py3dmodel.construct.extrude(occface, (0,0,1), height)
                solid_list.append(occsolid)
    cnt+=1
            
facade_area = 0
for solid in solid_list:
    facade_list, roof_list, footprint_list = pyliburo.gml3dmodel.identify_building_surfaces(solid)
    for facade in facade_list:
        area = pyliburo.py3dmodel.calculate.face_area(facade)
        facade_area = facade_area + area
    
pyliburo.utility3d.write_2_collada(solid_list, collada_filepath)
cmpd = pyliburo.py3dmodel.construct.make_compound(solid_list)
#export to stl
pyliburo.py3dmodel.construct.write_2_stl(cmpd, stl_filepath )

print facade_area
display_2dlist = []
display_2dlist.append(solid_list)
pyliburo.py3dmodel.construct.visualise(display_2dlist, ["WHITE"])