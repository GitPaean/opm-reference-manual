### LIFTOPT -- Activate Gas Lift Optimization

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LIFTOPT keyword actives the gas lift optimization option and defines the gas lift gas increment size, the minimum incremental oil improvement, as well as the timing of the calculations. Note that the LIFTOPT keyword should precede any GLIFTOPT and WLIFTOPT keywords in the SCHEDULE section in order to activate the gas lift optimization facility.

| 1 | GASLIFT | A real positive number that defines the gas lift gas size increment that is used to increase the gas lift size quantity in steps. For example, if GASLIFT is set to 0.5 MMscf/d then gas lift gas will be allocated in step of 0.5 MMscf/d to each well during the optimization process.<br>A zero or negative value switches off gas lift optimization. | None |
| --- | --- | --- | --- |
| Mscf/d | sm^3^/day | scc/hour |  |
| 2 | MINOIL | MINOIL is a real positive value that defines the minimum increase in oil rate for a given quantity of gas lift gas, for when gas lift gas should be applied to a well. Additional GASLIFT will only be assigned to a well if:<br>Where ΔQ~Oil\ ~is the incremental oil and OPTWGT is the well's weighting factor defined by the OPTWGT variable on the WLIFTOPT keyword in the SCHEDULE section. | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| 3 | TSTEP | TSTEP is a real positive value that defines the frequency of the gas lift optimization calculations, for example setting TSTEP equal to 30 days would result in the gas lift optimization calculation being performed approximately every 30 days.<br>The default value of zero will result in the calculations being performed every time step.<br>Note if the group or well is part of a production network then gas lift optimization is performed at the same time as the network is being balance, that is this parameter is ignored in this scenario. See the NETBALAN keyword in the SCHEDULE section to set the network balancing frequency in this case. | 0.0 |
| days | days | hours |  |
| 4 | OPTLIFT | A defined character string that determines if the gas lift optimization iterations should be performed for the same number of Newton iterations within a time step as used to update well targets, or to just use the first Newton iteration only.<br>The NUPCOL keyword in the RUNSPEC section determines the number of Newton iterations used to update well targets during a time step.<br>OPTLIFT should be set to one of the following:<br>1)  NO: In this case the gas lift optimization is only performed for the first Newton iteration for a time step and the distributed gas lift gas is then held constant for the groups and wells through resultant Newton iterations during the time step. This leads to better numerical performance, but may lead to the targets and constraints not being exactly satisfied if the reservoir conditions change during the time step calculations.<br>2)  YES: Sets the number gas lift optimization iterations to the same number of Newton iterations within a time step as used to update well targets, as per the NUPCOL keyword in the RUNSPEC section. This results in greater target and constraint accuracy even if the reservoir conditions change during the time step calculations, but at the expense of numerical performance. Similar to the NO option, after the NUPCOL Newton iteration during the time step, the distributed gas lift gas is then held constant for the groups and wells in subsequent Newton iterations. |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.52: LIFTOPT Keyword Description

See also the GLIFTOPT keyword to define the group gas lift optimization controls and the WLIFTOPT keyword to define the wells under gas lift optimization control, both keywords are described in the SCHEDULE section. The NUPCOL keyword in the RUNSPEC section that determines the number of Newton iterations used to update well targets and gas lift optimization calculations during a time step may also be of interest.

#### Example

The following example activates gas lift optimization for the field and defines the optimization parameters.

\--

\-- ACTIVATE GAS LIFT OPTIMIZATION AND PARAMETERS

\--

\-- INCR INCR TSTEP NEWTON

\-- GAS OIL INTVAL OPTN

LIFTOPT

12.5E3 5E-3 0.0 YES /

Here the maximum incremental gas lift gas quantity is set to 12.5 x 103 m3, the minimum incremental oil gain per m3 of gas lift gas is set to 5.0 x 10-3 m3, the time step interval is set to zero to perform the gas optimization every time step, and finally the gas lift optimization will be performed NUPCOL Newton iterations for the time step.
