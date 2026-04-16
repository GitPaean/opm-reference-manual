### UDQPARAM -- Define Parameters for the User Defined Quantity Feature

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions of the User Defined Arguments ("UDA") used by OPM Flow that can be applied to various connection, group, and well keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. UDAs are defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword that is used to specify values to be constants, [SUMMARY](#__RefHeading___Toc43949_784232322) variables, as defined in [SUMMARY](#__RefHeading___Toc43949_784232322) section, or a formula using various mathematical functions together with constants and [SUMMARY](#__RefHeading___Toc43949_784232322) variables.

Although this keyword is read by OPM Flow and the [ACTION](#__RefHeading___Toc148342_63720426) and [UDQ](#__RefHeading___Toc161095_2932703077) computational logic and calculations have been implemented, one should used caution using this facility as it may result in OPM Flow aborting.

| 1 | RSEED | RSEED is a positive integer greater than zero that sets a new random number seed for use in the [UDQ](#__RefHeading___Toc161095_2932703077) functions RANDN, RANDU RRNDN and RRNDU.<br>See also the RSEED character variable on the [UDQDIMS](#__RefHeading___Toc65916_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to default the random number seed for a restart run.<br>This feature is not supported by OPM Flow. | 1 |
| --- | --- | --- | --- |
| 2 | RANGE | RANGE is a real positive value greater than or equal to one and less than or equal to 1.0 x 10^20^, that sets the absolute range for the user defined quantities.<br>The default value of 1 x 10^20^ sets the range from -1 x 10^20^ to +1 x 10^20^. | 1 x 10^20^ |
| 3 | DEFAULT | DEFAULT is real value that is the default numerical value given to undefined [UDQ](#__RefHeading___Toc161095_2932703077) variables and should be in the same range as RANGE. | 0.0 |
| 4 | TOLUDQ | TOLUDQ a real positive number greater than zero and less than one that defines the tolerance used to determine if two real values are equal.<br>Floating-point numbers (as implemented in computers) are never exact, one cannot compare floating point numbers for exact equality. Thus, TOLUDQ defines a tolerance. For example, the default value of 1 x 10-4 means that if the difference between two real values is less than 1 x 10-4 then the values are considered equal. | 1 x 10-4 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.52: UDQPARAM Keyword Description

Note that OPM Flow has a more restricted [UDQ](#__RefHeading___Toc161095_2932703077) feature set than the commercial simulator, so not all options and functions are available.

#### Example

\--

\-- USER DEFINED DEFAULT VALUES

\-- SEED RANGE UNDEFINED COMPARISON

\-- INTG -AND+ VALUE TOLERANCE

UDQPARAM

1 1.0E20 0.0 1.0E-4 /

The example explicitly sets the default values for all four variables on the UDAPARAM keyword, namely the random seed to one, the range to 1 x 1020, the undefined [UDQ](#__RefHeading___Toc161095_2932703077) variables to zero, and the comparison tolerance to 1.0 x 10-4.
