### FIPOWG -- Activate Oil, Gas, and Water FIP Zone Reporting

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FIPOWG](#__RefHeading___Toc93831_3812137098) keyword activates automatic fluid in-place reporting based on the initial oil, gas and water zones defined by the initial equilibration. The fluid contacts on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section determine the reporting fluid category a grid cell belongs to. For example all grid cells with depths above the gas-oil contact on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword will be assigned to the gas zone and reported accordingly. Similarly, grid cells with depths between the gas-oil contact and the water-oil contact will be assigned to the oil zone. And finally, grid cells with depths below the oil-water contact will be assigned to the water zone. The simulator can print out summaries of the fluid in-place in each region, the current flow rates between regions, and the cumulative flows between regions.

Note that the total number of [FIP](#__RefHeading___Toc250560_252421755) and [FIPNUM](#__RefHeading___Toc77229_2752266063) regions must be defined by the NMFIPR variable on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- ACTIVATE OIL, GAS, AND WATER FIP ZONE REPORTING

\--

FIPOWG

The above example switches on automatic fluid in-place reporting based on the initial oil, gas and water zones defined by the initial equilibration.
