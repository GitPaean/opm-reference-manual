### SSWU -- End-Point Scaling Grid Cell Surfactant Maximum Water Saturation

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SSWU](#__RefHeading___Toc837482_4250154414) defines the surfactant maximum water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword and the surfactant phase has been activated by the [SURFACT](#__RefHeading___Toc863854_4250154414) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The maximum water saturation is defined as the maximum water saturation in a two-phase water relative permeability table. [SSWU](#__RefHeading___Toc837482_4250154414) scales the surfactant water relative permeability data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SSWU](#__RefHeading___Toc837482_4250154414) | [SSWU](#__RefHeading___Toc837482_4250154414) is an array of real numbers assigning the surfactant maximum water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword.<br>Repeat counts may be used, for example 30\*0.70 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.179: SSWU Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SSWL](#__RefHeading___Toc837484_4250154414), [SSWCR](#__RefHeading___Toc837495_4250154414), [SSWU](#__RefHeading___Toc837482_4250154414), [SSGL](#__RefHeading___Toc811291_4250154414), [SSGCR](#__RefHeading___Toc811289_4250154414), SSGU, [SSOWCR](#__RefHeading___Toc830913_4250154414), and [SSOGCR](#__RefHeading___Toc817831_4250154414) saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and [SKRW](#__RefHeading___Toc537530_38555213) relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SSWU DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SSWU

300\*0.700 /

The above example defines a constant surfactant connate gas saturation of 0.70 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
