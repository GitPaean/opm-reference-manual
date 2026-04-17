### UDADIMS -- Define the Dimensions of the User Defined Arguments

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions of the User Defined Arguments ("UDA") used by OPM Flow that can be applied to various connection, group, and well keywords in the SCHEDULE section. UDAs are defined by the UDQ keyword that is used to specify values to be constants, SUMMARY variables, as defined in SUMMARY section, or a formula using various mathematical functions together with constants and SUMMARY variables.

Although this keyword is read by OPM Flow and the ACTION and UDQ computational logic and calculations have been implemented, one should used caution using this facility as it may result in OPM Flow aborting.

| 1 | NMUDA | NMUDA is a positive integer that defines the number of arguments in a SCHEDULE section keyword, that are replaced by numeric UDQ values. | 0 |
| --- | --- | --- | --- |
| 2 | IGNORED | Not used and should be defaulted. | 1\* |
| 3 | MXUDA | MXUDA is a positive integer that defines the maximum number of unique* *arguments in a keyword that are replaced by numeric UDA values.<br>Note that MXUDA differs from NMUDA, for example:<br>1)  If only the oil rate argument of, say the WCONPROD keyword is specified by a UDA, then both NMUDA and MXUDA equal one.<br>2)  However, if a second WCONPROD uses a different UDA, then NMUDA equals two, but MXUDA would still be one.<br>3)  Finally, if the same two distinct UDAs are used separately in two lines of WCONPROD data, then both NMUDA and MXUDA must be set to two.<br>As MXUDA's default value is 100 then this only needs to be increased where the same UDA is used more than 100 times. | 100 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.50: UDADIMS Keyword Description

Note that OPM Flow has a more restricted UDQ feature set than the commercial simulator, so not all options and functions are currently available.

#### Example

\--

\-- USER DEFINED ARGUMENT DIMENSIONS

\-- NO. NOT TOTAL

\-- ARGS USED UDQ

UDADIMS

10 1\* 10 /

In the above example both NMUDA and MXUDA are set equal to ten.
