### PLYVMH -- Polymer Molecular Weight Model Polymer Viscosity Constants

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, PLYVMH, defines the constants used to calculate viscosity of the polymer solution as a function of the polymer molecular weight and the polymer concentration, for the simulator\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity. The keyword consists of a series of row vectors, which each vector having four elements, that define the constants used in calculating the polymer viscosity

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.

| 1<br>‍ | MHK<br>| | The Mark-Houwink K polymer specific constant in the Mark-Houwink equation, see equation .<br>| | None<br>| |
| --- | --- | --- | --- |
|  | ml/g |  |  |
| 2 | MHA | The Mark-Houwink exponent parameter a, in the Mark-Houwink equation, see equation . | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GAMMA | The ɣ intrinsic water-polymer viscosity constant in the Huggins equation, see equation . | None |
|  |  |  |  |
| 4 | KAPPA | The κ intrinsic water-polymer viscosity constant in the Huggins equation, see equation . | None |
|  |  |  |  |
| Notes:<br>1)  The keyword is followed by NPLYVHM records as declared on the PINTDIMS keyword in the RUNSPEC section, with each record terminated by a "/" and the keyword itself should be terminated by a "/". |  |  |  |

Table 8.109: PLYVMH Keyword Description

The high molecular weight of polymers greatly increase the viscosity of the injected water in which they are dissolved, thus adjusting the mobility ration of the displacing phase. The increase in viscosity is caused by strong internal friction between the randomly coiled and swollen macro molecules and the surrounding water molecules. And is dependent on both the nature of the polymer and the injected water acting as the solvent. There are several formulations of viscosity associated with polymer rheology, namely:

Relative viscosity is defined as:

where:

= is the relative viscosity,

= is the viscosity of the solution, and

= is the viscosity of the solvent (injected water).

Specific viscosity is defined as:

where:

= is the specific water-polymer viscosity, and

= is the viscosity of the solvent (injected water).

Reduced Specific Viscosity is given by:

where:

= is the reduced specific water-polymer viscosity, and

= is the polymer concentration.

Finally, the Intrinsic Velocity, which is defined as a measure for the internal friction in polymer solutions at the limit of zero polymer concentration. Thus, this quantity describes the effect of completely separated polymer chains on the solution viscosity, and is defined as:

where:

= is the intrinsic water-polymer viscosity and describes the increase in

viscosity arising from an individual polymer chain and is a measure of the polymers\' thickening power, and

= zero-shear viscosity.

For any given solvent pair, the intrinsic viscosity increases as the molecular weight of the polymer increases; here, the *Mark-Houwink equation*, also known as the Mark-Houwink-Staudinger equation[^1], [^2], and [^3] is used to calculate \[η\], that is:

where:

= is the polymer specific constant in the Mark-Houwink equation, the MHK

parameter in ,

= is the polymer molecular weight, and

= the exponent constant in the Mark-Houwink equation, the MHA parameter

in .

The Mark-Houwink parameters can be determined from a double logarithmic plot of intrinsic viscosity versus molecular weight which yields straight lines, that is:

OPM Flow uses a form of the Huggins[^4] equation to calculate the polymer apparent viscosity, as shown below:

where:

= a user defined constant, GAMMA in , and

= a user defined constant, KAPPA in .

Which can be used to calculate the zero-shear viscosity, η~0~, based on the quadratic function in equation time polymer concentration(C~p~) and polymer intrinsic viscosity described in equation .

In terms of the keyword units, given the intrinsic viscosity in ml/g, polymer concentration in kg/m3, and the molecular weight as kg/kg-M, then equation becomes:

and equation becomes:

Note that the model does not account for non-Newtonian flow; the apparent viscosity is simply set equal to the zero-shear viscosity, and that the model only considers the full mixing between the polymer and water.

See also the PLYMWINJ keyword in the PROPS section, that describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity. Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.

#### Example

Given NPLYVMH equals two on the PINTDIMS keyword in the RUNSPEC section, then:

\--

\-- POLYMER MOLECULAR WEIGHT MODEL POLYMER VISCOSITY CONSTANTS

\-- (OPM FLOW PROPS KEYWORD)

\--

\-- MHK MHA VISC VISC

\-- CONST EXPON GAMMA KAPPA

PLYVMH

0.02 0.50 0.40 0.60 /

0.03 0.51 0.42 0.63 /

/

Two sets of data should be entered with the PLYVMH keyword, as shown above.

[^1]: H. Mark, in R. Saenger, Der feste Koerper, Hirzel, Leipzig, 1938.

[^2]: R. Houwink , J. Prakt. Chem., Vol. 157, Issue 1-3, p. 15 (1940).

[^3]: H. Staudinger, **Die Hochmolekulare Organischen Verbindungen**, Julius Springer, Berlin 1932.

[^4]: Huggins, M. L. 1942. The viscosity of dilute solutions of long-chain molecules. IV. Dependence on concentration.» Journal of the American Chemical Society 64 (11): 2716-2718.
