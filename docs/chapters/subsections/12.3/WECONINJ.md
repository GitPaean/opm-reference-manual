### WECONINJ -- Well Economic Criteria for Injection Wells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WECONINJ](#__RefHeading___Toc949620_487874538) keyword defines economic criteria for injection wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONINJE](#__RefHeading___Toc146750_4203985108) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Note that wells can be allocated to a group when they are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword and groups can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and the controls specified by this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well economic injection criteria data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | [MINVALUE](#__RefHeading___Toc296605_1576177388) | A real positive value that defines the minimum economic injection value, below which an economic action will take place, as defined by the AUTO parameter on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword (SHUT or STOP). Note that TYPE determines if the minimum value is applied to the well's actual injection rate or the well's potential.<br>A value less than or equal to zero switches off this criterion. | 0.0 |
| Liquid stb/d<br>Gas Mscf/d | Liquid sm^3^/day<br>Gas sm3/day | Liquid scc/hour<br>Gas scc/hour |  |
| 3 | TYPE | A defined character string that determines if [MINVALUE](#__RefHeading___Toc296605_1576177388) is applied to a well's actual rate or potential, and should be set to one of the following:<br>1)  RATE: In this case the [MINVALUE](#__RefHeading___Toc296605_1576177388) is applied to a well's actual rate.<br>2)  POTN: Here, [MINVALUE](#__RefHeading___Toc296605_1576177388) is applied to the well's potential with only the BHP and THP constraints applied.<br>The default value is RATE. | RATE |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.82: WECONINJ Keyword Description

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define a wells shut-in or stop options and [GCONINJE](#__RefHeading___Toc134874_2055188184) for group controls in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the economic injection parameters for all gas and water injection wells.

\--

\-- WELL ECONOMIC LIMIT DATA FOR INJECTION WELLS

\--

\-- WELL MIN RATE

\-- NAME VALUE POTN

WECONINJ

GI\* 2.0E3 RATE /

WI\* 5.0E3 POTN /

/

Here all the gas injection wells have a minimum economic gas injection rate of 2 MMscf/d and the water injection wells have a minimum water potential rate of 5,000 stb/d. The AUTO parameter on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword will determine if the wells will be shut-in or stopped.
