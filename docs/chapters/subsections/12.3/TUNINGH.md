### TUNINGH -- Numerical Tuning Control for History Match Gradient Calculations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Defines the parameters used for controlling the commercial simulator's numerical convergence parameters. The keyword is similar to the TUNING keyword in the SCHEDULE section, but the defaults on this keyword are optimized for high throughput runs. See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| 1 | GRGLCV | GRGLCV is a real positive value that specifies the linear convergence error target. | 0.0001 |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| 2 | GXXLCV | GXXLCV is a real positive values that sets the maximum linear convergence error. | 0.001 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GMSLCV | GMSLCV is a real positive value that specifies the linear convergence residual reduction. | 1.0 x 10^-^20 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | LGTMIN | LGTMIN is a positive integer less or equal to LGTMAX that sets the minimum number of linear iterations within a Newton iteration. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | LGTMAX | LGTMAX is a positive integer greater or equal to LGTMIN that sets the maximum number of linear iterations within a Newton iteration. | 25 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  There is no keyword terminating "/". |  |  |  |

Table 12.68: TUNINGH Keyword Description

#### Example

\--

\-- DEFAULT TUNINGH PARAMETERS

\--

TUNINGH

/

The above example explicitly sets the default parameters.
