### UDQDIMS -- Define the Dimensions of the User Defined UDQ Feature

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions associated with the UDQ keyword used in OPM Flow to calculate various user defined values in the SCHEDULE section. The UDQ keyword defined variables can be constants, SUMMARY variables, as defined in the SUMMARY section, or a formula using various mathematical functions together with constants and SUMMARY variables.

Although this keyword is read by OPM Flow and the ACTION and UDQ computational logic and calculations have been implemented, one should used caution using this facility as it may result in OPM Flow aborting.

| 1 | MXFUNS | A positive integer that defines the maximum number of functions that can be included when defining a UDQ definition. This should also include any brackets that will be used in the UDQ definition. | 16 |
| --- | --- | --- | --- |
| 2 | MXITEMS | MXITEMS is a positive integer that defines the maximum number of ITEMS allowed in an UDQ definition. | 16 |
| 3 | MXUDC | MXUDC is a positive integer that defines the maximum number of user defined CONNECTION quantities allowed in an UDQ definition. | 0 |
| 4 | MXUDF | MXUDF is a positive integer that defines the maximum number of user defined FIELD quantities allowed in an UDQ definition. | 0 |
| 5 | MXUDG | MXUDG is a positive integer that defines the maximum number of user defined GROUP quantities allowed in an UDQ definition. | 0 |
| 6 | MXUDR | MXUDR is a positive integer that defines the maximum number of user defined REGION quantities allowed in an UDQ definition. | 0 |
| 7 | MXUDS | MXUDS is a positive integer that defines the maximum number of user defined SEGMENT quantities allowed in an UDQ definition. | 0 |
| 8 | MXUDW | MXUDW is a positive integer that defines the maximum number of user defined WELL quantities allowed in an UDQ definition. | 0 |
| 9 | MXUDA | MXUDA is a positive integer that defines the maximum number of user defined AQUIFER quantities allowed in an UDQ definition. | 0 |
| 10 | MXUDB | MXUDB is a positive integer that defines the maximum number of user defined BLOCK quantities allowed in an UDQ definition. | 0 |
| 11 | RSEED | RSEED is a character string that determines if a new random number seed should be generated for restart runs for use in the UDQ functions RANDN, RANDU RRNDN and RRNDU. If RSEED is set to Y than a new seed will be generated and if set to the default value of N or 1\* then the same seed of the "base" simulation will be employed.<br>See also the RSEED integer variable on the UDQPARAM keyword in the RUNSPEC section to set the random number seed for the current run.<br>This feature is not supported by OPM Flow. | N |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.51: UDQDIMS Keyword Description

Note that OPM Flow has a more restricted UDQ feature set than the commercial simulator, so not all options and functions are available.

#### Example

\--

\-- USER DEFINED ARGUMENT DIMENSIONS FACILITY

\-- MAX MAX MAX MAX MAX MAX MAX MAX MAX MAX RAND

\-- FUNCS ITEMS CONNS FIELD GROUP REGS SEGTM WELL AQUF BLCKS OPT

UDQDIMS

50 25 0 50 50 0 0 0 0 0 N /

In this case the maximum number of functions that can be included when defining a UDQ definition is set to 50, maximum number of items allowed in an UDQ definition is 25, the maximum number of user defined field quantities allowed in an UDQ definition is 50, and the maximum number of user defined group quantities allowed in an UDQ definition is also 50. All other parameters are defaulted including the RSEED variable (the same seed of the "base" simulation will be employed).
