### WELPI -- Define Well Productivity and Injectivity Indices

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WELPI](#__RefHeading___Toc121389_332691817) keyword is used to define a well's productivity or injectivity index at the time the keyword is activated. Productivity and injectivity indices are a function of both bottom-hole pressure and mobility and thus will vary in time as the bottom-hole pressure and fluids produce by the well are changing. Thus, the values enter on this keyword for a given well will override any previously calculated values, or values previously entered, using this keyword. This keyword should only be invoked after a well's connection factors have been declared via the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well productivity index is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | [WELPI](#__RefHeading___Toc121389_332691817) | A real positive value that defines the productivity or injectivity of a well at the time the keyword is activated in the input deck. Subsequent use of the keyword for a given well will override all previously entered data, including the original productivity index calculated from the well's [COMPDAT](#__RefHeading___Toc97651_3261743917) connection data. Note that:<br>1)  Only the connections currently *opened* will have their connection factors re-scaled to honor the productivity and injectivity index. Connections not opened will remain unchanged.<br>2)  Additional, previously defined connections added to the well at a later time, will not be influenced by a previous [WELPI](#__RefHeading___Toc121389_332691817) keyword. It may therefore be necessary to add another [WELPI](#__RefHeading___Toc121389_332691817) keyword at the time the new connections are opened, if desired.<br>3)  However, re-defining connections via the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword resets the calculated productivity and injectivity index for those re-defined connections in the well.<br>Subsequent usage of the keyword for the same well may lead to unintended values; use the WPI series of variables in the [SUMMARY](#__RefHeading___Toc43949_784232322) section to output and verify that the values are consistent with the desired results. | 1.0 |
| Liquid stb/d/psia<br>Gas Mscf/d/psia | Liquid sm^3^/day/bars<br>Gas sm3/day/bars | Liquid scc/hour/atm<br>Gas scc/hour/atm |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.89: WELPI Keyword Description

Note that only a well's currently opened connection factors, as entered via the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword, are re~~-~~scaled to match the required productivity and injectivity index. See section [[Well Productivity](#anchor-2)](#12.2.3.Well Productivity|outline) on well productivity for further information on well productivity.

See also the [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to set the productivity and injectivity index for a well by scaling the current index by a scaling factor.

#### Example

\--

\-- DEFINE WELL PRODUCTIVITY/INJECTIVITY INDEX

\--

\-- WELL PI

\-- NAME MULT

WELPI

OP01 1.250 /

OP02 2.750 /

OP03 1.100 /

/

In the above example the oil wells are are defined as having a well productivity indices of 1.250, 2.750 and 1.100 for the OP01, OP02 and OP03 wells, respectively.
