### WDFACCOR -- Gas Flow Dependent Skin Factor (Correlation)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WDFACCOR keyword defines the parameters to calculate a gas well's connection D-factors (flow dependent skin factor) for each connection based on a correlation for the coefficient of inertial resistance, usually known as *β*, in Forchheimer's flow equation[^1]^,[^2],\ [^3]\ ^and [^4]. This keyword uses Dake's correlation to calculate the D-factor.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well D-factor correlation is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section. | None |
| --- | --- | --- | --- |
| 2 | A | A real value greater than or equal to zero that defines the coefficient A in the D-factor correlation. | 0.0 |
| cP.day.ft^2^/mD/Mscf | cP.day.m^2^/mD/sm^3^ | cP.hour.cm^2^/mD/scc |  |
| 3 | B | A real value that defines the exponent B of the grid block permeability in the D-factor correlation. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | C | A real value that defines the exponent C of the grid block porosity in the D-factor correlation. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.260.1: WDFACCOR Keyword Description

The simulator evaluates the connection D-factors using the following expression based on Dake's correlation:

Where:

= effective permeability of the grid block,

= porosity of the grid block,

= connection length,

= wellbore radius,

= gas gravity at surface conditions,

= gas viscosity at bottom hole conditions.

Note that since is dependent on pressure the D-factor will also vary with pressure.

See also the WDFAC keyword in the SCHEDULE section that can be used to specify the well D-factor; and the COMPDAT keyword in the SCHEDULE section that can be used to specify the connection D-factors directly.

#### Examples

In the first example the connection D-factors for gas well GP01 are evaluated for correlation coefficients specified in field units based on the laboratory determined relationship between *β* and the absolute permeability presented by Dake in Fig. 8.8 (variation of *β* with porosity has been neglected).

\--

\-- WELL D-FACTOR CORRELATIONS

\--

\-- WELL

\-- NAME A B C

WEFAC

GP01 6.04E-05 -1.1045 0.0 /

/

In the second example the same correlation coefficients are specified in metric units.

\--

\-- WELL D-FACTOR CORRELATIONS

\--

\-- WELL

\-- NAME A B C

WEFAC

GP01 1.20E-07 -1.1045 0.0 /

/

[^1]: Dake, L.P. Fundamentals of Reservoir Engineering, Amsterdam, The Netherlands, Elsevier Science BV (1978) Chapter 8.6, pages 252-257.

[^2]: Geertsma, J., 1974. Estimating the Coefficient of Inertial Resistance in Fluid Flow Through Porous Media. Soc.Pet.Eng.J., October: 445-450.

[^3]: Gewers, C.W.W. and Nichol, L.R., 1969. Gas Turbulence Factor in a Microvugular Carbonate. J.Can.Pet.Tech., April.

[^4]: Wong, S.W., 1970. Effects of Liquid Saturation on Turbulence Factors for Gas Liquid Systems. J.Can.Pet.Tech., October
