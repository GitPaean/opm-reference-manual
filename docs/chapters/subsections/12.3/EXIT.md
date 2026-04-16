### EXIT -- Exit Simulation from within an Action Section

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EXIT](#__RefHeading___Toc627737_1466963378) keyword is part of OPM Flow's [ACTION](#__RefHeading___Toc148342_63720426) facility that allows for terminating the simulation for when a condition within an [ACTIONX](#__RefHeading___Toc152227_2992482751) definition is satisfied. Invoking the keyword within an [ACTIONX](#__RefHeading___Toc152227_2992482751) definition will result in the simulation terminating with an exit status code. The [ACTION](#__RefHeading___Toc148342_63720426) facility allows the user to enter computational logic to the simulation run based on the how the simulation run is proceeding -- see the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EXITCODE | An optional integer that sets the exit code printed to the \*.PRT file, if not not defined the default value of zero will be used. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

*Table 12.25: EXIT Keyword Description*
The [EXIT](#__RefHeading___Toc627737_1466963378) keyword should only be used as part of an [ACTIONX](#__RefHeading___Toc152227_2992482751) block, if found elsewhere in the input deck it will be ignored.

#### Examples

The first example uses the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword to define a condition for when the Field Oil Production Rate ("FOPR) falls below 1,000 stb/d (or 1,000 m^3^) using the default value for the EXITCODE.

\--

\-- DEFINE START OF ACTIONX SECTION

\--

ACTIONX

\'CHECK_FOPR\' 100000 /

FOPR \< 1000 /

/

\--

\-- TERMINATE AND EXIT SIMULATION

\--

EXIT

/

ENDACTIO

The next example terminates the simulation with EXITCODE one when the Field Pressure ("FPR") falls below 200 psia (or 200 barsa).

\--

\-- DEFINE START OF ACTIONX SECTION

\--

ACTIONX

\'CHECK_FPR\' 100000 /

FPR \< 200 /

/

\--

\-- TERMINATE AND EXIT SIMULATION

\--

EXIT

1 /

ENDACTIO

Note is is probably good practice to always set the EXITCODE to be able to identify the reason for the simulation stopping.
