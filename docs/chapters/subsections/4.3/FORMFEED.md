### FORMFEED -- Defined the Print File Form-Feed Character

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FORMFEED keyword defines the form-feed character, or carriage control character, for the output print (\*.PRT) run summary (\*.RSM) files. The keyword should be place at the very top of the input file.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FORMFEED | Defines a single integer that defines the carriage control character activates, and should be set to:<br>1)  1 -- Standard FORTRAN (the default).<br>2)  2 -- Form-feed character ASCII(12)<br>3)  3 -- None. | 0 |
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
