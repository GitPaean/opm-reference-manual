### ACTIONX -- Define Action Conditions and Command Processing

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ACTIONX keyword defines a series of conditions that invoke run time processing of ACTION functions and is similar to executing a run time script. This is the general purpose version of the ACTION series of keywords that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. The ACTION, ACTIONG, ACTIONR, ACTIONS and ACTIONW keywords are not implemented in OPM Flow and are unlikely to be so, as the ACTIONX keyword implements their functionality with greater flexibility.

This keyword starts the definition of an ACTIONX section that stipulates the Boolean conditions to test and the resulting SCHEDULE keywords to be executed if the Boolean condition evaluates to true. An ACTIONX Definition Section is terminated by an ENDACTIO keyword on a separate single line.

Although this keyword is read by OPM Flow and the ACTION and UDQ computational logic and calculations have been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the ACTIONX keyword enables the user to implement complex functionality and therefore it is advisable to start with simple expressions before adding the desired complexity.

See also the PYACTION keyword in the SCHEDULE section that implements OPM Flow's Python scripting facility using the standard Python scripting language.

| ACTIONX | Define the start of ACTIONX Definition Section. This is then followed on a new line by any number of ACTIONX records that define the conditions for which the defined action will be executed and the various operations to be performed if the conditions are satisfied. |  |  |
| --- | --- | --- | --- |
| 1-1 | ACTNAME | ACTNAME is a character sting of up to eight characters in length, that defines the name of this action definition.<br>If ACTNAME has previously been used by any ACTION series keyword, then the previous ACTION series definition will be replaced by the definition declared by this ACTIONX Definition Section. |  |
| 1-2 | ACTNSTEP | ACTNSTEP is a positive integer that defines the number times that the ACTNAME definition is executed. ACTIONX definitions are activated at the end of a time step and this parameter is used to set how many time steps the ACTNAME definition will be invoked. The default value of one means that the definition will be executed only once. Use a large value, for example 10,000 for the definition to be executed at every time step.<br>Note that the counter only affects successful evaluations; i.e. if ACTNSTEP is set equal to one (the default), then the simulator will test the action at the end of every time step until it evaluates to true. | 1 |
| 1-3 | ACTDELTA | ACTDELTA is a real positive value that defines the minimum duration of time after the conditions defined on the second record have been satisfied before the ACTIONX actions are executed. For example, if ACTDELTA is defaulted the actions will be executed at the end of the time step for which the conditions are met. If set to say 30, then a minimum of 30 days will pass before the actions are executed (assuming field or metric units). | 0.0 |
| days | days | hours |  |
| 1-4 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | ACTLHS | ACTLHS is a series of character strings, each up to eight characters in length, that defines a constant, UDQ defined value, or a SUMMARY variable on the left hand side of a Boolean conditional test.<br>The format for ACTLHS is dependent on the SUMMARY variable type: Aquifer, Block, Field, Group, Region, Time, Well, Well Connection, Well Local Grid Refinement Connection, or a Well Segment. In addition to SUMMARY variables, an UDQ defined value or a Constant variable can be used. The format for the various data types is given in . | Not Applicable |
| 2-2 | ACTTEST | ACTTEST is a defined character string that states the Boolean operator and must be set to one of the following Boolean conditionals:<br>1)  \>: Greater than.<br>2)  \<: Less than.<br>3)  \>=: Greater than or equal to.<br>4)  \<=: Less than or equal to.<br>5)  =: Equal to.<br>6)  !=: Not equal to.<br>For example to test if the field's gas production rate is less than 600 MMscf/d then one would use:<br>ACTIONX<br>PHASE2 1 /<br>GGPR \'FIELD\' \< 600E3 /<br>/<br>\...<br>ENDACTIO | Not Applicable |
| 2-3 | ACTRHS | ACTRHS is a numeric value or a series of character strings, each up to eight characters in length, that defines a constant, an UDQ defined value, or a SUMMARY variable on the right hand side of a Boolean conditional test, as outlined in (see also ACTLHS).<br>In the case of well quantities the set of matching wells is captured and can be used as a general \"well list\" with the symbol \'?\' in subsequent well keywords. For example, to shut-in all oil producing wells ('OP\*') with a water cut greater than 90% for every time the field water production rate exceeds 60,000 stb/d one would use:<br>ACTIONX<br>MXWATER 10000 /<br>GWPR \'FIELD\' \> 60E3 AND /<br>WWCT \'OP\*\' \> 0.90 /<br>/<br>\-- WELL PRODUCTION STATUS<br>\--<br>\-- WELL WELL \--LOCATION\-- COMPLETION<br>\-- NAME STAT I J K FIRST LAST<br>WELOPEN<br>\'?\' SHUT /<br>/<br>ENDACTIO | Not Applicable |
| 2-4 | ANDOR | An optional defined character string that specifies a Boolean operator that must be set to either AND or OR if included on this record, that links this record with additional records of this type. For example, to test if the field's gas production rate is less than 600 MMscf/d after 2020 then one would use:<br>ACTIONX<br>PHASE2 1 /<br>GGPR \'FIELD\' \< 600E3 AND /<br>YEAR \> 2020 /<br>/<br>\...<br>ENDACTIO<br>This item should be left blank if not required. | Not Applicable |
| 2.5 | / | Termination of an ACTIONX Boolean condition record. Note that multiple numbers of records of this type can be entered with each record terminated by a "/", as illustrated above. | Not Applicable |
| 3-1 | / | The Boolean condition section of the ACTIONX keyword is terminated by an empty line with a single "/". | Not Applicable |
|  |  | The next section contains any number of standard SCHEDULE keywords that will be executed if the Boolean expression evaluates to true. For example, to test if the field's gas production rate is less than 600 MMscf/d after 2020 and to open up additional wells if this occurs, then one would use:<br>ACTIONX<br>PHASE2 1 /<br>GGPR \'FIELD\' \< 600E3 AND /<br>YEAR \> 2020 /<br>/<br>\-- WELL PRODUCTION STATUS<br>\--<br>\-- WELL WELL \--LOCATION\-- COMPLETION<br>\-- NAME STAT I J K FIRST LAST<br>WELOPEN<br>GP10 OPEN /<br>GP11 OPEN /<br>/<br>ENDACTIO<br>In theory, most SCHEDULE keywords can be used in an ACTIONX Definition Section here, except for the time stepping keywords, i.e, TSTEP and DATES. See for a list of the SCHEDULE keywords that are known to work with the ACTIONX keyword. | Not Applicable |
| ENDACTIO | Define the end of ACTIONX Definition Section. | Not Applicable |  |
| Notes:<br>1)  There is no terminating "/" for this keyword, instead the ENDACTIO keyword terminates the keyword. |  |  |  |

