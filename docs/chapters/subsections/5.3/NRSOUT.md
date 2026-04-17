### NRSOUT -- Defined Maximum Number of RESTART Elements

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NRSOUT keyword specifies the maximum number of elements that can be written to the RESTART file at each reporting time step.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NRSOUT | A positive integer value that specifies the maximum number of elements that can be written to the RESTART file at each reporting time step. | 3600 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.28: NRSOUT Keyword Description

#### Example

\--

\-- MAX

\-- NRSOUT

NRSOUT

6000 /

The above example sets the maximum number of elements that can be written to the RESTART file at each reporting time step to 6000.
