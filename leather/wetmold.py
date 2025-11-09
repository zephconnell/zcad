import cadquery as cq

# Fillets should not be less than 2 mm

# Constants
LEATHER_THICKNESS = 5
LEATHER_GAP = 0.1
CLAMP_HEIGHT = 25
CLAMP_THICKNESS = 25
CLAMP_FILLET = 2

# # Poker deck (mm)
# LENGTH = 85
# WIDTH = 61
# HEIGHT = 16
# VERTICAL_FILLETS = 3.5
# HORIZONTAL_FILLETS = 2

# Ring case (mm)
LENGTH = 30
WIDTH = 50
HEIGHT = 30
VERTICAL_FILLETS = 2
HORIZONTAL_FILLETS = 2

mold = (cq.Workplane("XY")
    .box(WIDTH, LENGTH, HEIGHT)
    .edges("|Z").fillet(VERTICAL_FILLETS)
    .edges("|X or |Y").fillet(HORIZONTAL_FILLETS)
    .translate((0, 0, HEIGHT / 2)))

stand_height = LEATHER_THICKNESS * 2
mold_stand = (mold
    .translate((0, 0, -stand_height))
    .cut(mold)
    .translate((0, 0, stand_height)))

mold = mold.translate((0, 0, stand_height))
mold_top = mold
mold_bottom = mold
mold = None
mold_top = mold_top.translate((0, 0, HEIGHT / 2))
mold_bottom = mold_bottom.cut(mold_top)
mold_top = (mold_top
    .translate((0, 0, -HEIGHT / 2))
    .cut(mold_bottom))

clamp_cutout_width = WIDTH + LEATHER_THICKNESS * (1+LEATHER_GAP) * 2
clamp_cutout_length = LENGTH + LEATHER_THICKNESS * (1+LEATHER_GAP) * 2
clamp_cutout_fillet = VERTICAL_FILLETS + LEATHER_THICKNESS * (1+LEATHER_GAP)
clamp_cutout = (cq.Workplane("XY")
    .box(clamp_cutout_width, clamp_cutout_length, CLAMP_HEIGHT)
    .edges("|Z").fillet(clamp_cutout_fillet)
    .translate((0, 0, CLAMP_HEIGHT / 2)))
clamp_width = clamp_cutout_width + CLAMP_THICKNESS * 2
clamp_length = clamp_cutout_length + CLAMP_THICKNESS * 2
clamp_top = (cq.Workplane("XY")
    .box(clamp_width, clamp_length, CLAMP_HEIGHT)
    .edges().fillet(CLAMP_FILLET)
    .translate((0, 0, CLAMP_HEIGHT / 2)))
clamp_bottom = (clamp_top
    .translate((0, 0, -CLAMP_HEIGHT + HORIZONTAL_FILLETS))
    .cut(mold_stand))
clamp_top = (clamp_top
    .cut(clamp_cutout)
    .translate((0, 0, HORIZONTAL_FILLETS))
    .edges().fillet(CLAMP_FILLET))

# mold = None
# mold_stand = None
clamp_cutout = None
# clamp_bottom = None
# clamp_top = None