Table 12.6: ACTIONX Keyword Description

The variable types and the associated definitions that are available for use with Boolean conditionals are outlined in .

| AQUIFER | AQUIFER variable consists of two parameters:<br>1)  Aquifer SUMMARY variable; for example, Analytical Aquifer Influx Rate, AAQR.<br>2)  Aquifer number consisting of a positive integer greater than zero that defines the aquifer to be used. |
| --- | --- |
| BLOCK | BLOCK variable consists of four parameters:<br>1)  Block SUMMARY variable; for example Block Oil Saturation, BOSAT.<br>2)  Block I location which should be a positive integer greater than or equal to one and less than or equal to NX.<br>3)  Block J location which should be a positive integer greater than or equal to one and less than or equal to NY.<br>4)  Block K location which should be a positive integer greater than or equal to one and less than or equal to NZ.<br>The NX, NY, and NZ parameters are defined on the DIMENS keyword in the RUNSPEC section. |
| CONSTANTS | CONSTANTS can consist of one or optionally two parameters:<br>1)  A numerical value defining the Constant.<br>2)  An optional numerical value defining the Increment. If not specified then the Increment defaults to zero. The Increment is added to the Constant after each time the action is executed. The Increment can be positive or negative. |
| FIELD | The FIELD variable consists of any field SUMMARY variable; for example the Field average Pressure, as shown below:<br>ACTIONX<br>WIPHASE 1 /<br>FPR \< 2500 /<br>/<br>\...<br>ENDACTIO<br>The above would action a set of SCHEDULE keywords if the field average pressure fell below 2,500 psia for a run using FIELD units. |
| GROUP | GROUP variable definition consists of:<br>1)  Group SUMMARY variable; for example, Group Oil Production Rate, GOPR.<br>2)  Group Name which is a character string of up to eight characters in length that defines an existing group, note that the group named FIELD is the top most group.<br>To enable an action for when the field's oil production rate drops below 20,000 stb/d then one could use.<br>ACTIONX<br>OILMIN 1 /<br>GOPR \'FIELD\' \< 20.0E3 /<br>/<br>\...<br>ENDACTIO |
| REGION | REGION variable definition consists of:<br>1)  Region SUMMARY variable; selected from one of the following only: RPR, RGSAT, ROSAT, RWSAT, RGIP, ROIP, and RWIP. No other region summary fields are permitted in the expressions.<br>2)  Fluid In-Place region number which is a positive integer greater than or equal to zero that defines the region number. The value should less than or equal to the NTFIP variable on either the REGDIMS or TABDIMS keywords in the RUNSPEC section. Note that a zero value indicates the whole model.<br>3)  Fluid In-Place region family (not used by OPM Flow).<br>For example,<br>ACTIONX<br>WIPHASE 1 /<br>RPR 0 \< 2500 /<br>/<br>\...<br>ENDACTIO<br>Would action a set of SCHEDULE keywords if the field average pressure fell below 2,500 psia for a run using FIELD units. |
| TIME | TIME variable definition consists of one parameter that can have three values: DAY for the current simulation day of the month, MNTH for the current simulation month, and YEAR for the current simulation year.<br>Thus, to set an action for April 1, 2025 one would use:<br>ACTIONX<br>ACT01 1 /<br>DAY = 1 AND /<br>MNTH =\'APR\' AND /<br>YEAR = 2025 /<br>/<br>\...<br>ENDACTIO<br>Note that the value for the MNTH variable, 'APR', in the example, can also be entered without the quotes, that is:<br>MNTH = APR AND /<br>In addition, numerical values for MNTH, similar to DAY and YEAR, are also permitted and are converted to the nearest integer for comparison, so for example:<br>ACTIONX<br>ACT01 1 /<br>DAY = 0.95 AND /<br>MNTH = 4.40 AND /<br>YEAR = 2024.9 /<br>/<br>\...<br>ENDACTIO<br>Would again result in the action taking place on April 1, 2025. |
| WELL | WELL variable definition consists of:<br>1)  Well SUMMARY variable; for example, Well Oil Production Rate, WOPR.<br>2)  Well Name which is a character string of up to eight characters in length that defines the well name, which must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. The Well Name may be defaulted (\'\*\'), a well root (e.g \'OP\*\') or a well list (e.g. \'\*BLK-1\') when used on the LHS of a condition.<br>Note that the use of well lists is an OPM Flow specific feature.<br>To reduce the tubing head pressure constraint for when any of the oil producers' oil rate drop below 100 stb/d then one could use.<br>ACTIONX<br>WOILMIN 1 /<br>WOPR \'OP\*\' \< 100.0 /<br>/<br>\--<br>\-- FLOW WELLS THROUGH LOW PRESSURE SEPARATOR<br>\--<br>\-- WELL WELL TARGET<br>\-- NAME TARG VALUE<br>WELTARG<br>\'OP\*\' THP 150 /<br>/<br>ENDACTIO |
| WELL CONNECTION | WELL CONNECTION variable definition is comprised of:<br>1)  Well connection SUMMARY variable; for example, Connection Oil Flow Rate, COFR.<br>2)  Well Name which is a character string of up to eight characters in length that defines the well, which must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur.<br>3)  I- Connection: A positive integer greater than or equal to zero and less than or equal to NX that defines the connection location in the I-direction<br>4)  J-Connection: A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction.<br>5)  K- Connection: A positive integer greater than or equal to one and less than or equal to NZ that defines the connection location in the K-direction.<br>The NX, NY, and NZ parameters are defined on the DIMENS keyword in the RUNSPEC section. |
| WELL COMPLETION | WELL COMPLETION variable definition is comprised of:<br>1)  Well completion SUMMARY variable of the form W\*L followed one or more underscore characters and the completion number; for example, Well Completion Water Cut for completion number three, WWCTL\_\_3.<br>2)  Well Name which is a character string of up to eight characters in length that defines the well, which must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. |
| WELL LOCAL GRID REFINEMENT CONNECTION | WELL LOCAL GRID REFINEMENT CONNECTION variable definition is comprised of:<br>1)  Well local grid refinement connection SUMMARY variable; for example, the Local Grid Refinement Connection Oil Flow Rate, LCOFR.<br>2)  Well Name which is a character string of up to eight characters in length that defines the well, which must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur.<br>3)  Local Grid Refinement Name which is a character string of up to eight characters in length that defines the Local Grid Refinement ("LGR"), which must have been declared previously using the CARFIN or RADFIN keywords in the GRID section, otherwise an error may occur.<br>4)  I- Connection: A positive integer greater than or equal to zero and less than or equal to NX that defines the connection location in the I-direction within the LGR.<br>5)  J-Connection: A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction within the LGR.<br>6)  K- Connection: A positive integer greater than or equal to one and less than or equal to NZ that defines the connection location in the K-direction within the LGR.<br>The NX, NY, and NZ parameters are defined on either the CARFIN or RADFIN keywords in the GRID section depending upon whether a Cartesian or radial local grid refinement is being utilized.<br>Note Local Grid Refinements are currently not implemented in OPM Flow. |
| WELL SEGMENT | WELL SEGMENT variable definition consists of:<br>1)  Well Segment SUMMARY variable; for example, Segment Oil Flow Rate, SOFR.<br>2)  Multi-Segment Well Name which is a character string of up to eight characters in length that defines the well name which must have been declared previously using the WELSPECS and WELSEGS keywords in the SCHEDULE section, otherwise an error may occur.<br>3)  Segment Number, which is a positive integer greater than or equal to two and less than or equal to MXSEGS on WSEGDIMS keyword in the RUNSPEC section that defines the segment.<br>Note that the total number of wells should be defined via the WELLSDIMS keyword and the number of multi-segment wells should be declared on the WSEGDIMS keyword, both keywords are in the RUNSPEC section. |

