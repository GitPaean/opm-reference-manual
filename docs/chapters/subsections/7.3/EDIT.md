### EDIT -- Define the Start of the EDIT Section of Keywords

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EDIT](#__RefHeading___Toc40641_784232322) activation keyword marks the end of the [GRID](#__RefHeading___Toc38674_784232322) section and the start of the [EDIT](#__RefHeading___Toc40641_784232322) section that enables modifications to the OPM Flow calculated properties derived from the data entered in the [GRID](#__RefHeading___Toc38674_784232322) section, for example grid block pore volumes via the [PORV](#__RefHeading___Toc96547_718313858) array and the transmissibilities via the [TRANX](#__RefHeading___Toc93085_718313858), [TRANY](#__RefHeading___Toc93087_718313858) and [TRANZ](#__RefHeading___Toc93089_718313858) family of keywords.

There is no data required for this keyword.

#### Example

\-- ==============================================================================

\--

\-- EDIT SECTION

\--

\-- ==============================================================================

EDIT

The above example marks the end of the [GRID](#__RefHeading___Toc38674_784232322) section and the start of the [EDIT](#__RefHeading___Toc40641_784232322) section in the OPM Flow data input file.
