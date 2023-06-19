from datetime import date

import grf

g = grf.NewGRF(
    grfid=b'JWTM',
    name='Just Walk The Monorail',
    description='Just Walk The Monorail',
)
Train = g.bind(grf.Train)

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

rv_png = grf.ImageFile('sprites/Just_walk_railroad.png', colourkey=(0, 0, 255))
sprites = tmpl_rv(0, 20, lambda *args, **kw: grf.FileSprite(rv_png, *args, **kw, bpp=24))
#sprites = 'sprites/ALCOC420.png'
diesel_effects = {
    grf.SoundEvent.STOPPED: grf.RAWSound('sounds/modern_diesel_idle.wav'),
    grf.SoundEvent.VISUAL_EFFECT: grf.RAWSound('sounds/modern_diesel_run.wav'),
    grf.SoundEvent.RUNNING_16: grf.RAWSound('sounds/modern_diesel_coast.wav'),
    grf.SoundEvent.START: grf.RAWSound('sounds/horn_4.wav'),
    grf.SoundEvent.BREAKDOWN: grf.DefaultSound.BREAKDOWN_TRAIN_SHIP,
    grf.SoundEvent.TUNNEL: grf.RAWSound('sounds/horn_4.wav'),  # sounds are cached by filename so horn_4 will only be added once
}

Train(
    id=300,
    name='Pedestrian',
    liveries=[{
        'name': 'Default',
        'sprites': sprites,
    }],
    track_type = 1,
    sound_effects=diesel_effects,
    engine_class=Train.EngineClass.DIESEL,
    max_speed=Train.kmhishph(5),
    power=200,
    introduction_date=date(1700, 1, 1),
    weight=1,
    tractive_effort_coefficient=255,
    vehicle_life=80,
    model_life=80,
    climates_available=grf.ALL_CLIMATES,
    running_cost_factor=0,
    running_cost_base=360,
    cargo_capacity=1,
    default_cargo_type=0,
    cost_factor=1,
    refittable_cargo_types=0x1FFF | 0x8000,
)

g.write('Pedestrian_Monorail_Train.grf')