Table 12.7: ACTIONX Variable Definitions

See also the ACTDIMS and UDADIMS keyword in the RUNSPEC section to define the dimensions for the ACTIONX keyword and associated variables. In addition, the EXIT keyword in the SCHEDULE section that allows for terminating the simulation for when a condition within an ACTIONX definition is satisfied.

Although most SCHEDULE keywords should work with the ACTIONX keyword, shows the status of keywords that have been tested and known to work, together with keywords that are currently planned to be implemented.

| ACTIONX | GCONINJE | WCONHIST | WPIMULT | COMPDAT | BOX |
| --- | --- | --- | --- | --- | --- |
| UDQ | GCONPROD | WCONINJE | WSEGVALV | COMPLUMP | BRANPROP |
|  | GCONSUMP | WCONINJH | WTEST | COMPSEGS | ECHO |
|  | GEFAC | WCONPROD | WTMULT |  | ENDBOX |
|  | GLIFTOPT | WDFAC |  |  | EXIT^5^ |
|  | GRUPNET | WECON |  |  | INCLUDE^7^ |
|  | GRUPTARG | WEFAC |  |  | MULTX |
|  | GRUPTREE | WELOPEN |  |  | MULTX- |
|  | GSATINJE | WELPI |  |  | MULTY |
|  | GSATPROD | WELSEGS |  |  | MULTY- |
|  |  | WELSPECS^6^ |  |  | MULTZ |
|  |  | WELTARG |  |  | MULTZ- |
|  |  | WGRUPCON |  |  | NEXT |
|  |  | WINJMULT |  |  | NEXTSTEP |
|  |  | WLIST |  |  | NOECHO |
| Notes:<br>3)  Cells not colored show that the keyword has been tested and is functional within an ACTIONX block.<br>4)  Cells colored in gray indicate that the keyword has been tested in OPM Flow but the results are currently different to the commercial simulator.<br>5)  Cells colored orange show keywords that are currently available in OPM Flow but have not been tested; however, testing is ongoing.<br>6)  Cells colored red show keywords currently unavailable in OPM Flow because the underlying feature is not available; however, there are plans to implement this functionality.<br>7)  OPM Flow specific keyword.<br>8)  If a standard well is fully declared in an ACTIONX block which is then activated at a later date, and later the well is modified to be a multi-segment well using the WELSEGS and COMPSEGS keywords, then this will cause the simulator to abort with an assert failure.<br>9)  The INCLUDE keyword is permissible in an OPM Flow ACTIONX block, but this will cause an exception in the commercial simulator. Users must be cautious about the contents of the included file, as conflicts with the base DATA file (e.g., time progression settings) or keywords unsupported by ACTIONX may cause issues. Future updates to the parser may also alter or remove this functionality, so it's advisable not to rely on it for long-term compatibility. |  |  |  |  |  |

