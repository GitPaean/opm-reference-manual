### EOSNUM -- Define the Equation of State Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) keyword defines the Equation Of State ([EOS](#REF_HEADING_KEYWORD_EOS_5_3)) region number for all the cells in the model via an array. The region number specifies which Equation Of State is used in each grid block. The keyword should only be used if the compositional mode has been requested using the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) | [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) is an array of positive integers less than or equal to NMEOSR that define the [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region number for each cell in the model.<br>The NMEOSR variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section defines the number of [EOS](#REF_HEADING_KEYWORD_EOS_5_3) regions in the model. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table : [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) Keyword Description

#### Examples

The example below sets two [EOS](#REF_HEADING_KEYWORD_EOS_5_3)NUM regions for a 4 x 5 x 2 model.

\--

\-- DEFINE EOSNUM REGIONS FOR ALL CELLS

\--

EOSNUM

20\*1

20\*2

/
