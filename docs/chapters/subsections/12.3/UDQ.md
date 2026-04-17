<a id="__RefHeading___Toc161095_2932703077"></a>

### UDQ -- Declare User Define Quantities ("UDQ")

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword starts the definition of a UDQ section that stipulates the variables and operations used to access the User Defined Quantities features in OPM Flow. UDQ variables can be constants, SUMMARY variables, as defined in the SUMMARY section, or a formula using various mathematical functions together with constants and SUMMARY variables. Available operations include the ASSIGN, DEFINE, UNITS and UPDATE commands that are sub-keywords to the UDQ section keyword.

User Defined Quantities can be output to the summmary file and used as User Defined Arguments ("UDA") in the SCHEDULE section with various group, well, and connection keywords.

Although this keyword is read by OPM Flow and the ACTION and UDQ computational logic and calculations have been implemented, one should use caution when using this facility as it may result in OPM Flow aborting.

| UDQ | Define the start of UDQ Definition Section. This is then followed on a new line by any number of UDQ records that define the various operations to be performed using the ASSIGN, DEFINE UNITS and UPDATE sub-keywords for the OPERATOR. |  |  |
| --- | --- | --- | --- |
| 1 | OPERATOR | OPERATOR is a defined character string that specifies the type of operation to perform, and should be one of the following:<br>1)  ASSIGN: Assigns a constant numerical value to the UDQ defined by VARIABLE and sets the UPDATE status to OFF.<br>2)  DEFINE: Defines a mathematical formula and assigns it to the UDQ defined by VARIABLE. The UDQ is initialized with the formula and the UPDATE status is set to ON.<br>3)  UNITS: Sets the reporting units for the UDQ defined by VARIABLE. The units have no effect on the calculations. The UDQ must already have been defined prior to using this option.<br>4)  UPDATE: Stipulates when the UDQ defined by VARIABLE should be evaluated. |  |
| 2 | VARIABLE | VARIABLE is a character string of length eight that stipulates the name of the user defined variable that will processed by the OPERATOR command. The first two characters of VARIABLE must be set based on the type of variable being defined, that is:<br>1)  CU: For variables that are associated with connections, for example SUMMARY variable COFR (Connection Oil Flow Rate).<br>2)  FU: For variables that are associated with field data, for example SUMMARY variable FOPR (Field Oil Production Rate).<br>3)  GU: For variables that are associated with groups, for example SUMMARY variable GLPR (Group Liquid Production Rate).<br>4)  RU: For variables that are associated with regions, for example SUMMARY variable RPR (Region Pressure).<br>5)  SU: For variables that are associated with multi-segment wells, for example SUMMARY variable SOFR (Segment Oil Flow Rate).<br>6)  WU: For variables that are associated with wells, for example SUMMARY variable WWCT (Well Water Cut).<br>7)  AU: For variables that are associated with aquifers, for example SUMMARY variable AAQP (Analytical Aquifer Pressure).<br>8)  BU: For variables that are associated with blocks, for example SUMMARY variable BPR (Block oil phase Pressure).<br>OPM Flow currently only supports field, group, segment and well variables (FU\*, GU\*, SU\* and WU\*). |  |
| 3 | EXPRESSION | The data type for EXPRESSION is based on the OPERATOR option above, namely if OPERATOR is set to:<br>1)  ASSIGN: EXPRESSION should be a numerical value.<br>2)  DEFINE: EXPRESSION should be a mathematical expression. Allowable tokens for the expression include SUMMARY or UDQ variables, real numbers (can be integers or scientific notation), opening and closing brackets \'(\' and \')\', and basic mathematical operators plus \'+\', minus \'-\', multiply \'\*\', divide \'/\' and exponent \'\^\'.<br>3)  UNITS: EXPRESSION should be a character string (enclosed in quotes if it contains blanks) with a maximum length of eight characters, that declares the units that will used when reporting the UDQ defined by VARIABLE.<br>4)  UPDATE: EXPRESSION should be a defined character string (ON, OFF or NEXT): ON to evaluate the UDQ defined by VARIABLE at all time steps, OFF to not evaluate the UDQ, or NEXT to evaluate the UDQ at the next time step. |  |
|  | / | Termination of a UDQ record. Note that multiple numbers of records can be entered within a UDQ section with each record terminated by a "/". |  |
| / | Define the end of UDQ Definition Section |  |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.71: UDQ Keyword Description

