### VFPPROD -- Define Production Vertical Flow Performance Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword defines production Vertical Flow Performance ("VFP") tables that are used to determine the outflow or downstream pressure based on the inlet or upstream pressure and the phases flowing through the system. For a production well this means the table relates the flowing bottom-hole pressure ("BHP") to the well's tubing head pressure ("THP") based on the oil, gas and water rates (and any artificial lift quantities (\"ALQ\") like gas lift gas), or phases ratios, flowing up the wellbore. The table is also used to describe the pressure relationship when the network option is being used. In this case the table describes the pipeline pressure behavior from the LOWER group (inlet node) to the HIGHER group (outlet node) given the current flowing conditions (the group relationship is defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword in [SCHEDULE](#__RefHeading___Toc43945_784232322) section).

Each [VFPPROD](#__RefHeading___Toc121919_2556401936) table must be entered with a separate [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword that consists of seven records, with 1-1 to 1-9 representing record one items (1) to (9), 2-1 representing record two item (1), and so on in the "No." column in . Each record is terminated by a "/".

The seventh record should be repeated to give BHP data as a function of FLO for each combination of THP, WFR, GFR, and ALQ values. If record seven is only entered once then the BHP values will depend only on flow rate (FLO), and will be replicated across all combinations of THP, WFR, GFR, and ALQ values.

| 1-1 | VFPTAB | A positive integer greater than zero and less than or equal to the MXVFPTAB variable as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the vertical lift performance table number. | None |
| --- | --- | --- | --- |
| 1-2 | VFPREF | A real positive value that defines the reference depth used to generate this [VFPPROD](#__RefHeading___Toc121919_2556401936) table data set.<br>OPM Flow automatically corrects any difference between VFPREF and the BHPREF on the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, using the current hydrostatic head. | None |
| 1-3 | FLO | A defined character string that defines the flowing phases, and should be set to one of the following character strings:<br>1)  GAS: for flowing phase being the gas rate.<br>2)  OIL: for flowing phase being the oil rate.<br>3)  LIQ: for flowing phase being the liquid (oil plus water) rate. | None |
| 1-4 | WFR | A defined character string that defines the flowing water fraction and should be set to one of the following character strings:<br>1)  WOR: for the water fraction being the water-oil ratio and should be used if FLO is set to \'OIL\' or \'LIQ\'<br>2)  WCT: for the water fraction being the water cutand should be used if FLO is set to \'OIL\' or \'LIQ\'<br>3)  WGR: for the water fraction being the water-gas ratioand should be used if FLO is set to \'GAS\'. | None |
| 1-5 | GFR | A defined character string that defines the flowing gas fraction and should be set to one of the following character strings:<br>1)  GOR: for the gas fraction being the gas-oil ratioand should be used if FLO is set to \'OIL\' or \'LIQ\'<br>2)  GLR: for the gas fraction being the gas-liquid ratioand should be used if FLO is set to \'OIL\' or \'LIQ\'<br>3)  OGR: for the gas fraction being the oil-gas ratioand should be used if FLO is set to \'GAS\'. | None |
| 1-6 | VFPTYPE | A defined character string that should be defaulted or set equal to THP. | THP |
| 1-7 | ALQ | A defined character string that defines the artificial lift quantity and should be set to one of the following character strings:<br>1)  GRAT: for the artificial lift quantity being the gas lift gas injection rate.<br>2)  IGLR: for the artificial lift quantity being the gas lift gas, injection gas-liquid ratio.<br>3)  TGLR: for the artificial lift quantity being the gas lift gas, total gas-liquid ratio.<br>4)  COMP: for the artificial lift quantity being the compressor power, for a compressor.<br>5)  PUMP: for the artificial lift quantity being the pump rating for a pump.<br>6)  DENO: for oil surface density.<br>7)  DENG: for gas surface density.<br>8)  BEAN: for multi-segment wells choke parameter.<br>9)  \' \': for undefined, that is for no ALQ data.<br>The DENO and DENG options are not supported by OPM Flow.<br>The ALQ parameter is just another variable used to interpolate the outflow pressure based on the inlet pressure, together with the phases flowing through the system. As such, ALQ can represent any parameter; however, the units should be consistent with that used to set the value. For example, if pump speed (Hz) is used to set a well's artificial lift quantity via the [WCONPROD](#__RefHeading___Toc146754_4203985108)(ALQ-WELL) parameter in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, then the ALQ-DATA should represent pump speed in Hz.<br>The default value is \' \' or undefined, that covers the case when the ALQ variable is not entered, except for when gas lift is employed in the model. When gas lift is active then the default value for ALQ is set to GRAT provided:<br>1)  Gas lift optimization is active via the [LIFTOPT](#__RefHeading___Toc118992_332691817) keyword, or<br>2)  The [GLIFTLIM](#__RefHeading___Toc399999_1414963541) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section is used to constrain the total amount of gas lift used within a group, or<br>3)  Gas lift flows are included in the network pressure loss calculations as determined by the [GRUPNET](#__RefHeading___Toc118319_1596574740)(OPTION2), or the [NODEPROP](#__RefHeading___Toc212708_2026549522)(GASLIFT) parameters in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>In addition, if any of the above is true than ALQ must be set to GRAT. | \' \' |
| 1-8 | VFPUNITS | A defined character string that specifies the units system for the VFP table.<br>An error message is output if this is not the same as the model units. | Model<br>units |
| [FIELD](#__RefHeading___Toc71850_2267116897) | [METRIC](#__RefHeading___Toc70639_2267116897) | [LAB](#__RefHeading___Toc72458_2267116897) |  |
| 1-9 | VFPVALUE | A defined character string that defines the type of data in the VFP-DATA vector. This should be set equal to BHP if the vector contains bottom-hole pressure data, or TEMP if the vector contains Tubing Head Temperature (THT) data.<br>OPM Flow only supports the (default) BHP option. | BHP |
| 1-10 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | FLO-DATA | A real positive monotonically increasing vector that defines the numerical values of the flowing phase declared by the FLO variable.<br>The number of entries must greater than two and less than or equal to MXMFLO as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| Liquid: stb<br>Gas: Mscf | Liquid: sm^3^<br>Gas: sm^3^ | Liquid: scc<br>Gas: scc |  |
| 2-2 | / | Record terminated by a "/" | Not Applicable |
| 3-1 | THP-DATA | A real positive monotonically increasing vector that defines the numerical values of the tubing head pressure values.<br>The number of entries must greater than two and less than or equal to MXMTHP as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| psia | barsa | atma |  |
| 3-2 | / | Record terminated by a "/" | Not Applicable |
| 4-1 | WFR-DATA | A real positive monotonically increasing vector that defines the numerical values of the flowing water fraction declared by the WFR variable.<br>The number of entries must greater than two and less than or equal to MXMWFR as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| WOR: stb/stb<br>WCT: stb/stb<br>WGR: stb/Mscf | sm^3^/sm^3^<br>sm^3^/sm^3^<br>sm^3^/sm^3^ | scc/scc<br>scc/scc<br>scc/scc |  |
| 4-2 | / | Record terminated by a "/" | Not Applicable |
| 5-1 | GFR-DATA | A real positive monotonically increasing vector that defines the numerical values of the flowing gas fraction declared by the GFR variable.<br>The number of entries must greater than two and less than or equal to MXMGFR as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| GOR: Mscf/stb<br>GLR: Mscf/stb<br>OGR: stb/Mscf | sm^3^/sm^3^<br>sm^3^/sm^3^<br>sm^3^/sm^3^ | scc/scc<br>scc/scc<br>scc/scc |  |
| 5-2 | / | Record terminated by a "/" | Not Applicable |
| 6-1 | ALQ-DATA | A real positive monotonically increasing vector that defines the numerical values of the artificial lift quantity declared by the ALQ variable.<br>The number of entries must greater than two and less than or equal to MXMALQ as defined on the [VFPPDIMS](#__RefHeading___Toc95111_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| GRAT: Mscf/d<br>IGLR: Mscf/stb<br>TGLR: Mscf/stb<br>DENO: lb/ft^3^<br>DENG: lb/ft^3^<br>BEAN: 1/64 inch | sm^3^/day<br>sm^3^/sm^3^<br>sm^3^/sm^3^<br>kg/m^3^<br>kg/m^3^<br>mm | scc/hour<br>scc/scc<br>scc/scc<br>gm/cc<br>gm/cc<br>mm |  |
| 6-2 | / | Record terminated by a "/" | Not Applicable |
| 7-1 | NTHP | This data record consists of a series of integer values that defines the index of THP, WFR, GFR, ALQ entered via the those records on this keyword.<br>The first index, NTHP, is an integer value that defines the index of THP values entered via the THP-DATA records on this keyword. For example, if THP-DATA is equal to 100, 200, 300 and 350 and NTHP is equal to three then NTHP refers to third entry, that is THP equal to 300. | None |
| NWFR | The second index, NWFR, is an integer value that defines the index of the water fraction values entered via the WFR-DATA records on this keyword. For example, if WFR-DATA is equal to 0.00, 0.25, 0.50 and 0.75 and NWFR is equal to two then NWFR refers to second entry, that is WFR equal to 0.25. | None |  |
| NGFR | The third index, NGFR, is an integer value that defines the index of the gas fraction values entered via the GFR-DATA records on this keyword. For example, if GFR-DATA is equal to 100.0, 200.0, 500.0 and 750.0 and NGFR is equal to three then NGFR refers to third entry, that is GFR equal to 500.0. | None |  |
| NALQ | The fourth and final index entry, NALQ, is an integer value that defines the index of artificial lift values via the ALQ-DATA records on this keyword. For example, if ALQ-DATA is equal to 50, 100, 200 and 300 and NALQ is equal to one then NALQ refers to first entry, that is ALQ equal to 50.<br>The fourth index is then followed by the VFP-DATA, containing either the BHP or THT vector values. | None |  |
| VFP-DATA | VFP-DATA is a real vector of either BHP or THT values for each FLO production rate for the corresponding index value (NTHP, NWFR, NGFR, NALQ) and is then terminated with a"/".<br>The (7-1) record, which consists of the four indices and BHP (or THT) data, is then repeated until all combinations of (NTHP, NWFR, NGFR, NALQ) and the associate BHP (or THT) data has been entered.<br>Note that the VFPVALUE parameter, determines the type of VFP-DATA, that is BHP for bottom-hole pressure, or THT for tubing head temperature. | None |  |
| psia | barsa | atma |  |
| 7-2 | / | Each Index (NTHP, NWFR, NGFR, NALQ. VFP-DATA) data set is terminated by a "/" | Not Applicable |
| Notes:<br>1)  Each [VFPPROD](#__RefHeading___Toc121919_2556401936) table must be entered with a separate [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword that consists of seven records, with entries 1-1 to 1-10 representing record one items and 2-1 to 2-2 representing record number two items, etc., in the "No." column in this table.<br>2)  Each of the records are terminated by a "/" and is explicitly shown in the above rows.<br>3)  There is no keyword terminating "/". |  |  |  |

Table 12.75: VFPPROD Keyword Description

The data for this keyword is generated by an external program and is normally included into the input deck using the [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword as described in section [[CHAPTER 4:](#anchor-2)](#4.GLOBAL SECTION KEYWORDS|outline)[](#4.GLOBAL SECTION KEYWORDS|outline)[[GLOBAL SECTION KEYWORDS](#anchor-2)](#4.GLOBAL SECTION KEYWORDS|outline), as the data can be quite voluminous.

Note that for equivalent two phase runs:

3)  1)  1)  For example oil-water runs with only the [OIL](#__RefHeading___Toc97439_1778172979) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or runs that model dead oil[^1] with a constant solution gas-oil ratio value defined by the [RSCONST](#__RefHeading___Toc138398_332691817) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, then the FLO parameter in must be set to either [OIL](#__RefHeading___Toc97439_1778172979) or LIQ, WFR to either WCT or WOR, and GFR to GOR.

        2)  Gas-water models with only the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, or models that only have dry gas[^2] with a constant condensate-gas ratio defined by the [RVCONST](#__RefHeading___Toc329587_516898843) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, then the FLO parameter in must be set to [GAS](#__RefHeading___Toc38607_2267116897), WFR to WGR, and GFR to OGR.

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define wells and the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword that is used to allocate the [VFPPROD](#__RefHeading___Toc121919_2556401936) tables to specific wells. Note that one [VFPPROD](#__RefHeading___Toc121919_2556401936) table can be allocated to one or more wells, provided the wells in question have a similar trajectory and similar flow characteristics, for example vertical oil wells producing from the same reservoir, or different reservoirs with similar PVT properties.

The [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword is used to enter VFP tables for injection wells or to describe the pressure relationship when the network option is being used. In this case the table describes the pipeline pressure behavior from the HIGHER group (inlet node) to the LOWER group (outlet node) given the current injection conditions.

All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Examples

The following example shows the [VFPPROD](#__RefHeading___Toc121919_2556401936) table for a production gas well and is taken from the Norne OPM Flow model. Here WFR has been set to water-gas ratio and GFR has been set to the oil-gas ratio, and the ALQ value is defaulted.

VFPPROD

\-- Table Datum Depth Rate Type WFR Type GFR Type

\-- \-\-\-\-- \-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

5 2623.39 \'GAS\' \'WGR\' \'OGR\' /

\-- \'GAS\' units - SM3/DAY

50000.0 100000.0 200000.0 400000.0 800000.0

1200000.0 1600000.0 1999999.9 3000000.0 3999999.8

5000000.5 /

\-- \'THP\' units - BARSA

10.00 20.00 40.00 80.00 120.00

150.00 200.00 250.00 /

\-- \'WGR\' units - SM3/SM3

0 1e-9 1e-6 1e-5 0.0001

0.001 0.01 0.1 /

\-- \'OGR\' units - SM3/SM3

1e-7 1e-6 1e-5 0.0001 0.001

0.01 /

\-- \'ALQ\' units -

0 /

1 1 1 1 11.93 12.22 13.35 17.24 27.93

39.83 52.06 64.38 95.20 125.89

156.52

/

1 1 2 1 11.93 12.22 13.35 17.24 27.94

39.84 52.07 64.39 95.21 125.91

156.55

/

...........................................................................................................................................................

...........................................................................................................................................................

8 8 5 1 483.75 511.15 614.09 1044.78 2757.56

5592.55 9528.36 14567.24 32005.79 56375.24

87684

/

8 8 6 1 487.68 516.24 624.74 1075.40 2860.16

5803.92 9880.58 15093.76 33119.59 58297.57

90639

/

The example shows the first two and the last two records of type seven, as the data is too voluminous to be included.

The next example below shows an example oil producing well [VFPPROD](#__RefHeading___Toc121919_2556401936), again taken from Norne OPM Flow model. Here WFR has been set to water cut and GFR has been set to the gas-oil ratio, and the ALQ value is defaulted.

VFPPROD

\-- Table Datum Depth Rate Type WFR Type GFR Type TAB Type

\-- \-\-\-\-- \-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

\-- 37 2641.02 \'LIQ\' \'WCT\' \'GOR\' /

\-- Prosper files are corrected from RKB to MSL depth. lmarr

\-- Table Datum Depth Rate Type WFR Type GFR Type TAB Type

\-- \-\-\-\-- \-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

37 2617.02 \'LIQ\' \'WCT\' \'GOR\' /

\-- \'LIQ\' units - SM3/DAY

200.0 500.0 1000.0 1500.0 2000.0

2500.0 3000.0 3500.0 4000.0 4500.0

5000.0 5500.0 6000.0 6500.0 7000.0

7500.0 8000.0 10000.0 14000.0 /

\-- \'THP\' units - BARSA

21.01 51.01 61.01 81.01 101.01

121.01 141.01 161.01 181.01 201.01 /

\-- \'WCT\' units - FRACTION

0 0.1 0.2 0.3 0.4

0.5 0.6 0.7 0.8 1 /

\-- \'GOR\' units - SM3/SM3

90 100 150 200 500

1000 2000 /

\-- \'ALQ\' units -

0 /

1 1 1 1 160.82 136.70 119.79 115.86 117.38

121.16 126.08 131.56 137.48 143.74

150.29 157.07 164.02 171.07 178.13

185.11 192.09 220.38 280.86

/

1 1 2 1 155.63 129.40 112.32 108.64 110.44

114.74 120.15 126.09 132.47 139.05

146.02 153.41 160.67 167.91 175.13

182.34 189.55 218.81 281.02

/

...........................................................................................................................................................

...........................................................................................................................................................

10 10 6 1 439.30 437.95 437.53 437.79 438.39

439.26 440.36 441.67 443.19 444.92

446.85 448.99 451.32 453.85 456.58

459.51 462.64 477.11 515.47

/

10 10 7 1 439.30 437.95 437.53 437.79 438.39

439.26 440.36 441.67 443.19 444.92

446.85 448.99 451.32 453.85 456.58

459.51 462.64 477.11 515.47

/

The example shows the first two and the last two records of type seven, as the data is too voluminous to be included.

[^1]: "Dead" oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.

[^2]: Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR\'s greater than 100,000 scf/stb or 18,000 Sm3/m3.
