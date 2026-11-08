# ALP-ttbar Toy MC v1.9 — Preregistration: Layer Geometry at Fixed Material for the All-Pixel Three-Dimensional Vertex Fit of Displaced Light ALP → e⁺e⁻

**Author:** Won Shik Paik (Independent Researcher, Auckland, New Zealand)
**Date frozen:** 2026-11-08 (this file is committed to GitHub before any v1.9 simulation or fit is run)
**Builds on:** v1.8, https://doi.org/10.5281/zenodo.24034481 (preregistration https://doi.org/10.5281/zenodo.24028384); v1.7, https://doi.org/10.5281/zenodo.24011489; toy study motivated by arXiv:2610.38932
**Zenodo (this preregistration, PDF):** https://doi.org/10.5281/zenodo.24048262
**GitHub:** https://github.com/wspaik5/ALP_ttbar_Toy_MC_v1.9_Preregistration_Layer_Geometry
**Status:** plan only. No v1.9 outcome exists at the time of this commit.
**PDF version:** same text plus two figures drawn only from the geometry definitions, an analytic resolution formula and
published v1.6/v1.8 numbers (no new simulation or fit).

---

## 0. Why v1.9

v1.8 found that, in this toy, the 17 MeV loss is set mainly by multiple scattering relative to the small opening angle
(median 0.42 mrad), not by the bremsstrahlung-reduced momentum: a diagnostic covariance with the true momentum at every
surface removed most conversion fakes (7.4% → 1.9%) but improved 17 MeV only from 117× to 113×. Reducing the material
helped (z at every layer: 117× → 56× → 26.7× for material scale factors f = 1, 0.5, 0.25). The v1.8 future directions
named the layer geometry as the next test: a first layer closer to the beam, and more, thinner layers.

v1.9 asks whether **where** the material and the measurements are placed matters, at **fixed total material**.

An analytic estimate made before this preregistration (Fig. P1a; two 10 GeV tracks, z at every layer, Highland
scattering, Fisher matrix of the r–z fit, no simulation) gives the r–z opening resolution σ(Δcotθ) at f = 0.25:

| vertex radius | G0 (v1.8) | G1 closer | G2 finer | G3 both |
|---|---|---|---|---|
| 1 mm | 0.161 mrad | 0.165 | 0.134 | 0.138 |
| 40 mm | 0.163 | 0.163 | 0.155 | 0.156 |
| 100 mm | 0.193 | 0.193 | 0.177 | 0.177 |
| 250 mm | 0.203 | 0.203 | 0.203 | 0.203 |

For comparison: G0 at f = 1 gives 0.265–0.381 mrad, and the hit resolution alone 0.016–0.023 mrad. Scattering dominates
by an order of magnitude, so at fixed material the geometry changes the resolution by at most about 17% (G2), and the
closer first layer (G1) by almost nothing. On the other hand, more pixel layers mean more material bands, and the
material veto removes signal pairs whose vertex lies near any band. v1.9 tests whether these two effects leave the
conversion-induced loss essentially unchanged, as the estimate suggests.

## 0a. Related work (prior art)

- Low-material trackers with many thin layers and a first layer very close to the beam are pursued by next-generation
  concepts such as ALICE 3 [D1], ALICE ITS3 [D2] and the FCC-ee detector concepts [D3]. The geometries below only change
  the layer radii in this toy and make no statement about these detectors.
- The dependence of track and vertex resolution on layer radii, material and lever arm is textbook tracking [D4].

What v1.9 adds is limited to this series: it quantifies, in the preregistered toy of v1.0–v1.8, how the layer geometry
at fixed material affects the conversion-induced loss for top-associated displaced ALP → e⁺e⁻. No claim of novelty for
the method is made.

## 1. Questions

- **Q1 (primary).** At fixed total material (f = 0.25, 3.8 T) and with z at every layer, how does the limit degradation
  from conversions at 17, 50, 100 and 200 MeV (cτ = 1 mm) change when the first layer is moved closer to the beam, when
  the pixel layers are doubled at half the thickness each, and both, compared with the v1.8 geometry (26.7×, 8.8×, 3.3×,
  1.1×)?
- **Q2 (mechanism).** Do more, thinner layers improve the r–z separation (fraction of ALP pairs with Δχ²_L > 9) as
  estimated, and how much signal does the larger number of material bands cost in the material veto?

## 2. Unchanged from v1.8 (frozen)

- Field 3.8 T; material scale factor f = 0.25 applied to every material surface; v1.6 scalings of the conversion yield
  and the mass resolution for f = 0.25.
- Signal samples, kinematics, seeds and base selection (the base selection does not depend on the layers); subsample of
  the first 100,000 base conversion pairs and the first 60,000 base signal pairs per mass.
- Mini tracking simulation and fits (v1.3–v1.5), longitudinal simulation and r–z fit of v1.7 with both r–z hypotheses
  using s from the H_conv transverse fit, z at every layer with σ_z = 25 µm (V-allpixel), r–φ resolution 15 µm for
  layers below 200 mm and 35 µm above, nominal covariance (true initial momentum). Seeds 31/41 (transverse) and 1031/1041
  (longitudinal).
- Δχ²_3D = Δχ²_T + Δχ²_L; selection `scan_v15` (k ∈ {none, 1, 2, 4, 9, 16, 25, 49}), material veto, counting rule and
  metrics as in v1.8.

## 3. What is new (frozen)

**3.1 Geometries** (radii in mm; strips at 255–1080 mm and all other material unchanged; Fig. P1b):

| geometry | pixel layers (z and r–φ) | beam pipe | thickness per pixel layer |
|---|---|---|---|
| **G0** (= v1.8) | 29, 68, 109, 160 | 22 | 0.02 X₀ × f |
| **G1** closer | 20, 68, 109, 160 | 16 | 0.02 X₀ × f |
| **G2** finer | 29, 48, 68, 88, 109, 134, 160, 172 | 22 | 0.01 X₀ × f |
| **G3** both | 20, 44, 68, 88, 109, 134, 160, 172 | 16 | 0.01 X₀ × f |

The total pixel material (0.08 X₀ × f), the beam-pipe thickness (0.003 X₀ × f) and all other material are identical in
all geometries. Each pixel layer is a sensor and a material band of half-width 3 mm (beam pipe 0.5 mm), as before.

**3.2 Samples.** The conversion sample is regenerated for each geometry with the same generator and seed (5), because
the conversion radii follow the material; the signal truth samples are unchanged. The geometry is selected by an
environment variable before import, as the field and material were in v1.6.

**3.3 Reporting.** For each geometry: Δχ²_T only and Δχ²_3D (V-allpixel), with and without mass window; fraction of
pairs with Δχ²_L > 9 for conversions (r < 800 mm) and each ALP mass; fraction of base signal pairs removed by the
material veto (n_σ = 2, without exemption).

## 4. Sanity gate (frozen)

Before any degradation is computed:
1. **G0 identity.** Transverse vertex radius, Δχ²_T and Δχ²_L (V-allpixel) equal v1.8 config M025 within 10⁻⁶ for
   ≥ 99.9% of pairs in every sample.
2. **Material bookkeeping.** The total material (Σ X₀ at η = 0) is identical in G0–G3 to 10⁻¹².
3. **Fit success** ≥ 95%; fraction with Δχ²_L < −10⁻⁶ ≤ 0.1% in every sample.

If the gate fails, the code is fixed, the failure and the fix are reported, and the gate is re-run.

## 5. Validation (independent samples only; criteria frozen)

- **U1 (null, G2).** The v1.3 V4 collinear sample (seed 404, longitudinal seed 1404), no bremsstrahlung, G2,
  V-allpixel: Δχ²_L median 0.30–0.65 and 3–8% above 3.84 (χ²₁).
- **U2 (propagation, G3).** Without scattering, z hits agree with z_v + cotθ · s to better than 0.1 µm.
- **U3 (response).** Two 10 GeV tracks from a vertex at r uniform in 30–100 mm, |η| < 1, polar opening 1 mrad, no
  bremsstrahlung (seed 808, longitudinal seed 1808): the median Δχ²_L is larger in G2 than in G0.

If a criterion fails, the code is fixed and the fix is reported.

## 6. Predictions (written before running)

Values are degradations with the Δχ²_3D (V-allpixel) selection, f = 0.25, cτ = 1 mm, compared with G0 (v1.8:
26.7×, 8.8×, 3.3×, 1.1×).

- **P1 (17 MeV, primary).** G2 is within ±25% of G0: **between 20× and 33.4×**. The geometry at fixed material does not
  give a gain comparable to the material reduction (v1.8: a factor 2.1 from f = 0.5 to 0.25).
- **P2 (50 MeV, primary).** G2 is **between 6.6× and 11×** (±25% of 8.8×).
- **P3 (closer first layer).** G1 is within ±10% of G0 at every mass.
- **P4 (combination).** G3 is within ±10% of G2 at every mass.
- **P5 (r–z mechanism).** The fraction of 17 MeV ALP pairs with Δχ²_L > 9 is higher in G2 than in G0 (61.4%), by
  **at most 10 percentage points**; the conversion fraction with Δχ²_L > 9 changes by at most a factor 1.5 from G0
  (2.03%).
- **P6 (200 MeV).** All geometries give **≤ 1.5×**.
- **P7 (veto cost).** The fraction of base 17 MeV signal pairs removed by the material veto is **higher in G2 than in
  G0**.

Each prediction is reported as confirmed or refuted against these statements. Refuted predictions are not re-framed.

## 7. Reporting

v1.9 note with a Figure 13: (a) degradation versus mass for G0–G3 with the preregistered ranges; (b) the fraction of
pairs with Δχ²_L > 9 for conversions and ALP pairs and the veto loss per geometry; (c) the analytic estimate of Fig. P1a
next to the simulated r–z separation. The note contains the U1–U3 validation, the prediction table, "Deviations from
preregistration", "Limitations" and "Future directions".

## 8. Limitations known in advance

- All v1.0–v1.8 limitations apply (barrel only, idealised cylindrical layers, no pattern recognition, toy material map,
  crude counting rule, selection optimised on the same samples, truth used for the material list and the scattering
  momentum, single-Gaussian bremsstrahlung model in the transverse fit, sequential 3D fit).
- Only the pixel region changes; real trackers also change supports, services and the strip region. Thinner layers are
  assumed to keep the same hit resolution.
- The analytic estimate of Sec. 0 ignores bremsstrahlung, track curvature and the vertex spread; it guides the
  predictions but is not a result.
- Subsampled statistics; only trends and ratios are meaningful. No statement about real detectors is made.

[D1] ALICE Collaboration, Letter of intent for ALICE 3, arXiv:2211.02491.
[D2] ALICE Collaboration, Technical Design Report for the ALICE Inner Tracking System 3 – ITS3, CERN-LHCC-2024-003.
[D3] N. Bacchetta et al., CLD – A Detector Concept for the FCC-ee, arXiv:1911.12230; The IDEA detector concept for
FCC-ee, arXiv:2502.21223.
[D4] R. Frühwirth, M. Regler, R. K. Bock, H. Grote, D. Notz, Data Analysis Techniques for High-Energy Physics, 2nd ed.,
Cambridge University Press (2000).
