# Input data

Download the SDSS-IV MaNGA DR17 DRP v3_1_1 cube for plate-IFU **8244-12704**, MaNGA ID **1-73638**:

[manga-8244-12704-LOGCUBE.fits.gz](https://data.sdss.org/sas/dr17/manga/spectro/redux/v3_1_1/8244/stack/manga-8244-12704-LOGCUBE.fits.gz)

Place the compressed file in this directory with that exact filename. It is approximately 196 MiB. Only this README belongs in the public data directory; FITS data are excluded by `.gitignore`.

The cube has 4,563 wavelength samples and a 74 × 74 spatial grid. The notebook uses FLUX, IVAR, MASK and WAVE, with the FITS WCS. Wavelengths are observed-frame vacuum Angstrom; FLUX is in 10^-17 erg s^-1 cm^-2 Angstrom^-1 per spaxel, and IVAR is inverse variance in the corresponding numerical units. See the [MaNGA DR17 data documentation](https://www.sdss4.org/dr17/manga/manga-data/) and [LOGCUBE data model](https://data.sdss.org/datamodel/files/MANGA_SPECTRO_REDUX/DRPVER/PLATE/stack/manga-PLATE-IFU-LOGCUBE.html).

SHA-256 of the input used for the validated run (a local verification value, not a published SDSS checksum):

```
4c908f40abe64a676185311cffef4279b5afff95a68f26b90a171c2662123017
```

The adopted redshift, inclination and cosmology are documented in the main README. All retained figures are produced from this cube; survey data and adapted tutorial code are acknowledged there.
