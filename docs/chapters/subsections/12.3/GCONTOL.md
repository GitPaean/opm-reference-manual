### GCONTOL -- Define Group Constraint Tolerance

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GCONTOL](#__RefHeading___Toc202994_156692946) keyword defines the tolerance and parameters used to control the accuracy of group targets and constraints, including the field's targets and constraints. The keyword sets the tolerance and number of Newton iterations for each time step so that the wells under group control can match the desired group targets and constraints.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPCNV | GRPCNV is a real positive value less than one that sets the group tolerance criteria used to define if convergence has been satisfied for group's under rate control. Here, GRPCNV is an acceptable fraction of the group's rate target. Thus, the a numerical quantity 0.01 means that values must be with 0.01 (or 1.0%) of the groups' production target.<br>For groups under priority control, as per [GCONPRI](#__RefHeading___Toc659214_1190369742) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, GRPCNV is ignored.<br>Note that this criteria may not be satisfied if the number of Newton iterations used in updating the well targets, as set by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or the [NUPCOL](#__RefHeading___Toc86969_4106839650) parameter on this keyword, is exceeded. In this case, and only if the well potentials allow, the well rates are re-calculated ignoring the [NUPCOL](#__RefHeading___Toc86969_4106839650) limit.<br>Group tolerance criteria can also be set by the GRPCNV parameter on the [NETBALAN](#__RefHeading___Toc117627_2179381650) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. If both values of GRPCNV have been entered, then the minimum of the two is used.<br>The default value means there is no convergence criteria. | 1.0 x 1020 |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| 2 | [NUPCOL](#__RefHeading___Toc86969_4106839650) | A positive integer that defines the maximum number of Newton iterations used to update well targets within a time step.<br>Wells under group control may suffer from some dependency with other wells in the same group that are under group control. This may cause some oscillation in the production and injection well rates within the group. In order to avoid this, after the number Newton iterations within a time step surpasses [NUPCOL](#__RefHeading___Toc86969_4106839650), the group well rates are frozen until the time step has converged. Reducing the potential of well rate oscillations within the time step may result in the group targets and limits not being exactly being met in this case. Increasing the value of [NUPCOL](#__RefHeading___Toc86969_4106839650) will improve the accuracy of the group targets and limits at the expense of computational efficiency.<br>NUPCOL can also be set by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. A value entered on this keyword overwrites any previously entered values of [NUPCOL](#__RefHeading___Toc86969_4106839650), including the value set by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword.<br>The default value of 1\* invokes the last previously entered value of either by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword or this keyword. | 1\* |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GASCNV | In the commercial compositional simulator GASCNV is a real positive value less than one that sets the tolerance criteria used to define if convergence has been satisfied for well gas injection rates. GASCNV is also used in conjunction with well availability gas fraction quantities in the commercial compositional simulator<br>The value is ignored by OPM Flow. | 1.0 x 10-3 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | GASMXITE | In the commercial compositional simulator GASMXITE is a positive integer value that defines the maximum number of iterations for the gas injection computation.<br>The value is ignored by OPM Flow. | 5 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 12.34: GCONTOL Keyword Description*
See also the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and the [NETBALAN](#__RefHeading___Toc117627_2179381650) and [WLIMTOL](#__RefHeading___Toc123805_332691817) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that control the network balancing convergence criteria and the tolerance parameters for wells, respectively.

#### Examples

The example sets the group target convergence criteria to 1% (0.01) with a maximum of four Newton iterations ([NUPCOL](#__RefHeading___Toc86969_4106839650)).

\--

\-- GROUP CONSTRAINT TOLERANCE

\--

\-- GROUP NEWTON INJEC NEWTON

\-- TOL ITERS TOL ITERS

\-- \-\-\-\-- \-\-\-\-- \-\-\-\-- \-\-\-\-\--

GCONTOL

0.01 4 1\* 1\* /
