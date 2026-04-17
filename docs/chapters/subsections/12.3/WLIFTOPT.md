### WLIFTOPT -- Define Well Gas Lift Optimization Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WLIFTOPT defines which wells should use the Gas Lift Optimization facility in order to maximize oil production, as well as defining the associated gas lift optimization parameters for a given well. The keyword can also be used to switch off gas lift optimization for a well. Gas lift optimization is invoked via the LIFTOPT keyword in the SCHEDULE section. Note that the LIFTOPT keyword should precede the WLIFTOPT keyword in the SCHEDULE section in order to activate the gas lift optimization facility.

Wells are allocated to groups when the wells are specified by the WELSPECS keyword in the SCHEDULE section. Wells defined to be under group control will have their production rates and gas lift gas constraints (GLIFTOPT keyword in the SCHEDULE section) controlled by the group to which they belong, in addition to any well constraints defined for the wells, including the gas optimization parameters on the WLIFTOPT keyword.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well gas lift optimization parameters are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | OPTLIFT | A defined character string that sets if a well's gas lift gas rate should be calculated by the gas lift optimization facility or not, and should be set to:<br>1)  NO: In this case the gas lift gas is a constant determined from the MXLIFT variable on this keyword, the ALQ-WELL variable on the WCONPROD keyword, or the TARGET and VALUE variables on the WELTARG keyword.<br>2)  YES: Activates the gas lift optimization for the given well. | None |
| 3 | MXLIFT | A real value that defines the total amount of gas lift gas available for this well, multiplied by the well's efficiency factor.<br>1)  If OPTLIFT is defined as NO then MXLIFT is considered a fixed gas lift gas rate. However, if MXLIFT is defaulted (1\*) then MXLIFT is unchanged from the previously entered value.<br>2)  If OPTLIFT equals YES and MXLIFT is defaulted (1\*), then MXLIFT is taken from the largest value of the ALQ variable on the well's associated VFPPROD table.<br>Note that the value entered here should be in the range entered in the VFPPROD table allocated to the well, otherwise errors may occur when optimizing the gas lift gas injection rate for the well. | 1\* |
| Mscf/d | sm^3^/day | scc/hour |  |
| 4 | OPTWGT | OPTWGT (βw) is real positive value that defines a weighting factor for allocating the available gas lift gas to a well. An increment of gas lift gas supply is allocated to a well based on the well's current incremental gradient multiplied by OPTWGT using the following formulae:<br>Where:<br>βw = is OPTWGT, the weighting factor for the preferential<br>allocation of lift gas,<br>βg = is the gas production rate weighting factor,<br>∆QOil = is the increment/decrement in oil production rate,<br>∆Q~gas\ \ \ \ \ \ ~= is the increment/decrement in gas production rate, and<br>∆Q~GasLift~ = is the increment/decrement in gas lift gas rate.<br>Note by default βg, the gas production rate weighting factor, is set to zero,<br>and therefore the gradient equation simplifies to:<br>OPTWGT is ignored if OPTLIFT is equal to NO. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | MINGAS | A real value that defines the minimum amount of gas lift gas available to the well, multiplied by the well's efficiency factor. The allocation of the gas lift gas is determined by:<br>1)  If MINGAS is a positive value then this value is allocated to the well unless the well is unable flow with this quantity of gas lift gas. Alternatively, if the well is able to meet it's target rate without applying MINGAS, then the MINGAS rate is *not applied* to the well.<br>2)  If MINGAS is a negative value, then the well is supplied with sufficient gas lift gas to allow the well to flow, subject to the maximum allowed gas lift quantity, as per MXLIFT variable on this keyword. The negative value itself is not used in any calculations.<br>3)  If there is insufficient available gas lift gas, the wells are assigned values of MINGAS based on the decreasing order of their weighting factors as calculated per OPTWGT variable.<br>4)  Wells belonging to groups that can meet their production targets without gas lift, will have their MINGAS values not applied, that is no gas lift is applied. The exception is that if OPTWGT has been set to a value greater than or equal to one, then the well will use the MINGAS value for it's gas lift gas, even if the group's target can be satisfied without gas lift. However, if both the well's group and the well can meet their production targets, then MINGAS will not be applied.<br>This parameter is ignored if OPTLIFT is defined as NO. | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 6 | OPTGAS | OPTGAS (βg) is real positive value that defines the incremental gas weighting factor for allocating the available gas lift gas to a well. An increment of gas lift gas supply is allocated to a well based on the well's current incremental gradient as described by the definition of the OPTWGT (βg) variable above, that is by the following formulae:<br>See OPTWGT for a definition of the variables in the equation.<br>This parameter is ignored if OPTLIFT is defined as NO. | 0.0 |
| dimensionless1 | dimensionless | dimensionless |  |
| 7 | OPTLIMIT | A defined character string that defines if additional gas lift gas should be applied to the well, if the well's group gas target has been satisfied but the group's oil rate limit has not been achieved.<br>1)  NO: Additional gas lift gas is not available for the given well.<br>2)  YES: Additional gas lift gas is available for the given well. In cases where a well receiving additional gas lift may cause the well's group to exceed the group's gas target, normally the well will not be assigned the additional gas lift gas. However, if OPTLIMIT is set to YES, then this constraint is removed. This results in the gas lift optimization procedure continuing to maximize the oil rate, subject to available constraints. However, upon completion of the optimization process, applying the group controls may negate the gain from the gas lift optimization process.<br>This parameter is ignored if OPTLIFT is defined as NO. | NO |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.103: WLIFTOPT Keyword Description

