### RPTISOL -- Activate Isolated Reservoir Number Reporting

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RPTISOL](#__RefHeading___Toc310670_516898843) keyword activates the isolated reservoir report that generates an array of isolated region numbers that is printed in the debug file (\*.DBG). The main purpose of this facility is to use the generated array as input to the [ISOLNUM](#__RefHeading___Toc69656_3218818441) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section in conjunction with the Independent Reservoir Regions option. If the model can be divided into isolated reservoirs then the individual reservoirs may be solved independently, resulting in increased computational efficient, compared with solving the model as a whole.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE ISOLATED RESERVOIR NUMBER REPORTING

\--

RPTISOL

The above example activates the isolated reservoir report that generates an array of isolated region numbers to the debug file (\*.DBG).