*<a id="REF_TABLE_ACTIONX_SCHEDULE_D_STATUS_12_3"></a>Table 12.8: ACTIONX Schedule Section Keywords Status*
As mentioned previously, the UDQ keyword stipulates the variables and operations used to access the User Defined Quantities features in OPM Flow. UDQ variables can be constants, SUMMARY variables, as defined in the SUMMARY section, or a formula using various mathematical functions together with constants and SUMMARY variables.

User Defined Quantities can also be used as User Defined Arguments ("UDA") in the SCHEDULE section with various group, well, and connection keywords. In this case, the UDA variables are used to replace numerical values on these keywords by UDA variables that have been defined by the UDQ keyword. For example, if we wish to make the oil rate for certain wells to be a function of their water cut, then one can define the function using the UDQ keyword that results in a UDQ variable, WU_OPR say, and then use WU_OPR as a UDA variable on the WCONPROD keyword for the ORAT parameter. See [Table 12.76](#anchor-2) for a list of keywords that can be used with UDA variables in the [UDQ - Declare User Define Quantities ("UDQ")](#anchor-3) keyword section.

#### Examples

The first example uses the UDQ keyword to sort the oil wells from high water cut to low, via the WU_WLIST variable, and then use the ACTIONX keyword to shut-in the worst offending well when the field's water production is greater than 30,000 stb/d.

\--

\-- DEFINE START OF USER DEFINED QUANTITY SECTION

\--

UDQ

\--

\-- OPERATOR VARIABLE EXPRESSION

\--

DEFINE WU_WCUT WWCT \'OP\*\' / WELL WWCT LIST

DEFINE WU_LIST SORTD(WU_WCUT) / WELL WWCT LIST SORTED

/ END OF UDQ SECTION

\--

\-- DEFINE START OF ACTIONX SECTION

\--

ACTIONX

WSHUTIN 10 /

GWPR \'FIELD\' \> 30E3 AND /

WU_LIST \'OP\*\' = 1 /

/

\--

\-- DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS

\--

\-- WELL WELL \--LOCATION\-- COMPLETION

\-- NAME STAT I J K FIRST LAST

WELOPEN

\'?\' SHUT /

\'?\' SHUT 0 0 0 0 0 /

/

ENDACTIO

Apart from checking that the field's water production rate is greater than 30,000 stb/d the Boolean conditional also checks that there is at least one well in the sorted well list. Notice also the use of '?' symbol as a substitution of the well name and that the ACTIONX WSHUTIN series of commands will be executed a total of ten times.

The second example checks to see if the field's gas rate is below 600 MMscf/d and if the simulation time is greater that July 1, 2030. If it is, then compression is installed by re-setting all the gas producing well's THP and BHP pressures to 450 psia and 300 psia respectively. In addition all gas wells currently shut-in are tested to see if they can be opened up under the new THP and BHP constraints.

\--

\-- START ACTIONX FIELD PHASE-3 AUTOMATIC COMPRESSION

\--

ACTIONX

PHASE-3 1 /

GGPR \'FIELD\' \< 600E3 AND /

DAY \>= 1 AND /

MNTH \>= JUL AND /

YEAR \>= 2030 /

/

\--

\-- INSTALL COMPRESSION AND RESET WELL THP AND BHPS

\--

\-- WELL WELL TARGET

\-- NAME TARG VALUE

WELTARG

\'GP\*\' THP 450 /

\'GP\*\' BHP 300 /

/

\--

\-- TEST AND OPEN ALL WELLS UNDER COMPRESSION CONSTRAINTS

\--

\-- WELL TEST CLOSE NO. START

\-- NAME INTV CHECK CHECK TIME

WTEST

\'GP\*\' 1.0 PE 1 3 /

/

\--

\-- END OF ACTIONX FIELD PHASE-3 AUTOMATIC COMPRESSION DEFINITION

\--

ENDACTIO
