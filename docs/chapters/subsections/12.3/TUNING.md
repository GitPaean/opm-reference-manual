<a id="__RefHeading___Toc146744_4203985108"></a>

### TUNING -- Numerical Tuning Control

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TUNING keyword defines the parameters used to control the commercial simulator's time stepping and numerical convergence for the global grid. The keyword is similar to the TUNINGDP keyword in the SCHEDULE section that is optimized for high throughput runs. The keyword is mostly ignored by OPM Flow; however, the simulator can be instructed to read some parameters from the TUNING keyword if the appropriate command line parameter has been activated (see section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line)).

| 1-1 | TSINIT | TSINIT is a positive real value that defines the maximum length of the next time step.<br>Note that whenever the keyword is used TSINIT is always set back to the default value of one, unless explicitly over written. | 1.0 |
| --- | --- | --- | --- |
| days | days | hours |  |
| 1-2 | TSMAXZ | TSMAXZ is a positive real value that defines the maximum length of time steps following the next time step (TSINIT). | 365.0 |
| days | days | hours |  |
| 1-3 | TSMINZ | TSMINZ is a positive real value that defines the minimum length of all time steps. | 0.1 |
| days | days | hours |  |
| 1-4 | TSMCHP | TSMCHP is a positive real value that sets the minimum time step length that can be chopped. | 0.15 |
| days | days | hours |  |
| 1-5 | TSFMAX | TSFMAX is a positive real value that specifies the maximum growth rate a time step can be increased by, subject to the maximum allowable time step size set by TSMAXZ.<br>For example, if the current time step has converged at 10 days and TSFMAX is set to the default value, then the next time step will be 3.0 x 10 days, that is 30 days provided it is less than TSMAXZ. | 3.0 |
| dimensionless | dimensionless | dimensionless |  |
| 1-6 | TSFMIN | TSFMIN is a positive real value that specifies the minimum decay rate a time step can be decreased by, subject to the minimum allowable time step size set by TSMINZ.<br>For example, if the current time step has not converged at 10 days and TSFMIN is set to the default value, then the next time step will be 0.3 x 10 days, that is the maximum of 3 days and TSMINZ. | 0.3 |
| dimensionless | dimensionless | dimensionless |  |
| 1-7 | TSFCNV | TSFCNV is a positive real value that specifies the decay rate a time step can be decreased by after a convergence failure. | 0.1 |
| dimensionless | dimensionless | dimensionless |  |
| 1-8 | TFDIFF | TFDIFF is a positive real value that sets the time step growth factor of the time step after a convergence failure.<br>For example, if the chopped current convergent time step is 10 days and TFDIFF is set to the default value, then the time step will be increased to 1.25 x 10 days, that is the minimum of 12.5 days and TSMAXZ. | 1.25 |
| dimensionless | dimensionless | dimensionless |  |
| 1-9 | THRUPT | THRURT is a positive real value that specifies the maximum throughput ratio over a time step. | 1.0 x 10^20^ |
| dimensionless | dimensionless | dimensionless |  |
| 1-10 | TMAXWC | TMAXWC is a positive real value that defines maximum allowed time step after a well event; for example, when a well is opened or closed, etc. | None |
| days | days | hours |  |
| 1-11 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | TRGTTE | TRGTTE is a positive real value that sets the target time truncation error. | 0.1 |
| dimensionless | dimensionless | dimensionless |  |
| 2-2 | TRGCNV | TRGCNV is a positive real value that defines the target non-linear convergence error. | 0.001 |
| dimensionless | dimensionless | dimensionless |  |
| 2-3 | TRGMBE | TRGMBE is a positive real value that specifies the target material balance error. | 1.0 x 10^-7^ |
| dimensionless | dimensionless | dimensionless |  |
| 2-4 | TRGLCV | TRGLCV is a positive real value that specifies the target linear convergence error. | 0.0001 |
| dimensionless | dimensionless | dimensionless |  |
| 2-5 | XXXTTE | XXXTTE is a positive real value that sets the maximum time truncation error. | 10.0 |
| dimensionless | dimensionless | dimensionless |  |
| 2-6 | XXXCNV | XXXCNV is a positive real value that defines the maximum non-linear convergence error. | 0.01 |
| dimensionless | dimensionless | dimensionless |  |
| 2-7 | XXXMBE | XXXMBE is a positive real value that specifies the maximum mass balance error, that is the tolerated mass balance error relative to total mass present. | 1.0 x 10^-6^ |
| dimensionless | dimensionless | dimensionless |  |
| 2-8 | XXXLCV | XXXLCV is a positive real values that sets the maximum linear convergence error. | 0.0001 |
| dimensionless | dimensionless | dimensionless |  |
| 2-9 | XXXWFL | XXXWFL is a positive real values that fixes the maximum well flow convergence error. | 0.001 |
| dimensionless | dimensionless | dimensionless |  |
| 2-10 | TRGFIP | TRGFIP is a positive real value that stipulates the target fluid in-place error in Local Grid Refinements. | 0.025 |
| dimensionless | dimensionless | dimensionless |  |
| 2-11 | TRGSFT | TRGSFT is a positive real values that defines the target surfactant change when the Surfactant Model is active in the run. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2-12 | THIONX | THIONX is a positive real value used to set the threshold for damping in the ion echange calculation for when the Brine Model is active in the run. | 0.01 |
| dimensionless | dimensionless | dimensionless |  |
| 2-13 | TRWGHT | TRWGHT is an integer that stipulates the implicitness for active tracer updates within the Newton iterations, and should be set to:<br>0.   The calculation is explicit, that is fully decoupled.<br>1.   The calculation is implicit, that is fully coupled. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 2-14 | / | Record terminated by a "/" | Not Applicable |
| 3-1 | NEWTMX | NEWTMX is a positive integer greater or equal to NEWTMN that stipulates the maximum number of Newton iterations for a time step. | 12 |
| dimensionless | dimensionless | dimensionless |  |
| 3-2 | NEWTMN | NEWTMN is a positive integer that is less or equal to NEWTMX that defines the minimum number of Newton iterations for a time step. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 3-3 | LITMAX | LITMAX is a positive integer greater or equal to LITMIN that sets the maximum number of linear iterations within a Newton iteration. | 25 |
| dimensionless | dimensionless | dimensionless |  |
| 3-4 | LITMIN | LITMIN is a positive integer less or equal to LITMAX that sets the minimum number of linear iterations within a Newton iteration. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 3-5 | MXWSIT | MXWSIT is a positive integer that defines the maximum number of iterations within a well flow calculation. | 8 |
| dimensionless | dimensionless | dimensionless |  |
| 3-6 | MXWPIT | MXWPIT is a positive integer that stipulates the maximum number of iterations for solving the bottom-hole pressure for wells under tubing head pressure control within a well flow calculation. | 8 |
| dimensionless | dimensionless | dimensionless |  |
| 3-7 | DDPLIM | DDPLIM is a positive real value that stipulates the maximum pressure change at the last Newton iteration. | 1.0 x 10^6^ |
| psia | barsa | atma |  |
| 3-8 | DDSLIM | DDSLIM is a positive real value that sets the maximum saturation change at the last Newton iteration. | 1.0 x 10^6^ |
| dimensionless | dimensionless | dimensionless |  |
| 3-9 | TRGDPR | TRGDPR is a positive real value that defines the target maximum pressure change within a time step. | 1.0 x 10^6^ |
| psia | barsa | atma |  |
| 3-10 | XXXDPR | XXXDPR is a positive real value that stipulates the maximum tolerable pressure change within a time step. | None |
| psia | barsa | atma |  |
| 3-11 | MNWRFP | MNWRFP is a positive integer greater than one and less than NEWTMX that defines the minimum number of Newton iterations before invoking the bisection algorithm for when the polymer phase is active in the model via the POLYMER keyword in the RUNSPEC section. | 4 |
| dimensionless | dimensionless | dimensionless |  |
| 3-12 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  The keyword consists of three records, with items 1-1 to 1-11 representing record one items, 2-1 to 2-14 record two and 3-1 to 3-12 representing record number three. Each of the records are terminated by a "/" and is explicitly shown in the above rows.<br>2)  There is no keyword terminating "/". |  |  |  |

Table 12.66: TUNING Keyword Description

Note that for record number two (items 2-1 to 2-13) the maximum values should always be greater than the associated target value; for example, XXXCNV should be greater than TRGCNV. Also note that the TUNING keyword is stored on the restart files (see [RPTRST -- Define Data to be Written to the RESTART File](#anchor-3)) enabling the parameters to be utilized in a restart run without re-specifying the keyword.

#### Example

\--

\-- DEFAULT TUNING PARAMETERS

\--

TUNING

1.0 365.0 0.1 0.15 3 0.3 0.1 1.25 1E20 1\* /

/

/

The above example explicitly sets the default parameters for OPM Flow for when the appropriate command line parameter has been activated (see section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line)) to instruct the simulator to read the first record of the TUNING keyword. Alternatively one could just use the following to accomplish the same thing.

TUNING

/

/

/
