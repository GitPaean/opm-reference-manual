### THCO2MIX -- Specify Thermal Mixing Models

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [THCO2MIX](#REF_HEADING_KEYWORD_THCO2MIX_8_3) keyword specifies the thermal mixing models for salt in the water phase, CO~2~ in the liquid phase and vaporized water in gas phase.

This is an OPM Flow specific keyword that should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword has been specified in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SALTMOD | A defined character string that specifies the thermal mixing model for salt in the liquid phase, and should be set to one of the following:<br>1)  NONE: pure water enthalpy will be used, or<br>2)  MICHAELIDES: account for salt concentration according to Michaelides[^1], 1981. | MICHAELIDES |
| 2 | LIQMOD | A defined character string that specifies the thermal mixing model for CO2 in the liquid phase, and should be set to one of the following:<br>1)  NONE: do not account for CO~2~ in brine,<br>2)  IDEAL: account for CO~2~ assuming an ideal mixture (based on mass fractions), or<br>3)  DUANSUN: also add the heat of dissolution for CO~2~ according to Dun and Sun[^2], 2003 (Fig. 6). | DUANSUN |
| 3 | GASMOD | A defined character string that specifies the thermal mixing model for vaporized water in the gas phase, and should be set to one of the following:<br>1)  NONE: pure CO~2\ ~enthalpy will be used, or<br>2)  IDEAL: account for vaporized water assuming an ideal mixture (based on mass fractions). | NONE |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.3.343.1: [THCO2MIX](#REF_HEADING_KEYWORD_THCO2MIX_8_3) Keyword Description

#### Example

The following example specifies the default thermal mixing models for salt in the liquid phase, CO~2~ in the liquid phase, and vaporized water in the gas phase.

\--

\-- SPECIFY THERMAL MIXING MODELS

\--

\-- SALT LIQUID GAS

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

THCO2MIX

MICHAELIDES DUANSUN NONE /

[^1]: Michaelides, E. E., "Thermodynamic Properties of Geothermal Fluids", Geothermal Resources Council, Trans. Vol. 5 (361-364), October 1981.

[^2]: Duan, Zhenhao, and Rui Sun. \"An improved model calculating CO2 solubility in pure water and aqueous NaCl solutions from 273 to 533 K and from 0 to 2000 bar.\" Chemical geology 193.3-4 (2003): 257-271.
