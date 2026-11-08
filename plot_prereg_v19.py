"""v1.9 preregistration figures. NO simulation or fit: the geometry definitions, the analytic Highland formula and
published v1.6/v1.8 numbers only."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from geom_v19 import layers, material

G = ['G0', 'G1', 'G2', 'G3']; COL = dict(G0='k', G1='C1', G2='C0', G3='C2')


def highland(p, t):
    return 0.0136 / p * np.sqrt(t) * (1 + 0.038 * np.log(t))


def sigma_dcot(g, r0, p=10.0, f=0.25, sz=0.025, ms=True):
    """Analytic r-z resolution of the polar opening for two tracks from a common vertex at radius r0 (eta = 0,
    straight in s = R - r0), z at every layer, scattering at every material surface after the vertex (outer TOB
    material at 868/965/1080 mm as in minitrack). Fisher matrix of (z_v, c1, c2); returns sigma(c1 - c2) [mrad]."""
    S = layers(g); M = material(g) + [(868, 0.03, 4), (965, 0.03, 4), (1080, 0.03, 4)]
    MR = np.array([m[0] for m in M]); MT = np.array([m[1] for m in M]) * f
    s = S[S > r0] - r0; sm = MR[MR > r0 + 1e-9] - r0; th = highland(p, MT[MR > r0 + 1e-9]) if ms else 0 * sm
    arm = np.clip(s[:, None] - sm[None, :], 0, None)
    W = np.linalg.inv((arm * th**2) @ arm.T + np.eye(len(s)) * sz**2)
    A = np.stack([np.ones_like(s), s], 1); F1 = A.T @ W @ A
    F = np.array([[2 * F1[0, 0], F1[0, 1], F1[0, 1]], [F1[0, 1], F1[1, 1], 0], [F1[0, 1], 0, F1[1, 1]]])
    C = np.linalg.inv(F)
    return 1e3 * np.sqrt(C[1, 1] + C[2, 2] - 2 * C[1, 2])


if __name__ == '__main__':
    r0s = np.linspace(1, 400, 400)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.2))
    for g in G:
        ax[0].plot(r0s, [sigma_dcot(g, r) for r in r0s], c=COL[g], label=f'{g}, f = 0.25')
    ax[0].plot(r0s, [sigma_dcot('G0', r, f=1.0) for r in r0s], 'k--', lw=1, label='G0, f = 1')
    ax[0].plot(r0s, [sigma_dcot('G0', r, ms=False) for r in r0s], 'k:', lw=1, label='G0, hit resolution only')
    ax[0].axhline(0.42, c='C3', lw=1); ax[0].text(250, 0.44, 'median 17 MeV opening (0.42 mrad)', color='C3', fontsize=7)
    ax[0].set_yscale('log'); ax[0].set_ylim(0.01, 1); ax[0].set_xlabel('vertex radius [mm]')
    ax[0].set_ylabel(r'$\sigma(\Delta\cot\theta)$ [mrad], 10 GeV per track')
    ax[0].legend(fontsize=7, loc='lower right'); ax[0].set_title('(a) analytic r–z opening resolution (z at every layer)', fontsize=9.5)
    for i, g in enumerate(G):
        for r, t, hw in material(g):
            ax[1].add_patch(plt.Rectangle((r - hw, i - 0.3), 2 * hw, 0.6, color='0.75', lw=0))
        for r in layers(g):
            ax[1].plot([r, r], [i - 0.35, i + 0.35], c=COL[g], lw=1.6)
    ax[1].set_yticks(range(4)); ax[1].set_yticklabels(['G0 (v1.8)', 'G1 closer', 'G2 finer', 'G3 both'])
    ax[1].set_xlim(0, 300); ax[1].set_xlabel('radius [mm] (strips beyond 255 mm unchanged)')
    ax[1].set_title('(b) sensor layers (lines) and material bands (grey)', fontsize=9.5)
    fig.suptitle('Fig. P1 (geometry definitions and analytic formula only; no v1.9 simulation or fit)', fontsize=9.5)
    plt.tight_layout(); plt.savefig('figP1_geometries_and_rz_resolution.png', dpi=160)
    for g in G:
        print(g, 'layers', layers(g)[:8].astype(int), 'total pixel X0', round(sum(t for r, t, h in material(g) if 15 < r < 175 and h == 3), 4),
              'sigma(dcot) f=0.25 at r0 = 1/40/100/250:', [round(sigma_dcot(g, r), 3) for r in (1, 40, 100, 250)])
    # Figure P2: published inputs and preregistered ranges
    mm = np.array([17, 50, 100, 200])
    T = [34.7, 19.5, 8.8, 2.1]; A0 = [26.7, 8.8, 3.3, 1.1]; A05 = [56.1, 17.9, 5.7, 2.2]
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.plot(mm, T, 'o--', c='gray', label='transverse only, f = 0.25 (v1.6)')
    ax.plot(mm, A05, 'P:', c='C1', label='3D V-allpixel, f = 0.5 (v1.8)')
    ax.plot(mm, A0, 'P-', c='k', label='3D V-allpixel, f = 0.25 = G0 (v1.8)')
    for x, lo, hi, t in ((17, 20.0, 33.4, 'P1'), (50, 6.6, 11.0, 'P2'), (200, 0, 1.5, 'P6')):
        ax.fill_between([x * 0.9, x * 1.1], max(lo, 0.85), hi, color='C0', alpha=0.18, lw=0); ax.text(x * 1.12, max(lo, 1) * 1.1, t, fontsize=7, color='C0')
    ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xticks(mm); ax.set_xticklabels(['17', '50', '100', '200']); ax.minorticks_off()
    ax.set_ylim(0.8, 80); ax.set_xlim(13, 280); ax.grid(alpha=0.25); ax.set_xlabel(r'$m_a$ [MeV]')
    ax.set_ylabel(r'limit degradation (c$\tau$ = 1 mm)'); ax.legend(fontsize=7, loc='lower left')
    ax.set_title('Fig. P2 (published numbers; shaded: preregistered ranges for G2)', fontsize=9)
    plt.tight_layout(); plt.savefig('figP2_published_inputs_and_ranges.png', dpi=160)
