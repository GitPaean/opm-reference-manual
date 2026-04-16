### UDADIMS -- Define the Dimensions of the User Defined Arguments

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions of the User Defined Arguments ("UDA") used by OPM Flow that can be applied to various connection, group, and well keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. UDAs are defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword that is used to specify values to be constants, [SUMMARY](#__RefHeading___Toc43949_784232322) variables, as defined in [SUMMARY](#__RefHeading___Toc43949_784232322) section, or a formula using various mathematical functions together with constants and [SUMMARY](#__RefHeading___Toc43949_784232322) variables.

Although this keyword is read by OPM Flow and the [ACTION](#__RefHeading___Toc148342_63720426) and [UDQ](#__RefHeading___Toc161095_2932703077) computational logic and calculations have been implemented, one should used caution using this facility as it may result in OPM Flow aborting.

| 1 | NMUDA | NMUDA is a positive integer that defines the number of arguments in a [SCHEDULE](#__RefHeading___Toc43945_784232322) section keyword, that are replaced by numeric [UDQ](#__RefHeading___Toc161095_2932703077) values. | 0 |
| --- | --- | --- | --- |
| 2 | IGNORED | Not used and should be defaulted. | 1\* |
| 3 | MXUDA | MXUDA is a positive integer that defines the maximum number of unique* *arguments in a keyword that are replaced by numeric UDA values.<br>Note that MXUDA differs from NMUDA, for example:<br>1)  If only the oil rate argument of, say the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword is specified by a UDA, then both NMUDA and MXUDA equal one.<br>2)  However, if a second [WCONPROD](#__RefHeading___Toc146754_4203985108) uses a different UDA, then NMUDA equals two, but MXUDA would still be one.<br>3)  Finally, if the same two distinct UDAs are used separately in two lines of [WCONPROD](#__RefHeading___Toc146754_4203985108) data, then both NMUDA and MXUDA must be set to two.<br>As MXUDA's default value is 100 then this only needs to be increased where the same UDA is used more than 100 times. | 100 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.50: UDADIMS Keyword Description

Note that OPM Flow has a more restricted [UDQ](#__RefHeading___Toc161095_2932703077) feature set than the commercial simulator, so not all options and functions are currently available.

#### Example

\--

\-- USER DEFINED ARGUMENT DIMENSIONS

\-- NO. NOT TOTAL

\-- ARGS USED UDQ

UDADIMS

10 1\* 10 /

In the above example both NMUDA and MXUDA are set equal to ten.
