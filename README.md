# Gas kinematics of MaNGA 8244-12704

A reproducible single-galaxy analysis of spatially resolved emission-line spectra, developed from an undergraduate galaxy-kinematics project completed at UCL. The executed notebook follows the gas rotation from spectra to a rotation curve, then compares it with an illustrative exponential-disc model.

## Scientific question

How does the ionised gas in MaNGA 8244-12704 trace ordered rotation, and how does its rotation curve compare with a disc inferred from the galaxy's continuum light profile under explicit simplifying assumptions?

## Methods

- Inspect spectra and narrow-band spatial structure in the SDSS DR17 MaNGA cube.
- Fit H-alpha and the [N II] doublet jointly with a shared redshift and Gaussian width, separate amplitudes and a constant continuum.
- Construct rest-frame velocity and fitted line-flux maps using valid, unmasked samples and the adopted S/N selections.
- Sample an adopted major axis, fit an empirical rotation profile, locate its half-transition centre, and fold data and model consistently before correcting velocity for inclination.
- Integrate a rest-frame 7000–8000 Angstrom continuum band using wavelength-bin widths, fit an exponential profile, and convert projected luminosity density to disc-plane density.
- Compare the rotation with an illustrative thin exponential disc and inspect selected [O III] and [S II] diagnostics.

Seven retained figures in [analysis.ipynb](analysis.ipynb) show the joint spectral fit, H-alpha flux, velocity field and adopted axis, folded rotation, exponential brightness profile, disc comparison and [S II] map.

## Technical contribution

The author developed the single-galaxy fitting and modelling workflow: constrained joint Gaussian fitting, uncertainty calculations, S/N masks, major-axis sampling, empirical rotation fitting, continuum integration, exponential-profile fitting and selected additional-line fitting. Input validation and consistent geometry make the analysis reproducible. Cube loading, array transposition, WCS handling, masking and narrow-band inspection adapt SDSS tutorial code; those components are attributed below. The physical model families are established methods, not claimed as new inventions.

## Selected validated results

The notebook completed all 93 code cells in a fresh Python 3.13.15 kernel. Subsequent presentation edits preserve its executable calculations and retained numerical outputs.

| Quantity | Validated value |
|---|---:|
| Fitted kinematic centre, zero-based image pixels | (37.640778, 36.472877) |
| Fitted residual velocity centre | +9.429825 km/s |
| Asymptotic inclination-corrected empirical speed | 298.57 km/s |
| Exponential effective radius, Re | 16.43277 kpc |
| Exponential scale length, Rd = Re/1.678 | 9.79307 kpc |
| Central disc-plane band luminosity density | 6.68144 × 10^40 erg s^-1 kpc^-2 |
| Illustrative disc-model peak speed | approximately 133.71 km/s at 21.06 kpc |

The empirical profile is f(s) = (a-d)/(1+(s/q)^b)+d, with [a,b,q,d] = [280.17892461, 8.37488319, 24.73629452, -261.31927549]; a and d are in km/s, q in spaxels and b is dimensionless. The central joint fit gives z = 0.115145 and a Gaussian width of 3.77 Angstrom.

The peak-S/N velocity selection retains 1,176 spaxels. The integrated-flux diagnostic retains 648, all in its largest connected component. Additional-line detections number 86 for [O III] 4960.3, 1,448 for [O III] 5008.2 and 958 for [S II] 6718.3. An invalid parent fit is excluded from the latter map; its maximum numerical flux is approximately 1.553 rather than an isolated extreme outlier.

The gas rotation lies above the chosen illustrative disc curve. **This is a model comparison, not a calibrated stellar-mass measurement or a definitive dark-matter determination.**

## Limitations and assumptions

