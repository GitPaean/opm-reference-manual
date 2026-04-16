### PVZG -- Gas PVT Properties for Dry Gas (Z-Factor)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[PVZG](#__RefHeading___Toc350298_501926209) defines the gas PVT properties for dry gas[^1] via the gas compressibility factor (z-factor), instead of the gas formation volume factor. If the gas has a constant and uniform vaporized oil concentration, Condensate-Gas Ratio ("CGR"), and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the [OIL](#__RefHeading___Toc97439_1778172979) and [VAPOIL](#__RefHeading___Toc56610_2267116897) keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the gas as a dry gas, and defining a constant Rv (CGR) value with keyword [RVCONST](#__RefHeading___Toc329587_516898843) or [RVCONSTT](#__RefHeading___Toc138400_3326918171) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run with as a dry gas problem with no active oil (condensate) phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > No.                                                                                                                                                                                                                                                                                                                                                                                 | > Name                                          | > Description                                                                                                      | > Default        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > Field                                                                                                                                                                                                                                                                                                                                                                               | > Metric                                        | > Laboratory                                                                                                       |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > 1-1                                                                                                                                                                                                                                                                                                                                                                                 | > [RTEMP](#__RefHeading___Toc111816_2939291539) | > Single real positive value that defines the reservoir temperature for the data in the following records.         |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > ^o^F                                                                                                                                                                                                                                                                                                                                                                                | > ^o^C                                          | > ^o^C                                                                                                             |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > 1-2                                                                                                                                                                                                                                                                                                                                                                                 | > /                                             | > Record terminated by a "/"                                                                                       | > Not Applicable |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > 2-1                                                                                                                                                                                                                                                                                                                                                                                 | > PRESS                                         | > A columnar vector of real monotonically increasing down the column values that defines the gas phase pressure.   | > None           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > psia                                                                                                                                                                                                                                                                                                                                                                                | > barsa                                         | > atma                                                                                                             |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > 2-2                                                                                                                                                                                                                                                                                                                                                                                 | > GZFAC                                         | > A columnar vector of real values that defines the corresponding gas phase z-factor at the given pressure, PRESS. | > None           |
|                                                                                                                                                                                                                                                                                                                                                                                       |                                                 |                                                                                                                    |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > dimensionless                                                                                                                                                                                                                                                                                                                                                                       | > dimensionless                                 | > dimensionless                                                                                                    |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > 2-3                                                                                                                                                                                                                                                                                                                                                                                 | > GVISC                                         | > A columnar vector of real increasing down the column values that defines the corresponding gas phase viscosity.  | > None           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > cP                                                                                                                                                                                                                                                                                                                                                                                  | > cP                                            | > cP                                                                                                               |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+
| > Notes:                                                                                                                                                                                                                                                                                                                                                                              |                                                 |                                                                                                                    |                  |
|                                                                                                                                                                                                                                                                                                                                                                                       |                                                 |                                                                                                                    |                  |
| 1)  The keyword is followed by NTPVT data sets as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and each data set consists of two records, with items 1-1 to 1-2 representing record one items and 2-1 to 2-3 representing record number two items, etc., in the "No." column in this table.    |                                                 |                                                                                                                    |                  |
|                                                                                                                                                                                                                                                                                                                                                                                       |                                                 |                                                                                                                    |                  |
| 2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.                                                                                                                                                                 |                                                 |                                                                                                                    |                  |
|                                                                                                                                                                                                                                                                                                                                                                                       |                                                 |                                                                                                                    |                  |
| 3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                                                                                                                                                                                                                                 |                                                 |                                                                                                                    |                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+------------------+

Table 8.124: PVZG Keyword Description

See also the [RVCONST](#__RefHeading___Toc329587_516898843) and [RVCONSTT](#__RefHeading___Toc138400_3326918171) keywords to define the constant Rv for dry gas.

The ideal gas law provides a relationship between the pressure, the temperature and the specific volume of an ideal gas (pure component). This relationship is modified by use of a compressibility factor, Z[^2], to account for deviations, from ideal, to the behavior of real gases. The PVT relation for a real gas can be defined by:

As the gas formation volume factor is used to relate the volume of gas, as measured at reservoir conditions, to the volume of gas as measured at standard conditions (60 ^o^F and 14.7 psia, or 15 ^o^C and 101.325 kPa). This gas property is then defined as the actual volume occupied by a certain amount of gas at a specified pressure and temperature, divided by the same amount of gas at standard conditions. Thus, using the above equation one can obtain the gas volumes at reservoir and standard conditions, i.e.

Thus the gas formation volume factor can be expressed as:

And substituting equation and into we obtain

Incorporating standard pressure and temperature values gives in SI units:

or in field units:

Where,

= gas formation volume factor (scf /rcft or Sm^3^/m^3^)

= pressure (psia or kPa)

= pressure standard conditions (psia or kPa )

= initial reservoir pressure (psia or kPa)

= volume (ft^3^ or m^3^)

= absolute temperature (^o^R or K)

= temperature at standard conditions (^o^R or K)

= initial reservoir temperature (^o^R or K)

= gas constant (10.73 or 8.314)

R[TEMP](#__RefHeading___Toc146397_3544483072) on this keyword is the in the above equations and is PRESS columnar vector.

#### Example

\-\--

\-- GAS PVT TABLE USING GAS Z-FACTOR

\--

PVZG

\-- RESERVOIR TEMPERATURE FOR Z TO BG CONVERSION

\--

180.0 /

\--

\-- PRES ZG VISC

\-- PSIA DIMLESS CPOISE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\--

14.7 0.998970 0.0130

250.0 0.976260 0.0131

500.0 0.954790 0.0134

750.0 0.932050 0.0137

1000.0 0.912990 0.0142

1250.0 0.896320 0.0147

1500.0 0.881610 0.0152

1750.0 0.870830 0.0159

2000.0 0.863130 0.0166

2250.0 0.858920 0.0173

2500.0 0.857800 0.0181

2750.0 0.860430 0.0189

3000.0 0.866440 0.0197

3250.0 0.874980 0.0206

3500.0 0.885470 0.0214

3750.0 0.898350 0.0223

4000.0 1.025120 0.0277 / TABLE NO 01 \--

\-- GAS PVT TABLE USING GAS Z-FACTOR

\--

PVZG

\-- RESERVOIR TEMPERATURE FOR Z TO BG CONVERSION

\--

180.0 /

\--

\-- PRES ZG VISC

\-- PSIA DIMLESS CPOISE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\--

14.7 0.998970 0.0130

250.0 0.976260 0.0131

500.0 0.954790 0.0134

750.0 0.932050 0.0137

1000.0 0.912990 0.0142

1250.0 0.896320 0.0147

1500.0 0.881610 0.0152

1750.0 0.870830 0.0159

2000.0 0.863130 0.0166

2250.0 0.858920 0.0173

2500.0 0.857800 0.0181

2750.0 0.860430 0.0189

3000.0 0.866440 0.0197

3250.0 0.874980 0.0206

3500.0 0.885470 0.0214

3750.0 0.898350 0.0223

4000.0 1.025120 0.0277 / TABLE NO 01

The above example defines two dry [PVZG](#__RefHeading___Toc350298_501926209) tables assuming NTPVT equals two and NPPVT is greater than or equal to 17 on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. There is no terminating "/" for this keyword.

[^1]: Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR\'s greater than 100,000 scf/stb or 18,000 Sm3/m3.

[^2]: Standing, M. B.:" Volumetric and Phase Behaviour of Oil Field Hydrocarbon Systems", Renihold Publishing Corp., New York City (1952).
