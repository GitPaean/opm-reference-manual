### MINPORV -- Set a Minimum Grid Block Pore Volume Threshold for All Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[MINPORV](#__RefHeading___Toc77711_2479612490) defines a minimum threshold pore volume that makes all grid blocks whose pore volume is below this value inactive in the model (inactive cells are not used in OPM Flow calculations). Note this keyword is different to the [MINPVV](#__RefHeading___Toc132765_2319858807) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, that sets a minimum threshold pore volume for individual cells in the model.

This keyword is an alias for the [MINPV](#__RefHeading___Toc569208_3181922006) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section, and thus provides the same functionality.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [MINPORV](#__RefHeading___Toc77711_2479612490) | [MINPORV](#__RefHeading___Toc77711_2479612490) is a real positive number that defines the minimum pore volume for a cell to be active in the model. | Defined |
| rb<br>1.0e-6 | rm^3^<br>1.0e-6 | rcc<br>1.0e-6 |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.62: MINPORV Keyword Description

The [MINPORV](#__RefHeading___Toc77711_2479612490), [MINPV](#__RefHeading___Toc569208_3181922006), and [MINPVV](#__RefHeading___Toc132765_2319858807) keywords only apply their minimum threshold pore volume values to active cells. Thus, cells that have been made inactive via setting their [ACTNUM](#__RefHeading___Toc4410_421927891) values to zero, remain inactive, even if their pore volume exceeds the values set by the [MINPORV](#__RefHeading___Toc77711_2479612490), [MINPV](#__RefHeading___Toc569208_3181922006), and [MINPVV](#__RefHeading___Toc132765_2319858807) keywords.

Secondly, although the [MINPORV](#__RefHeading___Toc77711_2479612490) keyword allows one to set a minimum threshold pore volume below the default value, this is not recommended, as cells with small pore volumes can cause significant numerical convergence errors. Thus, in practice, values greater than the default values are normally applied to eliminate cells that have relatively small pore volumes. In addition, the simulator reports the total pore volume and the number of cells made inactive, as well as the pore volume reduction, when the keyword is invoked; allowing one to run some sensitivities to the minimum pore volume value.

See also the [PINCH](#__RefHeading___Toc74261_2479612490) keyword for the treatment of inactive grid cells and pinch-outs.

#### Example

\--

\-- MINIMUM PORE VOLUME FOR ACTIVE CELLS

\--

MINPORV

500.0 /

The above example defines 500 rb (or m3) as the minimum pore volume for a cell to be active in the model.
