# ----pygame---- #
RESOLUTION = (1280, 1024)
MAX_FPS = 60

# ----GAME---- #
GRAVITY = {'SUN': -274.13,
           'MERCURY': -3.59,
           'VENUS': -8.87,
           'EARTH': -9.81,
           'MOON': -1.62,
           'MARS': -3.77,
           'JUPITER': -25.95,
           'SATURN': -11.08,
           'URANUS': -10.67,
           'NEPTUNE': -14.07,
           'PLUTO': -0.42}

FUEL_MASS = 5
TANK_FUEL = {'small_tank': 200,
             'medium_tank': 400,
             'large_tank': 800}
TANK_MASS = {'small_tank': 125,
             'medium_tank': 250,
             'large_tank': 500}
TANK_TEXTURE = {'small_tank': 'assets/small_tank.png',
                'medium_tank': 'assets/medium_tank.png',
                'large_tank': 'assets/large_tank.png'}

ENGINE_MASS = {'basic_engine': 1250}
ENGINE_THRUST_ATM = {'basic_engine': 200000}
ENGINE_THRUST_VAC = {'basic_engine': 215000}
ENGINE_CONSUMPTION = {'basic_engine': 14}
ENGINE_TEXTURE = {'basic_engine': 'assets/basic_engine.png'}