All the functions available for use in the DEFINE EXPRESSION in the commercial simulator are listed in below.

| ( |  |  | Open bracket. |
| --- | --- | --- | --- |
| ) |  |  | Close bracket. |
| \[ |  |  | Start of user defined table argument list. |
| \] |  |  | End of user defined table argument list. |
| , |  |  | Separator for multi-dimensional user defined table argument list. |
| \- | 6 | unary elemental | Negation of defined elements. |
| ABS() | 6 | unary elemental | Absolute value of defined elements. |
| AVEA() | 6 | unary scalar | Arithmetic average of defined elements. |
| AVEG() | 6 | unary scalar | Geometric average of defined elements. |
| AVEH() | 6 | unary scalar | Harmonic average of defined elements. |
| DEF() | 6 | unary elemental | Returns 1 if the element is defined, otherwise returns undefined. |
| EXP() | 6 | unary elemental | Exponential of defined elements. |
| IDV() | 6 | unary elemental | Returns 1 if the element is defined, otherwise returns 0. |
| LN() | 6 | unary elemental | Natural logarithm of defined elements. |
| LOG() | 6 | unary elemental | Logarithm base 10 of defined elements. |
| MAX() | 6 | unary scalar | Maximum of defined elements. |
| MIN() | 6 | unary scalar | Minimum of defined elements. |
| NORM1() | 6 | unary scalar | 1 norm of defined elements. |
| NORM2() | 6 | unary scalar | 2 norm of defined elements. |
| NORMI() | 6 | unary scalar | Infinity norm of defined elements. |
| NINT() | 6 | unary elemental | Nearest integer to defined elements. |
| PROD() | 6 | unary scalar | Product of defined elements. |
| RANDN() | 6 | unary elemental | Random sample from Normal distribution N(0,1), where the seed is specified by the UDQPARAM keyword Item 1. |
| RANDU() | 6 | unary elemental | Random sample from Uniform distribution U(-1,1), where the seed is specified by the UDQPARAM keyword Item 1. |
| RRNDN() | 6 | unary elemental | Random sample from Normal distribution N(0,1), where the seed is determined from the current time. By default restart simulations will use the seed from the base simulation (see UDQDIMS keyword Item 11). |
| RRNDU() | 6 | unary elemental | Random sample from Uniform distribution U(-1,1), where the seed is determined from the current time. By default restart simulations will use the seed from the base simulation (see UDQDIMS keyword Item 11). |
| SORTA() | 6 | unary elemental | Position of the element in an ascending sort of defined elements. |
| SORTD() | 6 | unary elemental | Position of the element in an descending sort of defined elements. |
| SUM() | 6 | unary scalar | Sum of defined elements. |
| UNDEF() | 6 | unary elemental | Returns 1 if element is undefined, otherwise returns undefined. |
| TU\*\[\] | 6 | unary elemental | Lookup value of the user defined table based on the arguments in the square brackets. All arguments must have the same type or be scalar. A scalar is returned if all the arguments are scalar, or the same type of UDQ set is returned as the UDQ set arguments. |
| \<= | 5 | binary intersection | Returns 1 if the LHS is less than or equal to the RHS, otherwise return 0. The tolerance for equality is specified by the UDQPARAM keyword Item 4. |
| \>= | 5 | binary intersection | Returns 1 if the LHS is greater than or equal to the RHS, otherwise return 0. The tolerance for equality is specified by the UDQPARAM keyword Item 4. |
| \< | 5 | binary intersection | Returns 1 if the LHS is less than the RHS, otherwise return 0. |
| \> | 5 | binary intersection | Returns 1 if the LHS is greater than the RHS, otherwise return 0. |
| == | 5 | binary intersection | Returns 1 if the LHS is equal to the RHS. The tolerance for equality is specified by the UDQPARAM keyword Item 4. |
| != | 5 | binary intersection | Returns 1 if the LHS is not equal to the RHS. The tolerance for equality is specified by the UDQPARAM keyword Item 4. |
| \^ | 4 | binary intersection | Exponentiation. |
| \* | 3 | binary intersection | Multiplication. |
| / | 3 | binary intersection | Division. |
| \+ | 2 | binary intersection | Addition. |
| \- | 2 | binary intersection | Subtraction. |
| UADD | 1 | binary union | Returns sum of intersecting elements from the union of two UDQ sets. |
| UMAX | 1 | binary union | Returns maximum of intersecting elements from the union of two UDQ sets. |
| UMIN | 1 | binary union | Returns minimum of intersecting elements from the union of two UDQ sets. |
| UMUL | 1 | binary union | Returns product of intersecting elements from the union of two UDQ sets. |
| Notes:<br>1)  Functions are evaluated in order of decreasing precedence. Binary functions of equal precedence are evaluated left to right. Unary functions of equal precedence are evaluated right to left.<br>2)  Binary functions operate on either the union or the intersection of two UDQ sets. For intersections the result is only defined if both corresponding elements are defined. For unions the result is defined if either of the corresponding elements are defined. Both arguments of a binary function either need to be of the same type or one needs to be scalar.<br>3)  Unary functions operate on a single argument and are either elemental or return a scalar value. |  |  |  |

Table 12.71: UDQ - Description of Functions

See also the UDADIMS, UDQDIMS and UDQPARAM keywords in the RUNSPEC section to define the dimensions for the UDQ keyword and associated variables.

User Defined Quantities can also be used as User Defined Arguments ("UDA") in the SCHEDULE section with various group, well, and connection keywords. In this case, the UDA variables are used to replace numerical values on these keywords by UDA variables that have been defined by the UDQ keyword. For example, if we wish to make the oil rate for certain wells be a function of their water cut, then one can define the function using the UDQ keyword that results in a UDQ variable, WU_WCUT say, and then use WU_WCUT as a UDA variable on the WCONPROD keyword for the ORAT parameter. lists the keywords that can be used with UDA variables.

| 1 | GCONINJE | WALKALIN | WINJEDET | CECON | LINCOM |
| --- | --- | --- | --- | --- | --- |
| 2 | GCONPRI | WAPI | WINJFCNC | CPIFACT |  |
| 3 | GCONPROD | WCONHIST | WINJTEMP | CPIFACTL |  |
| 4 | GCONSALE | WCONINJE | WPOLYMER |  |  |
| 5 | GCONSUMP | WCONPROD | WSALT |  |  |
| 6 | GECON | WECON | WSOLVENT |  |  |
| 7 | GRUPFUEL | WECONCMF | WSURFACT |  |  |
| 8 | GRUPSALE | WELDRAW | WTADD |  |  |
| 9 | GSATPROD | WELLSTRE | WTMULT |  |  |
| 10 | GTADD | WELTARG | WTRACER |  |  |
| 11 | GTMULT | WFOAM |  |  |  |
|  |  | Multi-Segment Well Keywords |  |  |  |
| 1 |  | WSEGTABL | WSEGVALV |  |  |
| Notes:<br>3)  Cells not colored show that the keyword has been tested and is functional within an ACTIONX block using a User Defined Argument.<br>4)  Cells colored in gray indicate that the keyword has not been tested in OPM Flow.<br>5)  Cells colored orange show keywords currently unavailable in OPM Flow because the underlying feature is not available; either because the keyword is a compositional keyword in the commercial simulator, or the keyword has not been implemented in OPM Flow. |  |  |  |  |  |

<a id="REF_TABLE_ACTIONX_USER_DEF__KEYWORDS_12_3"></a>Table 12.72: UDQ - User Defined Argument Supported Keywords

#### Examples

The first example shows how to define some constant field variables used for calculating facilities corrected condensate and Liquefied Petroleum Gas[^1] ("LPG ") yields in a wet gas model:

\--

\-- DEFINE START OF USER DEFINED QUANTITY SECTION

\--

UDQ

\--

\-- OPERATOR VARIABLE EXPRESSION

\--

ASSIGN FUNGLYLD 1.100000 / \-- Condensate Yield (stb/Mscf)

ASSIGN FUNGLSHK 0.000000 / Condensate Shrinkage Factor to Zero

ASSIGN FULPGYLD 0.065775 / \-- LPG Sep Gas Yield (stb/Mscf)

ASSIGN FULPGSHK 0.080410 / LPG Shrinkage Factor

ASSIGN FUFACSHK 0.000935 / Facilities Shrinkage Factor

ASSIGN FUFULSHK 0.052924 / Fuel Utilization

ASSIGN FUDELTA 1E-10 / Value to avoid dividing by zero errors

/ DEFINE END OF USER DEFINED QUANTITY SECTION

