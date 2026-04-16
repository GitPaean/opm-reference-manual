### SKRW -- End-Point Scaling of Grid Cell Krw(Sw =1.0) (Surfactant)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SKRW](#__RefHeading___Toc537530_38555213) defines the scaling parameter at the maximum surfactant water relative permeability value ([SWU](#__RefHeading___Toc22883_7842323221)), that is for Sw = 1.0, for all the cells in the model via an array. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Surfactant option must be enabled by either the [SURFST](#__RefHeading___Toc1173151_4250154414) or [SURFSTES](#__RefHeading___Toc1173153_4250154414) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SKRW](#__RefHeading___Toc537530_38555213) | [SKRW](#__RefHeading___Toc537530_38555213) is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling [SKRW](#__RefHeading___Toc537530_38555213) values for each cell in the model.<br>Repeat counts may be used, for example 50\*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.161: SKRW Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be scale on the relative permeability values using the [SKRO](#__RefHeading___Toc1255617_516898843), [SKRORG](#__RefHeading___Toc70189_3358172232), [SKRORW](#__RefHeading___Toc70191_3358172232), [SKRW](#__RefHeading___Toc537530_38555213) and [SKRWR](#__RefHeading___Toc70193_3358172232) surfactant relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

The example uses the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword to set [SKRW](#__RefHeading___Toc537530_38555213) for layer one equal to 0.850, layer two [SKRW](#__RefHeading___Toc537530_38555213) to 0.875, and layer three [KRW](#__RefHeading___Toc97397_621662414) to 0.900.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SKRW 0.8550 1\* 1\* 1\* 1\* 1 1 / SKRW FOR LAYER 1

SKRW 0.8750 1\* 1\* 1\* 1\* 2 2 / SKRW FOR LAYER 2

SKRW 0.9000 1\* 1\* 1\* 1\* 3 3 / SKRW FOR LAYER 3

/
