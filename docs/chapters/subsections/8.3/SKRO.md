### SKRO -- End-Point Scaling of Grid Cell Kro(Swl) (Surfactant)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SKRO](#__RefHeading___Toc1255617_516898843) defines the scaling parameter for the surfactant oil relative permeability value at the connate water saturation ([SWL](#__RefHeading___Toc22881_7842323221)), for all the cells in the model via an array. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Surfactant option must be enabled by either the [SURFST](#__RefHeading___Toc1173151_4250154414) or [SURFSTES](#__RefHeading___Toc1173153_4250154414) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SKRO](#__RefHeading___Toc1255617_516898843) | [SKRO](#__RefHeading___Toc1255617_516898843) is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling [SKRO](#__RefHeading___Toc1255617_516898843) values for each cell in the model.<br>Repeat counts may be used, for example 50\*0.500. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.158: SKRO Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be scale on the relative permeability values using the [SKRO](#__RefHeading___Toc1255617_516898843), [SKRORG](#__RefHeading___Toc70189_3358172232), [SKRORW](#__RefHeading___Toc70191_3358172232), [SKRW](#__RefHeading___Toc537530_38555213) and [SKRWR](#__RefHeading___Toc70193_3358172232) surfactant relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

The example defines an input box for the whole grid and for layers one to three, for layer one [SKRO](#__RefHeading___Toc1255617_516898843) is set equal to 0.850, for layer two [SKRO](#__RefHeading___Toc1255617_516898843) equals 0.875, and for layer three [SKRO](#__RefHeading___Toc1255617_516898843) equals 0.900.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 1 3 / DEFINE BOX AREA

\--

\-- SET SKRO VALUES FOR THREE LAYERS IN THE MODEL

\--

SKRO

1000\*0.855 1000\*0.875 1000.0.900 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX
