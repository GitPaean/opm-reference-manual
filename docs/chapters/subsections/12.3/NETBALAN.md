### NETBALAN -- Network Balancing Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[NETBALAN](#__RefHeading___Toc117627_2179381650) keyword causes the simulator to perform a network balancing operation at the next time step. In addition, the keyword defines the network balancing parameters used to control how network balancing is performed on a network, as well as the frequency of the network balancing calculations. If any of the parameters on the keyword are defaulted, then either the previously entered values are used, or if there are no previously entered values, then the keyword default values are employed.

| 1 | NTSTEP | NSTEP is a real value that defines the criteria for the network balancing interval, used to define the frequency of the network balancing algorithm. NSTEP may be a negative number, a value of zero, or a positive number, as described below:<br>1)  Negative Value: If NSTEP is any negative value then the time stepping interval for the network balancing is based on the number of Newton iterations used in updating the well targets, as set by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or the NUPCOL parameter on the [GCONTOL](#__RefHeading___Toc202994_156692946) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. If [NUPCOL](#__RefHeading___Toc86969_4106839650) is defined on both keywords, then the [GCONTOL](#__RefHeading___Toc202994_156692946) value takes precedence.<br>2)  Thus, any negative value of NSTEP means the network will be balanced for the first [NUPCOL](#__RefHeading___Toc86969_4106839650) Newton iterations for each time step.<br>3)  Consequently, if this option is used it may result in some oscillations as the THP of the wells are updated at each Newton network re-balance computation.<br>4)  Zero Value: Here the network is balanced at the beginning of every time step, and should result in small network balancing errors for the time step, provided of course the reservoir conditions are fairly constant over the time step. This is the default value.<br>5)  Positive Value: In this case NSTEP is a time interval between the previous network balance and the next schedule network balancing. For example, if NSTEP is set equal to 91.25 days (365/4), then network balancing will occur every quarter. Again, the balancing occurs at the beginning of the time step.<br>Note only negative or zero values are currently supported. | 0.0 |
| --- | --- | --- | --- |
| days or<br>dimensionless | days or<br>dimensionless | hours or<br>dimensionless |  |
| 2 | NCNV | NCNV is a real positive value that defines the nodal pressure convergence variance, used to define if convergence has been satisfied. | Defined |
| psia<br>1.45 | barsa<br>0.10 | atma<br>0.09869 |  |
| 3 | NMXITER | A positive integer value that defines the maximum number of network balancing operations that may be performed during a network balancing computation. | 10 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | GRPCNV | GRPCNV is a real positive value less than one that sets the group tolerance criteria used to define if convergence has been satisfied for:<br>1)  Wells in subsea completion manifold groups under rate control. In this case GRPCNV is applied to the THP values of the wells within the group. In the field, these type of wells must flow against a common manifold pressure, that is all the wells must flow at approximately the same THP, for a given group's flow rate.<br>2)  Automatic chokes for group's under rate control. Here, GRPCNV is applied to the pressure drop across the automatic chokes.<br>In both cases GRPCNV is an acceptable fraction of the group's rate target. Thus, the default value 0.01 means that network balance calculated rate must be within 0.01 (or 1.0%) of the groups' production target.<br>Note that this criteria may not be satisfied if the number of Newton iterations used in updating the well targets, as set by the [NUPCOL](#__RefHeading___Toc86969_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or the NUPCOL parameter on the [GCONTOL](#__RefHeading___Toc202994_156692946) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, is exceeded.<br>Group convergence criteria can also be set by the GRPCNV parameter on the [GCONTOL](#__RefHeading___Toc202994_156692946) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. If both values of GRPCNV have been entered, then the minimum of the two is used. | 0.01 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | THPMXITE | A positive integer value that defines the maximum number of well THP iterations for wells in subsea completion.anifold groups under rate control.<br>There is no equivalent iteration maximum for automatic chokes in groups under rate control, as the pressure drop across the chokes is automatically calculated in the network balancing calculation. Thus, NMXITER is used for these calculations. | 10 |
| dimensionless | dimensionless | dimensionless |  |
| 6 | NTRGERR | A real positive value that stipulates the maximum target branch error in a network balance calculation, at the end of the time step.<br>NTRGERR is compared with the branch error (Error), where Error is the difference between the pressure drop along the branch from the previous network balance and the current calculation, again, at the end of the time step.<br>Subject to existing targets and constraints, the simulator will attempt to adjust the time step size in order to roughly match NTRGERR. Note also that NTRGERR should be a value that is sufficient to allow convergence as defined by NCNV and GRPNCN parameters.<br>The default value of 1.0 x 1020 means that this parameter has no effect in the selection of the time step size. | 1.0 x 1020 |
| psia | barsa | atma |  |
| 7 | NMAXERR | A real positive value that stipulates the maximum branch error in a network balance calculation, at the end of the time step.<br>Again, NMAXERR is compared against the branch error (Error), where Error is the difference between the pressure drop along the branch from the previous network balance and the current calculation, at the end of the time step.<br>If Error is greater than NMAXERR then the simulator will enforce a time step chop. Time step chops are computationally expensive and should therefore be minimized. Hence, care should be used in setting this value, which should be significantly greater than NTRGERR.<br>The default value of 1.0 x 1020 means that this parameter has no effect in the selection of the time step size. | 1.0 x 1020 |
| psia | barsa | atma |  |
| 8 | NTSMIN | NTSMIN is a real positive value that sets the minimum time step size for when NTRGERR and NMAXERR have values.<br>Large network balancing errors (Error) can take place for various reasons, a common occurrence is for wells producing near their operating limit which may shut in during a network balance operation. If NTRGERR and NMAXERR have values, then this will result in the simulator enforcing time step chops to perhaps very small time steps. NTSMIN can therefore be used to set the minimum time step size under, and only, these circumstances.<br>The default value, TSMINZ, is taken from TSMINZ parameter on the [TUNING](#__RefHeading___Toc146744_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. | TSMINZ |
| days | days | hour |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 12.53: NETBALAN Keyword Description*
#### Examples

The first example sets network balancing to occur at the beginning of each time step using a 1.0 psia convergence criteria, and a maximum of 10 iterations. All the other parameters are defaulted.

\--

\-- NETWORK BALANCE CONTROL OPTIONS

\--

\-- BAL CONV MAX WTHP WTHP ERR ERR TSTEP

\-- INTV TOL ITRS TOL ITS TARG MAX MIN

NETBALAN

0.0 1.0 10 1\* 1\* 1\* 1\* 1\* /

The next example sets network balancing to occur for the first [NUPCOL](#__RefHeading___Toc86969_4106839650) Newton iterations for each time step. All the other parameters are defaulted.

\--

\-- NETWORK BALANCE CONTROL OPTIONS

\--

\-- BAL CONV MAX WTHP WTHP ERR ERR TSTEP

\-- INTV TOL ITRS TOL ITS TARG MAX MIN

NETBALAN

-1 1\* 1\* 1\* 1\* 1\* 1\* 1\* /
