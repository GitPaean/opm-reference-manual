### PERMY -- Define the Permeability in the Y Direction for All the Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PERMY](#__RefHeading___Toc45793_719036256) defines the permeability in the Y direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PERMY](#__RefHeading___Toc45793_719036256) | [PERMY](#__RefHeading___Toc45793_719036256) is an array of real positive numbers assigning the permeability in the Y direction to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.106: PERMY Keyword Description

See also the [PERMX](#__RefHeading___Toc45791_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) keywords to fully define the permeability for the model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PERMY

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the [PERMY](#__RefHeading___Toc45793_719036256) to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
