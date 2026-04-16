### EHYSTRR -- Define Hysteresis Model and Parameters via SATNUM

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [EHYSTRR](#__RefHeading___Toc212157_803326780) keyword defines the hysteresis model and associated parameters via the drainage [SATNUM](#__RefHeading___Toc71136_2752266063) allocation region array, for when the hysteresis option has been activated by the HYSTER variable on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Only the Killough[^1] model is available for this keyword and the keyword is optional.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. See also the [EHYSTR](#__RefHeading___Toc67396_621662414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) for an alternative keyword to enter the hysteresis model and associated parameters that is supported by OPM Flow

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
| > 1                                                                                                                                                                                  | > HYSTRCP | > HYSTRCP is a positive real value that defines the Killough curvature parameter for capillary pressure hysteresis model.                                                                                                                 | > 0.1 |
|                                                                                                                                                                                      |           |                                                                                                                                                                                                                                           |       |
|                                                                                                                                                                                      |           | > The value should range from 0.05 to 0.10.                                                                                                                                                                                               |       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
| > 2                                                                                                                                                                                  | > HYSTREL | > HYSTREL is a positive real number that defines the Killough's wetting phase relative permeability curvature parameter. This parameter is ignored if HYSMOD on the [EHYSTR](#__RefHeading___Toc67396_621662414) keyword is not set to 4. | > 1.0 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
| > 3                                                                                                                                                                                  | > HYSTSGR | > HYSTSGR is a positive real number that sets a scaling parameter for the trapped non-wetting phase saturation in the Killough model.                                                                                                     | > 0.1 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
| > Notes:                                                                                                                                                                             |           |                                                                                                                                                                                                                                           |       |
|                                                                                                                                                                                      |           |                                                                                                                                                                                                                                           |       |
| 1)  The keyword is followed by NTSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |           |                                                                                                                                                                                                                                           |       |
|                                                                                                                                                                                      |           |                                                                                                                                                                                                                                           |       |
| 2)   There is no "/" terminator for the keyword.                                                                                                                                     |           |                                                                                                                                                                                                                                           |       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+

Table 8.33: EHYSTRR Keyword Description

#### Example

\--

\-- HYSTERESIS MODEL AND PARAMETERS VIA SATNUM

\--

\-- PC-CUR RELPERM TRAPPED

\-- HYSTRCP HYSTREL HYSTSGR

EHYSTRR

0.04 1.0 1\* / SATNUM REGION 1

0.06 1.0 1\* / SATNUM REGION 2

0.08 1.0 1\* / SATNUM REGION 3

0.10 1.0 1\* / SATNUM REGION 4

0.10 1.0 1\* / SATNUM REGION 5

The above example defines the hysteresis model and parameters for when NTSFUN equals five on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that is for five [SATNUM](#__RefHeading___Toc71136_2752266063) regions.

[^1]: Killough, J. E. "Reservoir Simulation with History-dependent Saturation Functions," paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.