The next example is a continuation of this example by showing how one can calculate the adjusted field condensate and LPG rates. Note both examples could be merged into a single UDQ definition but have been stated separately for ease of reference.

\--

\-- DEFINE START OF USER DEFINED QUANTITY SECTION

\--

UDQ

\--

\-- OPERATOR VARIABLE EXPRESSION

\--

DEFINE FU_FNGLR FGPR \* (FOGR \* FUNGLYLD) / Calculate Condensate Rate Field

UPDATE FU_FNGLR ON /

UNITS FU_FNGLR STBD /

DEFINE FU_FLPGR FU_FWGPR \* FULPGYLD / Calculate LPG Rate Field

UPDATE FU_FLPGR ON /

UNITS FU_FLPGR STBD /

/ DEFINE END OF USER DEFINED QUANTITY SECTION

In the above the DEFINE operator is use to define the equations to calculate the corrected condensate (FU_FNGLR) and LPG rates (FU_FLPGR) with the UPDATE operator set to ON so that the rates are calculate at every time step, and finally, the UNITS operator is used to set the units of the calculated rates.

The final example show the use of the UDADIMS and UDQDIMS keywords in the RUNSPEC section, followed by the keywords in the SCHEDULE section that define a UDQ definition that uses the DEFINE operator to calculate adjusted well rates based on an expression. The final set of keywords show how the UDQ defined variables are employed on the WCONPROD keyword to control the production constraints for several wells.

RUNSPEC SECTION KEYWORDS

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- USER DEFINED ARGUMENT DIMENSIONS

\-- NO. NOT TOTAL

\-- ARGS USED UDQ

UDADIMS

10 1\* 10 /

\--

\-- USER DEFINED ARGUMENT DIMENSIONS FACILITY

\-- MAX MAX MAX MAX MAX MAX MAX MAX MAX MAX RAND

\-- FUNCS ITEMS CONNS FIELD GROUP REGS SEGTM WELL AQUF BLCKS OPT

UDQDIMS

50 25 0 50 50 0 0 0 0 0 N /

And the SCHEDULE section part of the example is shown below.

SCHEDULE SECTION KEYWORDS

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- DEFINE START OF USER DEFINED QUANTITY SECTION

\--

UDQ

\--

\-- OPERATOR VARIABLE EXPRESSION

\--

DEFINE WUOPRL (WOPR OPL01 - 150) \* 0.90 / OIL & LIQ CAPACITIES

DEFINE WULPRL (WLPR OPL01 - 200) \* 0.90 / at GEFAC = 0.8995

DEFINE WUOPRU (WOPR OPU01 - 250) \* 0.80 /

DEFINE WULPRU (WLPR OPU01 - 300) \* 0.80 /

\--

UNITS WUOPRL SM3/DAY / DEFINE REPORTING UNITS

UNITS WULPRL SM3/DAY / FOR UDQ VARIABLES

UNITS WUOPRU SM3/DAY /

UNITS WULPRU SM3/DAY /

/ DEFINE END OF USER DEFINED QUANTITY SECTION

\--

\-- WELL PRODUCTION WELL CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS LIQ RES BHP THP VFP VFP

\-- NAME SHUT MODE RATE RATE RATE RATE RATE PRES PRES TABLE ALFQ

WCONPROD

OP01 SHUT GRUP 1\* 1\* 1\* 1\* 1\* 200.0 /

OP02 SHUT GRUP 1\* 1\* 1\* 1\* 1\* 200.0 /

/

DATES

1 FEB 2020 /

\--

\-- WELL PRODUCTION WELL CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS LIQ RES BHP THP VFP VFP

\-- NAME SHUT MODE RATE RATE RATE RATE RATE PRES PRES TABLE ALFQ

WCONPROD

OP01 OPEN GRUP WUOPRL 1\* 1\* WULPRL 1\* 60.0 /

OP02 OPEN GRUP WUOPRL 1\* 1\* WULPRL 1\* 00.0 /

/

DATES

1 MAR 2020 /

1 APR 2020 /

1 MAY 2020 /

1 JUN 2020 /

1 JLY 2020 /

1 AUG 2020 /

1 SEP 2020 /

/

[^1]: Liquefied Petroleum Gas or LPG consists mainly of propane, propylene, butane, and butylene in various mixtures. It is produced as a by-product of natural gas processing and petroleum refining. The components of LPG are gases at standard conditions.
