### MSGFILE -- Activate or Deactivate Message File Output

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[MSGFILE](#__RefHeading___Toc66023_4106839650) keyword activates or deactivates the message file output used by pre- and post-processing software. Note that message file processing is not available in OPM Flow.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MSGOPT | A positive integer set to 0 for to deactivate message file output or 1 to activate message file output. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.22: MSGFILE Keyword Description

#### Example

\--

\-- OUTPUT

\-- OPTN

MSGFILE

0 /

The above example deactivates the message file output, but the keyword is ignored by OPM Flow.
