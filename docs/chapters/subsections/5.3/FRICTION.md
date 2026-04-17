### FRICTION -- Activate Wellbore Friction Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FRICTION keyword activates the Wellbore Friction option and defines the maximum number of wellbore friction wells together with the maximum number of well branches.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | MXWELS | A positive integer defining the maximum number of wellbore friction wells for this model. | 0 |
| --- | --- | --- | --- |
| 3 | MXBRAN | A positive integer defining the maximum number of branches per well.<br>The default value of one implies a standard well with no branches. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.16: FRICTION Keyword Description

#### Example

\--

\-- WELL BRANCH

\-- MXWELS MXBRAN

FRICTION

5 1 /

The above example defines the maximum number of wellbore friction wells to be five and the maximum number of branches set to one, for standard wells.
