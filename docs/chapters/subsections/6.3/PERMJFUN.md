### PERMJFUN -- Define Leverett J-Function Permeability for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PERMJFUN](#__RefHeading___Toc757292_2928331029) defines the permeability to be used in de-normalizing the Leverett J-Functions[^1] for when the PERM variable on the [JFUNC](#__RefHeading___Toc86297_3218818441) or the [JFUNCR](#__RefHeading___Toc257142_2369005893) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section has been set to "U", as oppose to using [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256), [PERMZ](#__RefHeading___Toc45795_719036256) arrays etc.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PERMJFUN](#__RefHeading___Toc757292_2928331029) | [PERMJFUN](#__RefHeading___Toc757292_2928331029) is an array of real positive numbers assigning the permeability to be used in de-normalizing the Leverett J-Function to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.102: PERMJFUN Keyword Description

For grid blocks that have not been assigned a [PERMJFUN](#__RefHeading___Toc757292_2928331029) value the default directional permeability will be used, that is the average of [PERMX](#__RefHeading___Toc45791_719036256) and [PERMY](#__RefHeading___Toc45793_719036256).

See also the [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) keywords to fully define the permeability for the model.

#### Example

\--

\-- DEFINE GRID BLOCK PERMJFUN FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PERMJFUN

100\*500.0 100\*50.0 100\*200.0 /

The above example defines the [PERMJFUN](#__RefHeading___Toc757292_2928331029) to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

[^1]: Leverett, M. C.; "Capillary Behaviour in Porous Solids", Trans. AIME (1941) 142, 152-168.
