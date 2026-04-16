### DIFFMICP -- Define PVT Region MICP Diffusion Coefficients (Mass Concentration Formulation)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [DIFFMICP](#REF_HEADING_KEYWORD_DIFFMICP_8_3) keyword defines the diffusion coefficients assuming the mass concentration formulation for each component dissolved in water and for each PVT region, for when the molecular diffusion option has been activated by the [DIFFUSE](#__RefHeading___Toc349951_1539708736) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword should only be used if either the [MICP](#__RefHeading___Toc383375_111689907) or [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| 1 | MICRDIFF | A real positive number that declares the microbial concentration in water diffusion coefficient in the given PVT region. | None |
| --- | --- | --- | --- |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 2 | OXYGDIFF | A real positive number that declares the oxygen concentration in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| 3 | UREADIFF | A real positive number that declares the urea concentration in water diffusion coefficient in the given PVT region. | None |
| ft^2^/day | m^2^/day | cm^2^/hour |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Item 1 is only relevant for the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.28: DIFFMICP Keyword Description

#### Example

The example below is based on metric units, with NTPVT equal to one on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- PVT REGION MICP COMPONENT DIFFUSION COEFFICIENTS (OPM FLOW KEYWORD)

\--

DIFFMICP

\-- MICR IN OXYG IN UREA IN

\-- WAT DF WAT DF WAT DF

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

2E-04 2E-04 1E-04 / PVT REGION NO. 01
