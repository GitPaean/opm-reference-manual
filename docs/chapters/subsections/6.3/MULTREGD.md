### MULTREGD -- Multiply Diffusivities Between Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MULTREGD](#__RefHeading___Toc246602_1841740821) keyword multiplies the diffusivity between two regions by a constant. The region number array can be [FLUXNUM](#__RefHeading___Toc45781_719036256), [MULTNUM](#__RefHeading___Toc61329_2752266063) or [OPERNUM](#__RefHeading___Toc67857_718313858) and these arrays must be defined and be available before the [MULTREGD](#__RefHeading___Toc246602_1841740821) keyword is read by the simulator. The constant should be a real number.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION1 | A positive integer value that defines the from REGION number for which the CONSTANT in (3) should be applied. | None |
| 2 | REGION2 | A positive integer value that defines the to REGION number for which the CONSTANT in (3) should be applied. | None |
| 3 | CONSTANT | A real value to multiply the diffusivity between REGION1 and REGION2. | 1 |
| 4 | DIR | A character string that defines the direction to apply the diffusivity multiplier between the two regions, should be set to one of the following X, Y, Z, XY, XZ, YZ, or XYZ. | XYZ |
| 5 | TYPE | A character string that defines the type of connections the diffusivity multiplier should be applied to, should be one of the following:<br>1)  [NNC](#__RefHeading___Toc63285_718313858) -- Only apply the diffusivity multiplier between REGION1 and REGION2 to non-neighbor connections.<br>2)  [NONNC](#__RefHeading___Toc77075_4106839650) -- Do not apply the diffusivity multiplier between REGION1 and REGION2 to non-neighbor connections.<br>3)  [ALL](#__RefHeading___Toc4420_421927891) - Apply the diffusivity multiplier between REGION1 and REGION2 to all connections. | [ALL](#__RefHeading___Toc4420_421927891) |
| 6 | REGION<br>ARRAY | The REGION ARRAY to use for applying the CONSTANT in (3) based on the regions REGION1 and REGION2 in (1 and 2). REGION ARRAY can have the following values:<br>1)  F for the [FLUXNUM](#__RefHeading___Toc45781_719036256) array<br>2)  M for the [MULTNUM](#__RefHeading___Toc61329_2752266063) array<br>3)  O for the [OPERNUM](#__RefHeading___Toc67857_718313858) array | M |
| Notes:<br>1)  Where REGION1 and REGION2 should be less than or equal to the maximum number of regions as defined on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword for the [FIPNUM](#__RefHeading___Toc77229_2752266063) and [OPERNUM](#__RefHeading___Toc67857_718313858) arrays or the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword for the [MULTNUM](#__RefHeading___Toc61329_2752266063) array in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  If REGION1 is defaulted then the diffusivities between REGION2 and all other regions will be multiplied. Similarly, if REGION2 is defaulted then the diffusivities between REGION1 and all other regions will be multiplied. If both REGION1 and REGION2 are defaulted then the diffusivities between all pairs of regions will be multiplied.<br>3)  If REGION1 and REGION2 are equal and positive then all the diffusivities within that region as well as the diffusivities between that region and all other regions will be multiplied.<br>4)  If the same combination of REGION1 and REGION2 is repeated then only the latest multiplier will be used regardless of whether the REGION ARRAY specified is the the same or not.<br>5)  If the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword is not present in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section or if the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword is present but the maximum number of [MULTNUM](#__RefHeading___Toc61329_2752266063) regions (NRMULT) equals zero then REGION ARRAY will default to F for the [FLUXNUM](#__RefHeading___Toc45781_719036256) array.<br>6)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.76: MULTREGD Keyword Description

#### Example

\--

\-- MULTIPLY DIFFUSIVITIES BETWEEN RESERVOIRS

\--

\-- REGION REGION DIFFS DIREC NNC REGION ARRAY

\-- FROM TO MULT OPT OPTS M / F / O

MULTREGD

1\* 1\* 1.05 1\* \'ALL\' M / ALL REGIONS

/

The above example multiplies the diffusivities between all the [MULTNUM](#__RefHeading___Toc61329_2752266063) regions by 1.05 in all directions and for all connections types.
