### NRSOUT -- Defined Maximum Number of RESTART Elements

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [NRSOUT](#__RefHeading___Toc274544_718033703) keyword specifies the maximum number of elements that can be written to the [RESTART](#__RefHeading___Toc135629_1317547213) file at each reporting time step.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NRSOUT | A positive integer value that specifies the maximum number of elements that can be written to the [RESTART](#__RefHeading___Toc135629_1317547213) file at each reporting time step. | 3600 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.28: NRSOUT Keyword Description

#### Example

\--

\-- MAX

\-- NRSOUT

NRSOUT

6000 /

The above example sets the maximum number of elements that can be written to the [RESTART](#__RefHeading___Toc135629_1317547213) file at each reporting time step to 6000.
