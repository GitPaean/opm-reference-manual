### BIOFPARA -- Define Properties for Models with Biofilms

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [BIOFPARA](#REF_HEADING_KEYWORD_BIOFPARA) keyword defines parameters for models including biofilms. For the parameters, biomass means both suspended microbes in the water phase (labeled as microbial) and biofilm. Currently the two available models with biofilm effects are the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and the [MICP](#__RefHeading___Toc383375_111689907) model. See Landa-Marbán et al[^1] and [^2] for further information on the [MICP](#__RefHeading___Toc383375_111689907) model parameters, which are also used in the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model.

| 1 | DENSBIOF | A real positive value that defines the density of the biofilm. | None |
| --- | --- | --- | --- |
| lb/rft^3^ | kg/rm^3^ | gm/rcc |  |
| 2 | DEATRATE | A real value that defines the biomass death rate. | None |
| 1/days | 1/days | 1/hours |  |
| 3 | GROWRATE | A real positive value that defines the maximum specific biomass growth rate. | None |
| 1/days | 1/days | 1/hours |  |
| 4 | HALFGROW | A real positive value that defines the half-velocity coefficient in the Monod equation for the biomass growth rate. | None |
| lb/rft^3^ | kg/rm^3^ | gm/rcc |  |
| 5 | YIELGROW | A real value that defines the yield biomass growth coefficient. | None |
| dimensionless | dimensionless | dimensionless |  |
| 6 | OXYGSUBS | A real value that defines the mass ratio of oxygen consumed to substrate used for biomass growth. | None |
| dimensionless | dimensionless | dimensionless |  |
| 7 | ATTARATE | A real positive value that defines the microbial attachment rate. | None |
| 1/days | 1/days | 1/hours |  |
| 8 | DETARATE | A real positive value that defines the biofilm detachment rate. | None |
| 1/days | 1/days | 1/hours |  |
| 9 | DETAEXPO | A real value that defines the exponent in the norm for the water velocity in the detachment term (this value was set to 0.58 in the [MICP publication](https://www.sciencedirect.com/science/article/pii/S1750583621000086)). | None |
| dimensionless | dimensionless | dimensionless |  |
| 10 | UREARATE | A real positive value that defines the maximum rate of urea utilization. | None |
| 1/days | 1/days | 1/hours |  |
| 11 | HALFUREA | A real positive value that defines the half-velocity coefficient in the Monod equation for the urea utilization rate. | None |
| lb/rft^3^ | kg/rm^3^ | gm/rcc |  |
| 12 | DENSCALC | A real positive value that defines the calcite density. | None |
| lb/rft^3^ | kg/rm^3^ | gm/rcc |  |
| 13 | YIELURCA | A real value that defines the yield coefficient in the calcite precipitation term (units of produced calcite over units of urea utilization). | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN vectors as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Items 10 to 13 are only relevant for the [MICP](#__RefHeading___Toc383375_111689907) model.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.87: BIOFPARA Keyword Description

#### Example

The example below is based on metric units, with NTSFUN equal to two on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- DEFINE BIOMASS PARAMETERS FOR THE MICP MODEL

\--

\-- DENS DEAT GROW HALF YIEL OXYG

\-- BIOF RATE RATE GROW GROW SUBS

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

\-- ATTA DETA DETA UREA HALF DENS YIEL

\-- RATE RATE EXPO RATE UREA CALC URCA

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

BIOFPARA

35 0.0275 3.6 2E-05 0.5 0.5

0.0735 2.6E-13 0.58 1391 21.3 2710 1.67 /

10 0.0275 3.6 2E-05 0.5 0.5

0.0735 1.1E-05 0.58 1391 21.3 2710 1.67 /

[^1]: Landa-Marbán, D., Tveit, S., Kumar, K., Gasda, S.E., 2021. Practical approaches to study microbially induced calcite precipitation at the field scale. Int. J. Greenh. Gas Control 106, 103256. https://doi.org/10.1016/j.ijggc.2021.103256.

[^2]: Landa-Marbán, D., Kumar, K., Tveit, S., Gasda, S.E., 2021. Numerical studies of CO2 leakage remediation by micp-based plugging technology. In: Røkke, N.A. and Knuutila, H.K. (Eds) Short Papers from the 11th International Trondheim CCS conference, ISBN: 978-82-536-1714-5, 284-290.
