### WDFAC -- Define Gas Flow Dependent Skin Factor

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WDFAC](#__RefHeading___Toc442057_2026549522) keyword defines a gas well's D-factor (flow dependent skin factor), which is normally derived from well tests or calculated analytically based on the coefficient of inertial resistance, usually known as *β*, in Forchheimer's flow equation^,[^1],\ [^2]\ ^and [^3].

Internally the simulator evaluates a D-factor for each well connection by assuming the D-factors are inversely proportional to the connection transmissibility factors. This is done at the time the well D-factor is specified. If a connection is later closed then the well D-factor is likely to change but the connection D-factors for each of the remaining open connections should not be affected.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well D-factor is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. | None |
| --- | --- | --- | --- |
| 2 | DFACTOR | A real positive value greater than or equal to zero that defines the D-factor for the well. | 0.0 |
| day/Mscf | day/m^3^ | hour/scc |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.259.1: WDFAC Keyword Description

See also the [WDFACCOR](#__RefHeading___Toc48144_327352552) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that uses Dake's[^4] correlation to calculate the well D-factor; and the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that can be used to specify the connection D-factors directly.

#### Example

\--

\-- WELL D-FACTORS

\--

\-- WELL D-

\-- NAME FACTOR

WEFAC

GP01 1.0E-03 /

/

In the above example a well D-factor of 10^-3^ is specified for gas well GP01.

[^1]: Geertsma, J., 1974. Estimating the Coefficient of Inertial Resistance in Fluid Flow Through Porous Media. Soc.Pet.Eng.J., October: 445-450.

[^2]: Gewers, C.W.W. and Nichol, L.R., 1969. Gas Turbulence Factor in a Microvugular Carbonate. J.Can.Pet.Tech., April.

[^3]: Wong, S.W., 1970. Effects of Liquid Saturation on Turbulence Factors for Gas Liquid Systems. J.Can.Pet.Tech., October

[^4]: Dake, L.P. Fundamentals of Reservoir Engineering, Amsterdam, The Netherlands, Elsevier Science BV (1978) Chapter 8.6, pages 252-257.
