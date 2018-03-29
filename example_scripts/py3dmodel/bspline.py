from py4design import py3dmodel
#=====================================================================
#=====================================================================
circle = py3dmodel.construct.make_circle((0,0,0), (0,0,1), 1)
wire = py3dmodel.construct.make_wire_frm_edges([circle])
mwire = py3dmodel.modify.move((0,0,0), (0,20,10), wire)
mwire = py3dmodel.fetch.topo2topotype(py3dmodel.modify.scale(mwire, 0.5, (0,0,0)))
loft = py3dmodel.construct.make_loft_with_wires([wire,mwire])
mesh_face = py3dmodel.construct.simple_mesh(loft)
shell_mesh10 = py3dmodel.construct.sew_faces(mesh_face)[0]

loft_face_list = py3dmodel.fetch.topo_explorer(loft, "face")
spline_face1 = py3dmodel.construct.make_face_frm_wire(wire)
spline_face2 = py3dmodel.construct.make_face_frm_wire(mwire)
loft_face_list.append(spline_face1)
loft_face_list.append(spline_face2)
shell = py3dmodel.construct.sew_faces(loft_face_list)[0]
solid = py3dmodel.construct.make_solid(shell)
solid = py3dmodel.modify.fix_close_solid(solid)
solid_mesh_face = py3dmodel.construct.simple_mesh(solid)
shell_mesh = py3dmodel.construct.sew_faces(solid_mesh_face)[0]
solid_mesh = py3dmodel.construct.make_solid(shell_mesh)
edges = py3dmodel.fetch.topo_explorer(solid_mesh, "edge")
#=====================================================================
#=====================================================================
mwire2 = py3dmodel.modify.move((0,0,0), (0,3,30), wire)
mwire2 = py3dmodel.fetch.topo2topotype(py3dmodel.modify.scale(mwire2, 0.3, (0,0,0)))
loft2 = py3dmodel.construct.make_loft_with_wires([wire,mwire2])
loft2 = py3dmodel.fetch.topo2topotype(loft2)
mesh_face2 = py3dmodel.construct.simple_mesh(loft2)
shell_mesh20 = py3dmodel.construct.sew_faces(mesh_face2)[0]

loft_face_list2 = py3dmodel.fetch.topo_explorer(loft2, "face")
spline_face3 = py3dmodel.construct.make_face_frm_wire(mwire2)
loft_face_list2.append(spline_face1)
loft_face_list2.append(spline_face3)
shell2 = py3dmodel.construct.sew_faces(loft_face_list2)[0]
solid2 = py3dmodel.construct.make_solid(shell2)
solid2 = py3dmodel.modify.fix_close_solid(solid2)
solid_mesh_face2 = py3dmodel.construct.simple_mesh(solid2)
shell_mesh2 = py3dmodel.construct.sew_faces(solid_mesh_face2)[0]
solid_mesh2 = py3dmodel.construct.make_solid(shell_mesh2)
edges2 = py3dmodel.fetch.topo_explorer(solid_mesh2, "edge")
#=====================================================================
#=====================================================================
mwire3 = py3dmodel.modify.move((0,0,0), (10,-20,20), wire)
mwire3 = py3dmodel.fetch.topo2topotype(py3dmodel.modify.scale(mwire3, 0.3, (0,0,0)))
loft3 = py3dmodel.construct.make_loft_with_wires([wire,mwire3])
loft3 = py3dmodel.fetch.topo2topotype(loft3)
mesh_face3 = py3dmodel.construct.simple_mesh(loft3)
shell_mesh30 = py3dmodel.construct.sew_faces(mesh_face3)[0]

loft_face_list3 = py3dmodel.fetch.topo_explorer(loft3, "face")
spline_face4 = py3dmodel.construct.make_face_frm_wire(mwire3)
loft_face_list3.append(spline_face1)
loft_face_list3.append(spline_face4)
shell3 = py3dmodel.construct.sew_faces(loft_face_list3)[0]
solid3 = py3dmodel.construct.make_solid(shell3)
solid3 = py3dmodel.modify.fix_close_solid(solid3)
solid_mesh_face3 = py3dmodel.construct.simple_mesh(solid3)
shell_mesh3 = py3dmodel.construct.sew_faces(solid_mesh_face3)[0]
solid_mesh3 = py3dmodel.construct.make_solid(shell_mesh3)
edges3 = py3dmodel.fetch.topo_explorer(solid_mesh3, "edge")
#=====================================================================
#=====================================================================
diff = py3dmodel.construct.boolean_difference(shell_mesh10, solid_mesh2)
diff_faces = py3dmodel.fetch.topo_explorer(diff, "face")
diff_shells = py3dmodel.construct.sew_faces(diff_faces)
diff2_list = []
for ds in diff_shells:
    diff2 = py3dmodel.construct.boolean_difference(ds, solid_mesh3)
    diff2_list.append(diff2)
    
diff2_cmpd = py3dmodel.construct.make_compound(diff2_list) 
diff_faces2 = py3dmodel.fetch.topo_explorer(diff2_cmpd, "face")   
#print "IS diff NULL", py3dmodel.fetch.is_compound_null(diff)
#diff_faces2 = py3dmodel.fetch.topo_explorer(diff2, "face")
#print len(diff_faces2)

diff3 = py3dmodel.construct.boolean_difference(shell_mesh20, solid_mesh)
diff4 = py3dmodel.construct.boolean_difference(diff3, solid_mesh3)
diff_faces4 = py3dmodel.fetch.topo_explorer(diff4, "face")
print len(diff_faces4)

diff5 = py3dmodel.construct.boolean_difference(shell_mesh30, solid_mesh)
diff6 = py3dmodel.construct.boolean_difference(diff5, solid_mesh2)
diff_faces6 = py3dmodel.fetch.topo_explorer(diff6, "face")
print len(diff_faces6)

diff_faces_all = diff_faces2 + diff_faces4+diff_faces6
shell_list_all = py3dmodel.construct.sew_faces(diff_faces_all)
print len(shell_list_all)
#py3dmodel.calculate.sort_edges_into_order()
py3dmodel.utility.visualise([diff_faces2, diff_faces4, diff_faces6], ["RED", "GREEN", "BLUE"])