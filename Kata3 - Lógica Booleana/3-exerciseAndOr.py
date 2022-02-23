asteroidSpeed = 19 # km/h
asteroidSize = 19 # mts

if asteroidSize >= 25 and asteroidSize <= 1000:
    print('Oh no, this is the end!')
else:
    if asteroidSpeed >= 20 and asteroidSpeed < 25:
        print('I can see the bright of that asteroid')
    elif asteroidSpeed > 25:
        print('Warning! warning! Asteroid y comming really fast')
    print('No asteroids arround!')

