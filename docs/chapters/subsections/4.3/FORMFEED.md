### FORMFEED -- Defined the Print File Form-Feed Character

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FORMFEED](#__RefHeading___Toc322374_803326780) keyword defines the form-feed character, or carriage control character, for the output print (\*.PRT) run summary (\*.RSM) files. The keyword should be place at the very top of the input file.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [FORMFEED](#__RefHeading___Toc322374_803326780) | Defines a single integer that defines the carriage control character activates, and should be set to:<br>1)  1 -- Standard FORTRAN (the default).<br>2)  2 -- Form-feed character ASCII(12)<br>3)  3 -- None. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 4.3: FORMFEED Keyword Description

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE EXTRAPOLATION MESSAGES

\--

FORMFEED

3 /

The above example sets the carriage return character to no form-feed character.
