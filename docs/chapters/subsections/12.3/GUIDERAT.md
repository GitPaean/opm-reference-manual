### GUIDERAT -- Define Group Guide Rate Formula

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines a general formulae used to define a group's and well's guide rate as a function of the their potential. The default behavior, that is when this keyword is not invoked, is to set the target control mode and rate via the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. In this case the target rate is distributed between the group's wells that are under group control using a well's guide rate. If a well's guide rate has not been defined, for example by this keyword, then the well potential of the group controlling phase at the beginning of the time step is used. For example, if the group target rate and phase is oil, then the well's under group control will have their oil rates determined by their oil rate potential[^1]. The [GUIDERAT](#__RefHeading___Toc193039_2026549522) keyword substitutes the potential calculation with a more general formulae in the aforementioned distribution and allocation of the rates:

Where:

*Potential*~Phase~ = the potential of the phase,

*A to F* = constants defined on this keyword,

*Potential Ratio*~*1*~ = the potential phase ratio as defined by this keyword,

*Potential Ratio*~*2*~ = the potential phase ratio as defined by this keyword.

The formulae can be used to control high water cut or high GOR wells in an oil field, such as the offending wells are given progressively smaller guide rates as they water out or gas out.

Note that groups can only have potential guide rates if they are subordinate in another group and required to produce a proportion of the superior group's target rate. In this case the [GUIDERAT](#__RefHeading___Toc193039_2026549522) keyword can optionally be applied by setting GUIPHASE variable on the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Group potentials are the sum of the potentials of their subordinate open wells.

| 1 | TSTEP | A real positive value that defines the minimum time interval to re-calculate the guide rates. The guide rates are calculated at the start of a time step and the default value of zero means that the guide rates are calculated for each time step.<br>A non-zero value for TSTEP resets the minimum interval, for example setting TSTEP equal to 30 would mean the guide rates are calculate every 30 days, or to the nearest associated time step.<br>Calculating guide rates every time step may cause issues due to the rate dependent behavior, for example gas cusping or water coning causing the well rates to oscillate. In this case using a non-zero value of TSTEP may eliminate this oscillating behavior. | 0.0 |
| --- | --- | --- | --- |
| days | days | hours |  |
| 2 | PHASE | A defined character string that sets the potential phase guide rate for the group and well, the resulting Phase Guide Rate in equation . PHASE should be set to one of the following character strings:<br>1)  [OIL](#__RefHeading___Toc97439_1778172979): is set as the potential phase guide rate and in this case the Potential Ratio1 variable is the water-oil ratio ("WOR") and Potential Ratio2 refers to the gas-oil ratio ("GOR") in equation .<br>2)  LIQ: is set as the potential phase guide rate and the Potential Ratio1 variable is the water cut ("WCT") and Potential Ratio2 refers to the gas-liquid ratio ("GLR") in equation .<br>3)  [GAS](#__RefHeading___Toc38607_2267116897): is set as the potential phase guide rate with the Potential Ratio1 variable being the water cut ("WCT") and Potential Ratio2 referring to the oil-gas ratio ("OGR") in equation .<br>4)  RES: here the potential phase guide rate is defined as the reservoir fluid volume rate and the Potential Ratio1 variable is the water-oil ratio ("WOR") and Potential Ratio2 refers to the gas-oil ratio ("GOR") in equation .<br>5)  COMB: this option uses the linearly combined phase guide rate based on the values entered on the [LINCOM](#__RefHeading___Toc287176_2843394514) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Here the *Potential Ratio*~*1*~ variable is the water divided by linearly combined phase and *Potential Ratio*~*2*~ refers to the gas divided by linearly combined phase in equation . This option is not available in OPM Flow.<br>6)  NONE: the Phase Guide Rate calculation is switched off and the well guide rates revert to the well potentials of their group target phase.<br>For reference, the units for the various options is given below . | None |
| WOR: dimensionless<br>WCT: dimensionless<br>WGR: stb/Mscf | dimensionless<br>dimensionless<br>dimensionless | dimensionless<br>dimensionless<br>dimensionless |  |
| GOR: Mscf/stb<br>GLR: Mscf/stb<br>OGR: stb/Mscf | dimensionless<br>dimensionless<br>dimensionless | dimensionless<br>dimensionless<br>dimensionless |  |
| 3 | A | A real value greater than or equal to -3 and less than or equal to 3, that defines coefficient A in equation . | 0.0 |
| 4 | B | B is a real positive value that defines coefficient B in equation . | 0.0 |
| 5 | C | C is a real value that defines coefficient C in equation . | 0.0 |
| 6 | D | D is a real value greater than or equal to -3 and less than or equal to 3, that defines coefficient D in equation . | 0.0 |
| 7 | E | E is a real value that defines coefficient E in equation . | 0.0 |
| 8 | F | F is a real value greater than or equal to -3 and less than or equal to 3, that defines coefficient F in equation . | 0.0 |
| 9 | GROPT01 | A defined character string that determines if calculated phase guide rates should be allowed to increase (YES) or not (NO), and should be set to one of the following:<br>1)  NO: The phase guide rates calculated from equation are not allowed to increase above the current value, and will be reset to the current value if the calculated value does exceed the current value.<br>2)  YES: The phase guide rates calculated from equation are allowed to increase at each calculation. This may increase the propensity for oscillations in the rates if the water cut and GOR are rate dependent.<br>Note only the default value is currently supported by OPM Flow. | YES |
| 10 | GROPT02 | A real positive value greater than or equal to zero and less than or equal to one that "dampens" the calculated phase guide rate based on the following formula:<br>The option is intended to have a similar effect as the GROPT01 NO option to reduce oscillations as a result of either the water cut or GOR being rate dependent.<br>Values approaching one allows the calculated phase guide rates to change instantaneously with the phase potentials, whereas values approaching zero dampen the potential guide rates towards the previously calculated values, thereby reducing the potential for oscillating behavior. | 1.0 |
| 11 | GROPT03 | A defined character string that determines if "free" gas potential rates for the Potential Ratio2 variable in equation should be used (YES), or if "free and associated" gas should be used (NO), and should be set to one of the following:<br>1)  NO: Use "free and associated" gas, that is total gas in the Potential Ratio2 variable.<br>2)  YES: Only utilize "free" gas in the Potential Ratio2 variable. | NO |
| 12 | GROPT04 | A real positive value that sets the minimum potential guide rate. If the calculated potential guide is below this value it will be reset to GROPT04.<br>The option is meant to avoid groups and wells being ignored due to the calculated potential guide rates being minuscule. | 1.0 x10-6 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 12.47: GUIDERAT Keyword Description*
Note that the [GUIDERAT](#__RefHeading___Toc193039_2026549522) keyword only applies to production groups and wells. Injection groups and wells are still controlled by their potential guide rates.

Finally, as mentioned previously, if the [GUIDERAT](#__RefHeading___Toc193039_2026549522) or [WGRUPCON](#__RefHeading___Toc121641_2412586160) keywords are not present in the input deck then the group and well potential guide rates will be calculated using the well's potential rates. The [WGRUPCON](#__RefHeading___Toc121641_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section can be used to set a constant potential guide rate for a well.

#### Examples

The first example sets the guide phase to oil and the resulting Phase Guide Rate based on oil potential based on setting the A and B coefficients to to one, that is:

with all the other parameters defaulted, except for the minimum time interval to re-calculate the guide rates which is set to 30 days.

\--

\-- SETS GUIDE RATES FOR GROUPS AND WELLS UNDER GUIDE RATE CONTROL

\--

\-- TIME GUIDE A B C D E F INCR DAMP FREE

\-- STEP PHASE POW CON CON POW CON POW OPTN OPTN GAS

GUIDERAT

30 \'OIL\' 1.0 1.0 1\* 1\* 1\* 1\* 1\* 1\* 1\* /

The next example sets the Phase Guide Rate to the reservoir fluid volume rate, with preference given to low GOR wells and with high GOR wells penalized, based on setting A and B to one, C and D to zero, E equal to 10 and F equal to two, that is:

with all the other parameters defaulted.

\--

\-- SETS GUIDE RATES FOR GROUPS AND WELLS UNDER GUIDE RATE CONTROL

\--

\-- TIME GUIDE A B C D E F INCR DAMP FREE

\-- STEP PHASE POW CON CON POW CON POW OPTN OPTN GAS

GUIDERAT

1\* \'RES\' 1.0 1.0 1\* 1\* 10 2 1\* 1\* 1\* /

The [GUIDERAT](#__RefHeading___Toc193039_2026549522) keyword is very flexible but can also lead to unexpected results, thus it is probably useful to perform some manual calculations outside of the simulator before implementing the selected scheme in the input deck.

[^1]: Production and injection potentials are based on rates that are unrestricted. For wells this implies that well potential is calculated based on either the BHP or THP limit, which ever is the more *constraining*.
