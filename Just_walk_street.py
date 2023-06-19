from datetime import date

import grf

g = grf.NewGRF(
    grfid=b'JWTS',
    name='Just Walk The Street',
    description='Just Walk The Street',
)
RoadVehicle = g.bind(grf.RoadVehicle)

def tmpl_rv(x, y, func):
    return [
        func(      x, y, 10, 28, xofs= -4, yofs=-15),
        func( x + 20, y, 26, 28, xofs=-18, yofs=-14),
        func( x + 50, y, 36, 28, xofs=-18, yofs=-17),
        func( x + 90, y, 26, 28, xofs=-10, yofs=-15),
        func(x + 120, y, 10, 28, xofs= -4, yofs=-15),
        func(x + 140, y, 26, 28, xofs=-16, yofs=-16),
        func(x + 170, y, 36, 28, xofs=-18, yofs=-20),
        func(x + 210, y, 26, 28, xofs= -6, yofs=-15),
    ]

rv_png = grf.ImageFile("sprites/Just_walk_railroad.png", colourkey=(0, 0, 255))
rv_mask_png = grf.ImageFile("sprites/Just_walk_street.png")

RoadVehicle(
    id=5,
    name='Pedestrian',
    liveries=[{
        'name': 'Default',
        'sprites': tmpl_rv(0, 20, lambda *args, **kw: grf.FileSprite(rv_png, *args, **kw, bpp=24,
                                                                     mask=(rv_mask_png, 0, 0))),
    }],
    introduction_date=date(1700, 1, 1),
    max_speed=RoadVehicle.kmhishph(5),
    vehicle_life=80,
    model_life=80,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=0,
    running_cost_base=360,
    cargo_capacity=1,
    default_cargo_type=0,
    cost_factor=246,
    misc_flags=grf.RVFlags.USE_2CC,
    refittable_cargo_classes=0x1FFF | 0x8000,
)

g.write('Pedestrian_Truck.grf')
