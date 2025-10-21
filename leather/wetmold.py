import cadquery as cq

HEIGHT = 85
WIDTH = 61
DEPTH = 16
CARD_FILLET = 3.5
EDGE_FILLET = 1
LEATHER_THICKNESS = 2.5
CLAMP_DEPTH = 25
CLAMP_THICKNESS = 25
LEATHER_GAP = 0.1

mold = (cq.Workplane("XY")
    .box(WIDTH, HEIGHT, DEPTH)
    .edges("|Z").fillet(CARD_FILLET)
    .edges("|X or |Y").fillet(EDGE_FILLET)
    .translate((0, 0, EDGE_FILLET / 2)))

stand_depth = LEATHER_THICKNESS * 2
mold_stand = (mold
    .translate((0, 0, -stand_depth))
    .cut(mold))

clamp_cutout_width = WIDTH + LEATHER_THICKNESS * (1+LEATHER_GAP) * 2
clamp_cutout_height = HEIGHT + LEATHER_THICKNESS * (1+LEATHER_GAP) * 2
clamp_fillet = CARD_FILLET + LEATHER_THICKNESS * (1+LEATHER_GAP)
clamp_cutout = (cq.Workplane("XY")
    .box(clamp_cutout_width, clamp_cutout_height, CLAMP_DEPTH)
    .edges("|Z").fillet(clamp_fillet))
clamp_width = clamp_cutout_width + CLAMP_THICKNESS * 2
clamp_height = clamp_cutout_height + CLAMP_THICKNESS * 2
clamp_top = (cq.Workplane("XY")
    .box(clamp_width, clamp_height, CLAMP_DEPTH)
    .edges("|Z").fillet(clamp_fillet)
    .edges("|X or |Y").fillet(EDGE_FILLET))
clamp_bottom = (clamp_top
    .translate((0, 0, -CLAMP_DEPTH + EDGE_FILLET))
    .cut(mold_stand))
clamp_top = (clamp_top
    .cut(clamp_cutout)
    .translate((0, 0, EDGE_FILLET))
    .edges("|X or |Y").fillet(EDGE_FILLET))

# mold = None
# mold_stand = None
clamp_cutout = None
# clamp_bottom = None
# clamp_top = None
