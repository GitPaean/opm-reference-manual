### PVTSOL -- Oil PVT Properties for Live Oil versus CO2 Mass Fraction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PVTSOL](#__RefHeading___Toc414279_1093985484) defines the live oil PVT properties as a function of CO~2~ mass fraction. The keyword automatically invokes the simulator's CO2 Dynamic EOR Model[^1], that uses a fourth component to model the injected CO~2.~, for use in evaluating CO~2~ Enhanced Oil Recovery ("EOR") projects. Normally CO~2~ EOR projects are evaluated via compositional simulators to account for the mass transfer of the various components and phases. Unfortunately, compositional models are computationally expensive compared to the black-oil approach, which for field studies is challenging, especially if an ensemble approach is being used to capture the uncertainties. Previous extended black-oil formulations often poorly represent the PVT properties of the oil-CO~2~ mixtures, resulting in poor agreement with the compositional formulation.

To overcome the limitations of the standard four component black-oil formulation, OPM Flow uses an improved extended black-oil formulation, the CO2 Dynamic EOR Model, with the black-oil properties dependent on the fraction of CO2 in the cell, as described by the [PVTSOL](#__RefHeading___Toc414279_1093985484) keyword. This approach models the oil-CO2 mixture more accurately and thus give results closer to the compositional simulator. Data for the keyword should normally be derived from laboratory or numerical slim-tube experiments based on one-dimensional compositional Equation Of State ("EOS") simulations.

Note, if this keyword is absent from the input deck then the CO2 Standard EOR Model is used instead.

| 1 | CO2 | A real monotonically increasing down the column values that stipulates the CO2 mass fraction, that defines the oil and gas properties, formation volume factor, viscosity etc., for the tabulated corresponding pressure for the stated CO2 mass fraction.<br>CO2 should be greater than or equal to zero and less than or equal to one. Note it is not necessary to repeat the value of CO2 for the pressure column. However, for a given CO2 mass fraction, the last pressure entry (PRESS) of the sub table should be terminated by a "/". | None |  |
| --- | --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |  |
| 2 |  | PRESS | PRESS is a real columnar vector of real monotonically increasing down the column values that defines the oil phase saturation pressure (bubble-point pressure), that defines the oil formation volume factor and the oil viscosity for the corresponding PRESS pressure for a given saturated value of CO2. | None |
| psia | barsa | atma |  |  |
| 3 |  | OFVF | OFVF is a columnar vector of real increasing down the column values that defines the corresponding oil phase saturated formation volume factor for a given pressure (PRESS) and for a given saturated value of CO2. | None |
| rb/stb | rm^3^/sm^3^ | rcc/scc |  |  |
| 4 |  | GFVF | GFVF is a columnar vector of real decreasing down the column values that defines the corresponding gas phase saturated formation volume factor for a given pressure (PRESS) and for a given saturated value of CO2. | None |
| rb/Mscf | rm^3^/sm^3^ | rcc/scc |  |  |
| 5 |  | [RS](#__RefHeading___Toc137361_1317547213) | [RS](#__RefHeading___Toc137361_1317547213) is a real monotonically increasing down the column values that defines the saturated gas-oil ratio ("GOR") or Rs, for the given value of PRESS and for a given saturated value of CO2. | None |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |  |
| 6 |  | [RV](#__RefHeading___Toc137365_1317547213) | [RV](#__RefHeading___Toc137365_1317547213) is a real monotonically increasing down the column values that defines the saturated condensate-gas ratio ("CGR") or Rv, for the given value of PRESS and for a given saturated value of CO2. | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |  |
| 7 |  | XVOL | XVOL is a real positive value greater than or equal to zero and less than or equal to one, that stipulates the volumetric fraction of CO2 in the oil phase, that is:<br>where:<br>Volume ~oil\ ~(CO~2~) is the surface volume of CO~2~ in the oil phase,<br>Volume oil~\ ~(Gas) is the surface volume of gas in the oil phase, and<br>Volume ~oil~ (Oil) is the surface volume of oil in the oil phase. | None |
| dimensionless | dimensionless | dimensionless |  |  |
| 8 |  | YVOL | YVOL is a real positive value greater than or equal to zero and less than or equal to one, that defines the volumetric fraction of CO2 in the gas phase, that is:<br>where:<br>Volume ~gas\ ~(CO~2~) is the surface volume of CO~2~ in the gas phase,<br>Volume ~gas\ ~(Gas) is the surface volume of gas in the gas phase, and<br>Volume gas (Oil) is the surface volume of oil in the gas phase. | None |
| dimensionless | dimensionless | dimensionless |  |  |
| 9 |  | OVISC | OVISC is a columnar vector of real decreasing down the column values that defines the corresponding oil phase saturated viscosity for a given pressure (PRESS) and for a given saturated value of CO2. | None |
| cP | cP | cP |  |  |
| 10 |  | GVISC | GVISC is a columnar vector of real increasing down the column values that defines the corresponding gas phase saturated viscosity for a given pressure (PRESS) and for a given saturated value of CO2. | None |
| cP | cP | cP |  |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows and NRPVT Rs entries as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Except for the CO2 column, there must be same number of entries for each column.<br>4)  Each sub table defining the properties for a given value of CO2 must be terminated by "/" and the keyword itself is terminated by "/". |  |  |  |  |

Table 8.121: PVTSOL Keyword Description

See also the [PVDS](#__RefHeading___Toc104058_57619843) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that can also be used to model CO2 injection, using the [SOLVENT](#__RefHeading___Toc62787_1778172979) model (CO2 Standard EOR), this is the conventional approach, and does not take into account black-oil properties being dependent on the fraction of CO2.

As an aside, the scope and accuracy of gas condensate modeling using black-oil reservoir simulators is well established in the industry; both depletion and gas cycling above the dew point can be modeled and yield an adequate match with the results from multi-component compositional simulators. The main inadequacy is with the treatment of gas injection below the dew point where the primary compositional effect, the stripping of liquid components is inversely proportional to their molecular weights, is completely ignored. The standard black-oil model assumes that the saturated hydrocarbon fluid properties are functions of pressure only and disregards any compositional dependence in the saturated fluid PVT properties. Thus, when dry gas is injected into a condensate below its dew point the gas continues to re-vaporize liquid at a rate governed only by the ambient pressure. The vapor saturates over a zone whose thickness is of the order of one grid block; in particular all the liquid in the vicinity of the injectors evaporates rapidly. Results obtained with fully compositional simulation models suggest that liquid saturation profiles would vary more slowly with increasing distance from the gas injectors. This compositional effect can thus be modeled via the CO2 Dynamic EOR Model, although there are no test cases at this stage.

#### Example

\--

\-- OIL PVT PROPERTIES FOR LIVE OIL VERSUS CO2 MASS FRACTION

\--

PVTSOL

\-- CO2 PSAT BO BG RS RV XVOL YVOL OIL VISC GAS VISC

\-- MFRAC PSIA RB/STB RB/MSCF MSCF/STB STB/MSCF CPOISE CPOISE

\-- \-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\--

0.000 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.0000 0.0000 2.0340e-01 1.3016e-02

725.18 1.0655 6.0855e+00 0.1302 1.4432e-04 0.0000 0.0000 2.0340e-01 1.3016e-02

870.22 1.0806 5.0340e+00 0.1591 1.9594e-04 0.0000 0.0000 1.9973e-01 1.3222e-02

1015.26 1.0961 4.2814e+00 0.1886 2.8389e-04 0.0000 0.0000 1.9609e-01 1.3452e-02

1160.30 1.1121 3.7174e+00 0.2189 4.1914e-04 0.0000 0.0000 1.9246e-01 1.3708e-02

1305.33 1.1285 3.2799e+00 0.2499 6.0779e-04 0.0000 0.0000 1.8886e-01 1.3994e-02

1450.37 1.1454 2.9314e+00 0.2819 8.5105e-04 0.0000 0.0000 1.8527e-01 1.4309e-02

1595.41 1.1629 2.6479e+00 0.3148 1.1490e-03 0.0000 0.0000 1.8171e-01 1.4657e-02

1740.45 1.1809 2.4133e+00 0.3487 1.5030e-03 0.0000 0.0000 1.7819e-01 1.5037e-02

1885.49 1.1996 2.2163e+00 0.3838 1.9155e-03 0.0000 0.0000 1.7469e-01 1.5450e-02

2030.52 1.2189 2.0490e+00 0.4200 2.3899e-03 0.0000 0.0000 1.7122e-01 1.5897e-02

2175.56 1.2389 1.9055e+00 0.4574 2.9302e-03 0.0000 0.0000 1.6779e-01 1.6377e-02

2320.60 1.2597 1.7812e+00 0.4962 3.5412e-03 0.0000 0.0000 1.6440e-01 1.6890e-02

2465.64 1.2812 1.6728e+00 0.5364 4.2273e-03 0.0000 0.0000 1.6104e-01 1.7435e-02

2610.67 1.3037 1.5775e+00 0.5782 4.9942e-03 0.0000 0.0000 1.5772e-01 1.8011e-02

2755.71 1.3270 1.4933e+00 0.6216 5.8471e-03 0.0000 0.0000 1.5443e-01 1.8617e-02

2900.75 1.3514 1.4185e+00 0.6668 6.7918e-03 0.0000 0.0000 1.5117e-01 1.9253e-02

3045.79 1.3768 1.3517e+00 0.7139 7.8347e-03 0.0000 0.0000 1.4795e-01 1.9917e-02

3137.32 1.3937 1.3132e+00 0.7450 8.5549e-03 0.0000 0.0000 1.4592e-01 2.0353e-02

4061.05 1.3705 1.3132e+00 0.7450 8.5549e-03 0.0000 0.0000 1.5939e-01 2.0353e-02 /

0.010 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.0464 0.0381 2.0301e-01 1.3203e-02

725.18 1.0670 6.0041e+00 0.1341 1.4845e-04 0.0464 0.0381 2.0301e-01 1.3203e-02

.......................................................................................................................................................................\........................................\...

3135.04 1.4082 1.2950e+00 0.7755 8.9113e-03 0.0298 0.0277 1.4422e-01 2.0743e-02

4061.05 1.3840 1.2950e+00 0.7755 8.9113e-03 0.0298 0.0277 1.5772e-01 2.0743e-02 /

0.100 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.3426 0.3023 1.9984e-01 1.4740e-02

725.18 1.0795 5.3329e+00 0.1666 1.8243e-04 0.3426 0.3023 1.9984e-01 1.4740e-02

.......................................................................................................................................................................\........................................\...

3116.25 1.5281 1.1444e+00 1.0268 1.1849e-02 0.2492 0.2431 1.3023e-01 2.3961e-02

4061.05 1.4955 1.1444e+00 1.0268 1.1849e-02 0.2492 0.2431 1.4400e-01 2.3961e-02 /

0.200 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.5303 0.4898 1.9699e-01 1.5838e-02

725.18 1.0909 4.8402e+00 0.1964 2.1919e-04 0.5303 0.4898 1.9699e-01 1.5838e-02

.......................................................................................................................................................................\........................................\...

4061.05 1.6501 1.0017e+00 1.3720 1.6728e-02 0.4220 0.4240 1.2963e-01 2.7757e-02 /

0.300 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.6486 0.6159 1.9471e-01 1.6588e-02

725.18 1.1003 4.4992e+00 0.2210 2.5440e-04 0.6486 0.6159 1.9471e-01 1.6588e-02

.......................................................................................................................................................................\........................................\...

4061.05 1.8529 8.8189e-01 1.8200 2.4541e-02 0.5491 0.5597 1.1636e-01 3.2195e-02 /

0.400 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.7303 0.7059 1.9292e-01 1.7131e-02

725.18 1.1079 4.2506e+00 0.2413 2.8832e-04 0.7303 0.7059 1.9292e-01 1.7131e-02

.......................................................................................................................................................................\........................................\...

4061.05 2.1298 7.8515e-01 2.4251 3.7664e-02 0.6468 0.6616 1.0441e-01 3.7755e-02 /

0.500 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.7905 0.7733 1.9156e-01 1.7543e-02

725.18 1.1140 4.0628e+00 0.2581 3.2217e-04 0.7905 0.7733 1.9156e-01 1.7543e-02

.......................................................................................................................................................................\........................................\...

4061.05 2.5282 7.1557e-01 3.2879 6.0741e-02 0.7245 0.7379 9.3885e-02 4.5038e-02 /

0.600 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.8372 0.8259 1.9061e-01 1.7868e-02

725.18 1.1188 3.9168e+00 0.2720 3.5813e-04 0.8372 0.8259 1.9061e-01 1.7868e-02

.......................................................................................................................................................................\........................................\...

4061.05 3.1455 6.8307e-01 4.6154 1.0176e-01 0.7880 0.7951 8.4761e-02 5.4583e-02 /

0.700 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.8755 0.8686 1.9018e-01 1.8132e-02

725.18 1.1223 3.8017e+00 0.2833 4.0084e-04 0.8755 0.8686 1.9018e-01 1.8132e-02

.......................................................................................................................................................................\........................................\...

4061.05 3.3568 6.6803e-01 5.4784 1.3282e-01 0.9106 0.9124 8.9321e-02 6.2163e-02 /

0.800 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.9520 0.9591 1.8807e-01 1.8720e-02

725.18 1.1335 3.5254e+00 0.3153 5.0228e-04 0.9520 0.9591 1.8807e-01 1.8720e-02

.......................................................................................................................................................................\........................................\...

4061.05 2.7406 5.5115e-01 3.5079 8.5588e-02 0.8828 0.8905 8.1404e-02 7.0425e-02 /

0.900 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 0.9846 0.9855 1.9003e-01 1.8852e-02

725.18 1.1293 3.5076e+00 0.3007 4.6299e-04 0.9846 0.9855 1.9003e-01 1.8852e-02

.......................................................................................................................................................................\........................................\...

4061.05 1.9854 5.0045e-01 2.0535 3.9219e-02 0.9400 0.9448 1.0088e-01 6.5831e-02 /

1.000 14.50 1.0000 1.7810e+02 0.0000 0.0000e+00 1.0000 1.0000 1.7716e-01 1.8887e-02

725.18 1.1418 3.5421e+00 0.2487 1.7810e-10 1.0000 1.0000 1.7716e-01 1.8887e-02

.......................................................................................................................................................................\........................................\...

4061.05 1.2145 4.3773e-01 0.6633 4.2745e-09 1.0000 1.0000 1.4288e-01 6.2211e-02 /

/

The above example defines one oil PVT Properties for Live Oil versus CO2 Mass Fraction table, and assumes that NTPVT equals one the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

[^1]: T. H. Sandve, O. Sævareid and I. Aavatsmark: "Improved Extended Blackoil Formulation \-- for CO2 EOR Simulations." in ECMOR XVII -- The 17th European Conference on the \-- Mathematics of Oil Recovery, September 2020.
