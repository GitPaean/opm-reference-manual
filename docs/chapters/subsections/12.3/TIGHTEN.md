### TIGHTEN -- Tighten and Relax Numerical Controls

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TIGHTEN keyword tightens up or slackens the numerical controls for the linear, non-linear and material balance convergence targets and also tightens or relaxes the maximum values for the aforementioned parameters. The keyword should be used with caution as it may result in significantly increasing the run times.

Note that any subsequent use of the TUNING keyword in the SCHEDULE section will result in resetting the numerical controls. See also the TIGHTENP in the SCHEDULE section that allows for greater flexibility in modifying the numerical controls.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
