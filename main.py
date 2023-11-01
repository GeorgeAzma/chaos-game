import pygame as pg
import numpy as np
import random

pg.init()

size = (800, 800)
screen = pg.display.set_mode(size)

running = True
clock = pg.time.Clock()
range_x = (-1, 1)
range_y = (-1, 1)
range_width = range_x[1] - range_x[0]
range_height = range_y[1] - range_y[0]
p = np.array(
    [
        random.random() * range_width + range_x[0],
        random.random() * range_height + range_y[0],
    ]
)
# Sierpinkski triangle
fs = [
    lambda p: ((p[0] - 1) * 0.5, (p[1] - 1) * 0.5),
    lambda p: ((p[0] + 1) * 0.5, (p[1] - 1) * 0.5),
    lambda p: ((p[0] + 0) * 0.5, (p[1] + 1) * 0.5),
]
# Rectangle
fs = [
    lambda p: ((p[0] - 1) * 0.5, (p[1] - 1) * 0.5),
    lambda p: ((p[0] + 1) * 0.5, (p[1] - 1) * 0.5),
    lambda p: ((p[0] + 1) * 0.5, (p[1] + 1) * 0.5),
    lambda p: ((p[0] - 1) * 0.5, (p[1] + 1) * 0.5),
]
# Pentagon
fs = [
    lambda p: ((p[0] + 0.000) * 0.5, (p[1] + 1.000) * 0.5),
    lambda p: ((p[0] + 0.951) * 0.5, (p[1] + 0.309) * 0.5),
    lambda p: ((p[0] + 0.588) * 0.5, (p[1] - 0.809) * 0.5),
    lambda p: ((p[0] - 0.588) * 0.5, (p[1] - 0.809) * 0.5),
    lambda p: ((p[0] - 0.951) * 0.5, (p[1] + 0.309) * 0.5),
]
# Hexagon
fs = [
    lambda p: ((p[0] + 0.000) * 0.5, (p[1] + 1.000) * 0.5),
    lambda p: ((p[0] + 0.866) * 0.5, (p[1] + 0.500) * 0.5),
    lambda p: ((p[0] + 0.866) * 0.5, (p[1] - 0.500) * 0.5),
    lambda p: ((p[0] - 0.000) * 0.5, (p[1] - 1.000) * 0.5),
    lambda p: ((p[0] - 0.866) * 0.5, (p[1] - 0.500) * 0.5),
    lambda p: ((p[0] - 0.866) * 0.5, (p[1] + 0.500) * 0.5),
]
# Sierpinski carpet
# fs = [
#     lambda p: ((p[0] - 1) * 0.33333333333, (p[1] - 1) * 0.33333333333),
#     lambda p: ((p[0] + 1) * 0.33333333333, (p[1] - 1) * 0.33333333333),
#     lambda p: ((p[0] + 1) * 0.33333333333, (p[1] + 1) * 0.33333333333),
#     lambda p: ((p[0] - 1) * 0.33333333333, (p[1] + 1) * 0.33333333333),
#     lambda p: ((p[0] - 1) * 0.33333333333, (p[1] - 0) * 0.33333333333),
#     lambda p: ((p[0] + 1) * 0.33333333333, (p[1] - 0) * 0.33333333333),
#     lambda p: ((p[0] + 0) * 0.33333333333, (p[1] + 1) * 0.33333333333),
#     lambda p: ((p[0] - 0) * 0.33333333333, (p[1] - 1) * 0.33333333333),
# ]
# Barnsley fern
# range_x = (-2, 2)
# range_y = (-8, 0)
# range_width = range_x[1] - range_x[0]
# range_height = range_y[1] - range_y[0]
# fs = [
#     lambda p: np.array([[0, 0], [0, 0.16]]) @ p + np.array([0, 0]),
#     lambda p: np.array([[0.85, 0.04], [-0.04, 0.85]]) @ p + np.array([0, 1.6]),
#     lambda p: np.array([[0.2, -0.26], [0.23, 0.22]]) @ p + np.array([0, 1.6]),
#     lambda p: np.array([[-0.15, 0.28], [0.26, 0.24]]) @ p + np.array([0, 0.44]),
# ]

while running:
    # screen.fill((0, 0, 0))
    prev_idx = -1
    prev2_idx = -1
    it = 0
    p = np.array(
        [
            random.random() * range_width + range_x[0],
            random.random() * range_height + range_y[0],
        ]
    )
    for i in range(1000):
        idx = random.randrange(len(fs))

        # Current point can't be anti-clockwise neighbor of previous vertex
        # if idx == prev_idx + 1 or (idx == 0 and prev_idx == len(fs) - 1):
        #     idx = (idx + 1) % len(fs)

        # Current vertex can't be previous vertex
        # if idx == prev_idx:
        #     idx = (idx + 1) % len(fs)

        # Current vertex can't be opposite to previous vertex
        # if idx == len(fs) - 1 - prev_idx:
        #     idx = (idx + 1) % len(fs)

        # Current vertex can't be neighboring previous vertex
        if (
            abs(prev_idx - idx) == 1
            or (prev_idx == 0 and idx == len(fs) - 1)
            or (idx == 0 and prev_idx == len(fs) - 1)
        ):
            idx = (idx + 1) % len(fs)

        # Current vertex can't be neighboring previous vertex if previous vertex is equal to previous to previous vertex
        # if prev2_idx == prev_idx and (
        #     abs(prev_idx - idx) == 1
        #     or (prev_idx == 0 and idx == len(fs) - 1)
        #     or (idx == 0 and prev_idx == len(fs) - 1)
        # ):
        #     idx = (idx + 1) % len(fs)

        prev2_idx = prev_idx
        prev_idx = idx
        f = fs[idx]
        p = f(p)
        if it > 20:
            sx = int((p[0] - range_x[0]) / range_width * size[0])
            sy = int((-p[1] - range_y[0]) / range_height * size[1])
            sx = min(size[0] - 1, max(0, sx))
            sy = min(size[1] - 1, max(0, sy))
            px = screen.get_at((sx, sy))
            if px[0] + px[1] + px[2] < 510:
                screen.set_at(
                    (sx, sy),
                    (
                        max(0, min(255, px[0] + 4 + sx / size[0] * 16)),
                        max(0, min(255, px[1] + 4 + sy / size[1] * 16)),
                        max(0, min(255, px[2] + 4)),
                    ),
                )
        it += 1

    # Process Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()

    clock.tick()
    fps = int(clock.get_fps())
    pg.display.set_caption(f"FPS: {fps}")

pg.quit()
