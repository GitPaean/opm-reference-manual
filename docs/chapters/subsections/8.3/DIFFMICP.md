### DIFFMICP -- Define PVT Region MICP Diffusion Coefficients (Mass Concentration Formulation)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DIFFMICP keyword defines the diffusion coefficients assuming the mass concentration formulation for each component dissolved in water and for each PVT region, for when the molecular diffusion option has been activated by the DIFFUSE keyword in the RUNSPEC section. The keyword should only be used if either the MICP or BIOFILM model has been activated in the RUNSPEC section.

| 1 | MICRDIFF | A real positive number that declares the microbial concentration in water diffusion coefficient in the given PVT region. | None |
| --- | --- | --- | --- |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 2 | OXYGDIFF | A real positive number that declares the oxygen concentration in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 3 | UREADIFF | A real positive number that declares the urea concentration in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Item 1 is only relevant for the BIOFILM model.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.28: DIFFMICP Keyword Description

#### Example

The example below is based on metric units, with NTPVT equal to one on the TABDIMS keyword.

\--

\-- PVT REGION MICP COMPONENT DIFFUSION COEFFICIENTS (OPM FLOW KEYWORD)

\--

DIFFMICP

\-- MICR IN OXYG IN UREA IN

\-- WAT DF WAT DF WAT DF

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

2E-04 2E-04 1E-04 / PVT REGION NO. 01
