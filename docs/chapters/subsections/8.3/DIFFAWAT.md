### DIFFAWAT -- Define PVT Region Water Component Diffusion Coefficients (Mass Fraction Formulation)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keyword defines the water diffusion coefficients assuming a mass fraction formulation for each compositional component in the model and for each PVT region, for when the Molecular Diffusion option has been activated by the [DIFFUSE](#__RefHeading___Toc349951_1539708736) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is optional as OPM Flow will automatically calculate the coefficients assuming the mole fraction formulation, as described by Sandve et al.[^1], if the [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) and [DIFFCWAT](#__RefHeading___Toc314077_1539708736 Copy 1 Copy 1) keywords are absent from the input deck. The keyword thus allows one to overwrite the automatically calculated values.

The keyword should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keywords and either the [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) or the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, have also been activated for the gas-water two component model.

See also the [DIFFCGAS](#__RefHeading___Toc314077_1539708736 Copy 1) and [DIFFCWAT](#__RefHeading___Toc314077_1539708736 Copy 1 Copy 1) keywords that assume the standard mole fraction formulation for diffusion rather than the mass fraction formulation assumed by the [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) and [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keywords. The [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) and [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keywords cannot be used in combination with the [DIFFCGAS](#__RefHeading___Toc314077_1539708736 Copy 1) and [DIFFCWAT](#__RefHeading___Toc314077_1539708736 Copy 1 Copy 1) keywords.

| 1 | CO2DIFF | A real positive number that declares the CO~2~ or H~2~ in water diffusion coefficient in the given PVT region. | None |
| --- | --- | --- | --- |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 2 | WATDIFF | A real positive number that specifies the water in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.32.1: DIFFAWAT Keyword Description

See also the [DIFFUSE](#__RefHeading___Toc349951_1539708736) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the Molecular Diffusion option and the [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that defines the gas diffusion coefficients for each compositional component in the model and for each PVT region. Finally, for gas-oil systems the [DIFFC](#__RefHeading___Toc314077_1539708736) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section should be used.

Normally diffusion coefficients are measured in laboratory units, that is cm^2^/s, for ease of use, outlines the conversion factors for converting the laboratory measured diffusion coefficients to those used by the simulator.

| Diffusivity Conversion Factors |  |  |
| --- | --- | --- |
| Laboratory Measured Units | Conversion Factor | Simulator Units |
| 1 cm^2^/s | 92.9979 ft^2^/day | Field |
| 8.64 m^2^/day | Metric |  |
| 3600 cm^2^/hour | Laboratory |  |

*Table 8.3.32.2: Diffusivity Conversion Factors*
#### Example

The example below is based on field units, with NTPVT equal to three on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- PVT REGION WATER COMPONENT DIFFUSION COEFFICIENTS (OPM FLOW KEYWORD)

\--

DIFFAWAT

\-- CO2 IN WAT IN

\-- WAT DF WAT DF

\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.160 0.150 / PVT REGION NO. 01

0.165 0.155 / PVT REGION NO. 02

/ PVT REGION NO. 03

Here the third PVT region has no values for the two component diffusion coefficients, and therefore the simulator will use correlations to define the diffusivity coefficients for this PVT region.

[^1]: Tor Harald Sandve, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.
