"""v1.9 layer geometries (preregistered). Radii in mm, thickness in X0 at eta = 0 before the scale factor f; half-width mm."""
import numpy as np
STRIPS = [255, 339, 418, 498, 608, 692, 780, 868, 965, 1080.]
OTHER_MAT = [(185, 0.05, 5), (255, 0.04, 4), (339, 0.04, 4), (418, 0.04, 4), (498, 0.04, 4), (550, 0.08, 10),
             (608, 0.03, 4), (692, 0.03, 4), (780, 0.03, 4)]
PIX = {'G0': ([29, 68, 109, 160.], 22.0),
       'G1': ([20, 68, 109, 160.], 16.0),
       'G2': ([29, 48, 68, 88, 109, 134, 160, 172.], 22.0),
       'G3': ([20, 44, 68, 88, 109, 134, 160, 172.], 16.0)}
PIX_X0_TOTAL = 0.08                       # four layers x 0.02 X0 in v1.0-v1.8; kept fixed and split equally


def layers(g):
    pix, bp = PIX[g]
    return np.array(pix + STRIPS, float)


def material(g):
    """bkg-style list (radius, X0, half-width) for geometry g (before the scale factor f)."""
    pix, bp = PIX[g]
    t = PIX_X0_TOTAL / len(pix)
    return sorted([(bp, 0.003, 0.5)] + [(r, t, 3) for r in pix] + OTHER_MAT)
