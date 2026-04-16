### LOWSALT -- Activate the Low Salt Brine Phase in the Brine Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [LOWSALT](#__RefHeading___Toc331072_2843394514), activates the low salt brine phase for the Brine option and also activates the Brine option. See also the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE THE LOW SALT BRINE PHASE FOR THE BRINE OPTION

\--

LOWSALT

The above example declares that the low salt brine phase is active in the model for the Brine option.
