### TITLE -- Define the Title for the Input Deck

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [TITLE](#__RefHeading___Toc37371_784232322) keyword defines the title for the input deck. The title text will be printed on all reports so as to act as a reference for the run.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TITLE | A character string that defines the title for the input deck | None￹ |
| Notes:<br>1)  All the characters on the line following the [TITLE](#__RefHeading___Toc37371_784232322) keyword are processed as a string and therefore there is no need to enclose the title in quotes.<br>2)  There is no terminator "/" for the keyword. |  |  |  |

Table 5.47: TITLE Keyword Description

#### Example

\--

\-- DEFINE THE TITLE FOR THE RUN

TITLE

SPE01-THEM01-OPM1810-R01 - OPM THERMAL OPTION RUN

The above example defines the title for the run to be "SPE01-THEM01-OPM1810-R01 - OPM THERMAL OPTION RUN".
