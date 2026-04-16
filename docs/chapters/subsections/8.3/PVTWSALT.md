### PVTWSALT -- Define Brine Water Fluid Properties for Various Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PVTWSALT](#__RefHeading___Toc331848_501926209) defines the brine water properties for various regions in the model, for when the brine phase has been activated by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In this case [PVTWSALT](#__RefHeading___Toc331848_501926209) is used instead of [PVTW](#__RefHeading___Toc2086106_3315222525) in the input file. However, if the [ECLMC](#__RefHeading___Toc206960_803326780) keyword has been entered in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to invoke the Multi-Component Brine model, the [PVTW](#__RefHeading___Toc2086106_3315222525) keyword should be used instead of [PVTWSALT](#__RefHeading___Toc331848_501926209), as with this combination the salinity effect on the density is ignored.

The number of [PVTWSALT](#__RefHeading___Toc331848_501926209) table data sets is defined by the NTPVT parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the allocation of the [PVTWSALT](#__RefHeading___Toc331848_501926209) tables to different grid blocks in the model is done via the [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword in the REGION section.

| 1-1 | PRESS | Single real positive value that defines the reference pressure for the data in the following records (Pref). PRESS should be approximately equal to the average reservoir pressures in the model.<br>The simulator uses the previous time step values to forecast the current time step water properties by linear interpolation. If PRESS is not representative of the average reservoir pressures in the model then the linear interpolation might result in nonphysical values of the water saturation and water viscosity. | None |
| --- | --- | --- | --- |
| psia | barsa | atma |  |
| 1-2 | SALTSURF | A real value that defines the reference salt concentration in the solution in the surface stock tank water (Cs, ref)<br>If defaulted SALTSURF is taken as the minimum salt concentration entered in the SALTCON columnar vector in the second record for this keyword. This should be in most cases be zero. | Defined |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 1-3 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | SALTCON | A columnar vector of real monotonically increasing values that defines the salt concentration in the solution (Cs). | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2-2 | WFVF | WFVF is a real columnar vector defining the water formation volume factor (Bw) at the reference pressure PRESS, for the corresponding salt concentration SALTCON. | None |
| rb/stb | rm^3^/sm^3^ | rcc/scc |  |
| 2-3 | WCOMP | WCOMP is a real columnar vector defining the water compressibility (Cw) at the water reference pressure PRESS, for the corresponding salt concentration SALTCON. The water compressibility is defined as: | None |
| 1/psia | 1/bars | 1/atma |  |
| 2.4 | WVISC | WVISC is a real columnar vector defining the water viscosity (µw) at the water reference pressure PRESS, for the corresponding salt concentration SALTCON. | None |
| cP | cP | cP |  |
| 2.5 | WVISCOMP | WVISCOMP is a real columnar vector defining the water viscosibility (µwc) at the water reference pressure PRESS, for the corresponding salt concentration SALTCON. The water viscosibility is defined as: | None |
| 1/psia | 1/barsa | 1/atma |  |
| 2-6 | / | Table and record terminated by a "/" | Not Applicable |
| Notes:<br>1)  The keyword is followed by NTPVT data sets as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and each data set consists of two records, with items 1-1 to 1-3 representing record one items and 2-1 to 2-6 representing record number two items, etc., in the "No." column in this table.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.123: PVTWSALT Keyword Description

As mentioned above, the simulator first calculates the water properties as functions of the salt concentration at the previous time step by linear interpolation in salt concentration for water compressibility (Cw), water viscosibility (μwc), and. It then calculates the values ofandat the current time step using the current pressure P, using the following equations:

and

See also the [BDENSITY](#__RefHeading___Toc223317_1539708736) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that defines the brine surface densities for the salt concentrations declared on the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword. Note that if the [BDENSITY](#__RefHeading___Toc223317_1539708736) keyword is absent from the input file then the brine surface densities will be set to the water density values declared via the [DENSITY](#__RefHeading___Toc45799_719036256) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. In this case there is no variation in brine surface density with respect to salt concentration.

#### Example

The following shows the [PVTW](#__RefHeading___Toc2086106_3315222525)[SALT](#__RefHeading___Toc593214_516898843) keyword for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set equal to two and NPPVT is set to greater than four on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- WATER SALT PVT TABLE

\--

PVTWSALT

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4500.0 0.000 / TABLE NO. REF. DATA

\--

\-- SALTCON BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.020 2.7E-6 0.370 0.0

2.0 1.010 2.7E-6 0.370 0.0

4.0 1.000 2.7E-6 0.370 0.0

10.0 0.950 2.7E-6 0.370 0.0 / TABLE NO. 01 SALT DATA

\--

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4000.0 0.000 / TABLE NO. 02 REF. DATA

\--

\-- SALTCON BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.005 2.5E-6 0.320 0.0

3.0 1.000 2.5E-6 0.320 0.0

6.0 0.985 2.5E-6 0.320 0.0

12.0 0.930 2.5E-6 0.320 0.0 / TABLE NO. 02 SALT DATA

Note that each table is terminated by a "/" and there is no "/" terminator for the keyword.
