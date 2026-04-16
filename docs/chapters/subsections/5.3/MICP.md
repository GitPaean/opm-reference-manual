### MICP -- Activate the Microbially Induced Calcite Precipitation Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MICP](#__RefHeading___Toc383375_111689907) keyword activates the Microbially Induced Calcite Precipitation ("MICP") model for the run. [MICP](#__RefHeading___Toc383375_111689907) is a new and sustainable technology which utilizes biochemical processes to create barriers by calcium carbonate cementation, the technology has the potential to be used for sealing leakage zones in geological formations. Further information on the mathematical model can be found in the open-access publications Landa-Marbán et al[^1] and [^2].

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE MICROBIAL INDUCED CALCITE PRECIPITATION MODEL

\--

MICP

\--

\-- WATER PHASE IS PRESENT IN THE RUN

\--

WATER

The above example declares that the [MICP](#__RefHeading___Toc383375_111689907) model is active for the run and activates the water phase for the [MICP](#__RefHeading___Toc383375_111689907) model. For a complete example of this model, see [MICP.DATA](https://github.com/OPM/opm-tests/blob/master/micp/MICP.DATA).

[^1]: Landa-Marbán, D., Tveit, S., Kumar, K., Gasda, S.E., 2021. Practical approaches to study microbially induced calcite precipitation at the eld scale. Int. J. Greenh. Gas Control 106, 103256. https://doi.org/10.1016/j.ijggc.2021.103256.

[^2]: Landa-Marbán, D., Kumar, K., Tveit, S., Gasda, S.E., 2021. Numerical studies of CO2 leakage remediation by micp-based plugging technology. In: Røkke, N.A. and Knuutila, H.K. (Eds) Short Papers from the 11th International Trondheim CCS conference, ISBN: 978-82-536-1714-5, 284-290.
