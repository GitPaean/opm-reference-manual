### NUMRES -- Define the Number of Reservoir Grids

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NUMRES keyword defines the number of reservoir grids (COORD data sets) that the simulator should process. OPM Flow currently only supports a single reservoir grid.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NUMRES | A positive integer that defines the number of COORD data sets to be processed by OPM Flow.<br>OPM Flow currently only supports a single reservoir grid and so this item should be defaulted (1\*) or set to one. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.30: NUMRES Keyword Description

#### Example

\--

\-- DEFINE THE NUMBER OF RESERVOIR GRIDS (COORD DATA SETS)

\--

NUMRES

1 /

The above example sets the maximum number of COORD data sets to be processed to one.