See also the LIFTOPT keyword to activate gas lift optimization, the GLIFTOPT keyword to define the group gas lift optimization controls, GRUPTREE keyword to define the hierarchy of the groups below the FIELD level, the WCONPROD and WCONINJE keywords to define a well's production and injection rate targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example first switches on gas lift optimization via the LIFTOPT keyword and then defines the artificial lift constraints for PLAT-A, using the GLIFTOPT keyword and sets the well gas lift parameters using the WLIFTOPT keyword.

\-- ACTIVATE GAS LIFT OPTIMIZATION AND PARAMETERS

\--

\-- INCR INCR TSTEP NEWTON

\-- GAS OIL INTVAL OPTN

LIFTOPT

12.5E3 5E-3 0.0 YES /

/

\--

\-- GROUP GAS LIFT OPTIMIZATION CONSTRAINTS

\--

\-- GRUP MAX MAX

\-- NAME GAS ALQ TOTAL GAS

GLIFTOPT

PLAT-A 200E3 1\* /

/

\--

\-- WELL GAS LIFT OPTIMIZATION PARAMETERS

\--

\-- WELL OPTN MAX WEIGHT MIN GAS OPTN

\-- NAME LIFT LIFT FACTOR LIFT FACTOR LIMIT

WLIFTOPT

OP01 YES 150E3 1.01 -1.0 /

OP02 YES 150E3 1.01 -1.0 /

OPO3 YES 150E3 1.01 -1.0 /

OP04 YES 150E3 1.01 -1.0 /

OP05 YES 150E3 1.01 -1.0 /

/

Here the LIFTOPT keyword defines the maximum incremental gas lift gas quantity to be 12.5 x 103 m3, the minimum incremental oil gain per m3 of gas lift gas is set to 5.0 x 10-3 m3, the time step interval is set to zero to perform the gas optimization every time step, and finally the gas lift optimization will be performed NUPCOL Newton iterations for the time step.

The GLIFTOPT keyword sets the maximum amount of gas lift gas for PLAT-A to 200,000 m3 and there is no maximum limit for the total maximum amount of gas that the group can process. In addition, WLIFTOPT sets all five wells to have gas lift gas optimization implemented with a maximum gas lift gas value of 150,000 m3 per well, with equal weighting factors and all wells are supplied with sufficient gas lift gas to allow the wells to flow, (minimum lift set to a negative value) subject to the maximum allowed gas lift quantity for the well (150,000 m3).
