### NMESSAGE -- Export Cumulative Message Summary Variables to File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of a standard set of summary OPM Flow simulation performance summary variables to the [SUMMARY](#__RefHeading___Toc43949_784232322) (\*.SMSPEC and \*.UNSMRY) and RSM (\*.RSM) files, namely the number of messages written per message class. lists the summary variables written out by the [NMESSAGE](#__RefHeading___Toc350871_305403938) keyword.

The keyword is recognized by OPM Flow but none of the variables are currently supported.

| Messages - Cumulative number of BUG messages. | MSUMBUG | Unsupported. |
| --- | --- | --- |
| Messages - Cumulative number of COMMENT messages. | MSUMCOMM | Unsupported. |
| Messages - Cumulative number of ERROR messages. | MSUMERR | Unsupported. |
| Messages - Cumulative number of [MESSAGES](#__RefHeading___Toc61634_2479612490) messages. | MSUMMESS | Unsupported. |
| Messages - Cumulative number of PROBLEM messages. | MSUMPROB | Unsupported. |
| Messages - Cumulative number of WARNING messages. | MSUMWARN | Unsupported. |
| Notes:<br>3)  Cells under the Variable column not colored indicate that the summary variable is available in OPM Flow.<br>4)  Cells under the Variable column colored in gray indicate that the summary variable is recognized by the parser but the summary variable is not available.<br>5)  Cells under the Variable column colored in orange indicate that the summary variable is not recognized by the parser and the summary variable is not available. These summary variables may cause the simulator to abort. |  |  |

Table 11.30: Simulator Performance Summary Variables (Cumulative Messages)

#### Example

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT PERFORMANCE CUMULATIVE MESSAGE VARIABLE VECTORS TO FILE

\--

NMESSAGE

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE

Note the [SEPARATE](#__RefHeading___Toc210158_2884651453) keyword is not required for OPM Flow as this is the default behavior; however, it is probably good practice to include it if the same input decks are being run with the commercial simulator.
