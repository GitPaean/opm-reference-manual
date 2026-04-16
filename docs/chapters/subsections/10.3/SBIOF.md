### SBIOF -- Define The Initial Equilibration Biofilm Volume Fraction For All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SBIOF](#__RefHeading___Toc394934_111689907) keyword defines the initial equilibration biofilm volume fraction for all grid cells in the model. The keyword should only be used if either the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or [MICP](#__RefHeading___Toc383375_111689907) model has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SBIOF](#__RefHeading___Toc394934_111689907) | [SBIOF](#__RefHeading___Toc394934_111689907) is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration biofilm volume fraction values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  Physical values are less or equal to the grid cell porosity. For the [MICP](#__RefHeading___Toc383375_111689907) model, then the sum of [SBIOF](#__RefHeading___Toc394934_111689907) and [SCALC](#__RefHeading___Toc406066_111689907) has to be less or equal to the grid cell porosity.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 10.41: SBIOF Keyword Description

For both [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and [MICP](#__RefHeading___Toc383375_111689907) models, see also the [SMICR](#__RefHeading___Toc428289_111689907) keyword, and for the [MICP](#__RefHeading___Toc383375_111689907) model, the [SCALC](#__RefHeading___Toc406066_111689907), [SOXYG](#__RefHeading___Toc439460_111689907), and [SUREA](#__RefHeading___Toc450660_111689907) keywords to define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION BIOFILM VOLUME FRACTION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SBIOF

10000\*0.0000 10000\*0.0000 10000\*0.0010 /

The above example defines the initial equilibration biofilm volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.