- Adopted inputs are systemic redshift 0.115137 ± 0.000019, inclination 65.07 ± 0.04 degrees, 0.5 arcsec pixels and WMAP9 cosmology. They are analysis inputs, not independently measured here.
- Thirty rounded pixels sample the axis from (30,14) to (47,64). With e = (17,50)/sqrt(2789), s = 1 + (p-p1) dot e. Its positive origin is a model convention; the unweighted empirical fit constrains only q to be positive. The centre is p1 + (q-1)e and the velocity centre is (a+d)/2. The profile need not be reflection-symmetric about that centre.
- Velocity is c(z-z_sys)/(1+z_sys), with c = 300,000 km/s. Independent marginal redshift errors are propagated, but systemic uncertainty is shared across spaxels. Folded errors omit fitted-centre covariance. Gaussian flux errors omit amplitude–width covariance.
- All 30 continuum samples have complete valid-band coverage. Independent wavelength-bin errors are combined in quadrature. Formal exponential-fit errors are much smaller than the spatial scatter and do not quantify all uncertainty.
- The thin, transparent disc uses disc-plane luminosity density equal to projected luminosity density times cos(i). Its assumed scaling LM = 0.1 uses a bolometric solar-luminosity constant with restricted-band light; it is not a calibrated stellar-population mass-to-light ratio. Full disc covariance propagation is absent.
- Beam smearing, dust, gas mass, bulge structure, finite thickness and stellar-population variation are not modelled. Additional-line fits inherit a fixed width in Angstrom and use amplitude/pixel-noise detection, so they remain exploratory.

The validated run has no S/N divide-by-zero warnings. Two Astropy WCS warnings concern input FITS headers: PLATEID's type and MJD-OBS being filled from DATE-OBS. They do not prevent execution. Separate Windows kernel/transport notices are environment-specific.

## Data provenance

The input is the SDSS-IV MaNGA DR17 DRP v3_1_1 LOGCUBE for plate-IFU **8244-12704** (MaNGA ID **1-73638**). The compressed file is approximately 196 MiB and is deliberately excluded from this repository.

Download [manga-8244-12704-LOGCUBE.fits.gz from the SDSS Science Archive Server](https://data.sdss.org/sas/dr17/manga/spectro/redux/v3_1_1/8244/stack/manga-8244-12704-LOGCUBE.fits.gz) and place it in `data/`. See [data/README.md](data/README.md) for units, input verification and further documentation. No original report, external figure, local environment or execution diagnostics form part of the public file set.

## Acknowledgements and attribution

Data are from SDSS-IV MaNGA. Please follow the [SDSS-IV citation and acknowledgement guidance](https://www.sdss4.org/collaboration/citing-sdss/) when reusing this work. Relevant survey references include [Bundy et al. (2015)](https://arxiv.org/abs/1412.1482), [Law et al. (2016)](https://arxiv.org/abs/1607.08619) and the [DR17 release paper, Abdurro'uf et al. (2022)](https://arxiv.org/abs/2112.02026).

Code adapted from the [SDSS MaNGA Python tutorial](https://www.sdss4.org/dr17/manga/manga-tutorials/how-do-i-look-at-my-data/python) handles cube loading, transposition, WCS conversion, masking and narrow-band inspection. The Sersic function adapts the author's earlier Python work. Exponential-disc equations follow Cimatti, Fraternali & Nipoti (2019), *Introduction to Galaxy Formation and Evolution*. The project originated as an undergraduate investigation at UCL.

All retained figures are generated by this analysis from the survey cube. No externally reproduced figure is included. No repository-wide licence is assigned in this review draft; tutorial-derived code retains explicit attribution.

## Environment and setup

The validated environment uses Python 3.13.15, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.2 and Astropy 8.0.1. `requirements.txt` lists the required analysis and notebook-execution packages; `requirements-lock.txt` pins the validated environment including transitive dependencies. `environment.yml` provides an unpinned conda alternative. The locked environment was validated on Windows; other platforms have not been tested.

From this project's directory, create a local environment and install the locked dependencies:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe run_notebook.py
```

On macOS/Linux with Python 3.13 available:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python run_notebook.py
```

Download the cube before running the last command. The launcher uses the selected environment's interpreter, creates a temporary kernel specification without global registration, and executes from the project directory. It stops at the first error and saves the notebook only after successful completion. Re-execution regenerates the full set of intermediate outputs; this review copy retains only selected outputs for readability.

The ignore rules admit only the documented public files and exclude data binaries, local environments, diagnostics, checkpoints, temporary files and editor artefacts. Do not force-add ignored files.
