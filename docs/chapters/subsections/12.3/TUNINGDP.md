### TUNINGDP -- Numerical Tuning Control for High Throughput Cases

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TUNINGDP keyword defines the parameters used for controlling the commercial simulator's numerical convergence parameters. This keyword is similar to the TUNING keyword in the SCHEDULE section, but the defaults on this keyword are optimized for high throughput runs.

This keyword is generally ignored by OPM Flow; however, the simulator can be instructed to read some parameters from the TUNINGDP keyword if the command line option \--enable-tuning=true has been used (see section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line)).

| 1 | TRGLCV | TRGLCV is a positive real value that specifies the linear convergence error target. The default value is ten times lower than the default value on the TUNING keyword. | 0.00001 |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| 2 | XXXLCV | XXXLCV is a positive real values that sets the maximum linear convergence error. The default value is ten times lower than the default value on the TUNING keyword. | 0.0001 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | TRGDDP | TRGDDP a positive real value that stipulates the maximum pressure change during a Newton iteration that enables the solution to be accepted when the residual pressure is still outside its convergence criteria. | 1.0 |
| psia | barsa | atma |  |
| 4 | TRGDDS | TRGDDS a positive real value that sets the maximum saturation change during a Newton iteration that enables the solution to be accepted when the residual saturation is still outside its convergence criteria. | 0.01 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | TRGDDRS | TRGDDRS a positive real value that sets the maximum gas dissolution factor change during a Newton iteration that enables the solution to be accepted when the residual gas dissolution factor is still outside its convergence criteria.<br>This is an OPM Flow specific item that is not supported by the commercial simulator. | 0.0 |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |
| 6 | TRGDDRV | TRGDDRV a positive real value that sets the maximum oil dissolution factor change during a Newton iteration that enables the solution to be accepted when the residual oil dissolution factor change is still outside its convergence criteria.<br>This is an OPM Flow specific item that is not supported by the commercial simulator. | 0.0 |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.67: TUNINGDP Keyword Description

Note that the TUNING keyword is stored on the restart files (see [RPTRST -- Define Data to be Written to the RESTART File](#anchor-3)) enabling the parameters to be utilized in a restart run without re-specifying the keyword.

#### Example

\--

\-- DEFAULT TUNINGDP PARAMETERS

\--

TUNINGDP

/

The above example explicitly sets the default parameters.
