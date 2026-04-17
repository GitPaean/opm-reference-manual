### DIFFAWAT -- Define PVT Region Water Component Diffusion Coefficients (Mass Fraction Formulation)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DIFFAWAT keyword defines the water diffusion coefficients assuming a mass fraction formulation for each compositional component in the model and for each PVT region, for when the Molecular Diffusion option has been activated by the DIFFUSE keyword in the RUNSPEC section.

This keyword is optional as OPM Flow will automatically calculate the coefficients assuming the mole fraction formulation, as described by Sandve et al.[^1], if the DIFFAWAT and DIFFCWAT keywords are absent from the input deck. The keyword thus allows one to overwrite the automatically calculated values.

The keyword should only be used if the CO2STORE or H2STORE keywords and either the GASWAT or the GAS and WATER keywords in the RUNSPEC section, have also been activated for the gas-water two component model.

See also the DIFFCGAS and DIFFCWAT keywords that assume the standard mole fraction formulation for diffusion rather than the mass fraction formulation assumed by the DIFFAGAS and DIFFAWAT keywords. The DIFFAGAS and DIFFAWAT keywords cannot be used in combination with the DIFFCGAS and DIFFCWAT keywords.

| 1 | CO2DIFF | A real positive number that declares the CO~2~ or H~2~ in water diffusion coefficient in the given PVT region. | None |
| --- | --- | --- | --- |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 2 | WATDIFF | A real positive number that specifies the water in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.32.1: DIFFAWAT Keyword Description

See also the DIFFUSE keyword in the RUNSPEC section to activate the Molecular Diffusion option and the DIFFAGAS keyword in the PROPS section that defines the gas diffusion coefficients for each compositional component in the model and for each PVT region. Finally, for gas-oil systems the DIFFC keyword in the PROPS section should be used.

Normally diffusion coefficients are measured in laboratory units, that is cm^2^/s, for ease of use, outlines the conversion factors for converting the laboratory measured diffusion coefficients to those used by the simulator.

| Diffusivity Conversion Factors |  |  |
| --- | --- | --- |
| Laboratory Measured Units | Conversion Factor | Simulator Units |
| 1 cm^2^/s | 92.9979 ft^2^/day | Field |
| 8.64 m^2^/day | Metric |  |
| 3600 cm^2^/hour | Laboratory |  |

*Table 8.3.32.2: Diffusivity Conversion Factors*
#### Example

The example below is based on field units, with NTPVT equal to three on the TABDIMS keyword.

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
