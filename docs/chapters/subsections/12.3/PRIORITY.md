### PRIORITY -- Activate and Define Well Prioritization Coefficients

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PRIORITY keyword activates the Well Priority option and defines the coefficients in the well priority equation. Wells under group control are ranked based on their well potential in order to satisfy group controls. For example if a group's oil target is exceeded, then the group may shut-in the lease productive oil wells based on their well potential. The Priority option is an alternative form of ranking the wells based on the following equation:

Where:

Q~oil~ = well oil potential

Q~water~ = well water potential

Q~gas~ = well gas potential

a~1-4\ ~= priority coefficients supplied by this keyword

b~1-4\ ~= priority coefficients supplied by this keyword

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | TIME | A real positive integer that defines the minimum time interval between executing the well priority calculation. The calculation is performed at the beginning of the time step that exceeds the previous calculation (t0) by a minimum of TIME, that is for when tn ≥ ( t0 + TIME).<br>Note that the default value of zero means that the calculation is performed at each time step. As a consequence, this may result in some oscillation as well wells are switched on/off at subsequent time steps. | 0 |
| --- | --- | --- | --- |
| days | days | hours |  |
| 2 | A1 | A real positive integer greater than or equal to zero that defines a~1~ priority coefficient in equation . | 0 |
| 3 | A2 | A real positive integer greater than or equal to zero that defines a~2~ priority coefficient in equation . | 0 |
| 4 | A3 | A real positive integer greater than or equal to zero that defines a~3~ priority coefficient in equation . | 0 |
| 5 | A4 | A real positive integer greater than or equal to zero that defines a~4~ priority coefficient in equation . | 0 |
| 6 | B1 | A real positive integer greater than or equal to zero that defines b~1~ priority coefficient in equation . | 0 |
| 7 | B2 | A real positive integer greater than or equal to zero that defines b~2\ ~priority coefficient in equation . | 0 |
| 8 | B3 | A real positive integer greater than or equal to zero that defines b~3\ ~priority coefficient in equation . | 0 |
| 9 | B4 | A real positive integer greater than or equal to zero that defines b~4~ priority coefficient in equation . | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 12.59: PRIORITY Keyword Description*
#### Example

\--

\-- SETS COEFFICIENTS FOR WELL PRIORITIZATION OPTION

\--

\-- TIME A B C D E F G H

\-- STEP Qo Qw Qg Qo Qw Qg

PRIORITY

0.0 0.0 1.0 0.0 0.0 1.0 0.0 0.0 0.0 / High Oil Pot

\-- 0.0 0.0 1.0 1.0 0.0 0.0 0.0 1.0 0.0 / Low Water Cut Pot

\-- 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 1.0 / Low GOR Pot

The above example defines the well priority calculation to be based on a well's oil potential, with calculation to be performed at each time step. Note that the low water cut and low GOR options are given for reference but are commented out and therefore ignored by the simulator.
