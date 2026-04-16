### CO2STORE -- Activate the CO2 Storage Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword activates the carbon dioxide (CO~2~) storage model for the run to account for both carbon dioxide and water phase solubility, via the simulator's CO~2~-Brine PVT model. This keyword is a compositional keyword in the commercial simulator but has been implemented in OPM Flow's black-oil model.

The CO~2~-Brine PVT model computes the PVT properties such as density, viscosity, and enthalpy internally as functions of pressure, temperature, and composition by using analytic correlations and models from the literature rather than by interpolation from tabulated values. These values are transformed to the standard black-oil equivalent PVT tables internally by the simulator. A full description of the underlying PVT models is described by Sandve et al.[^1]. This means that the normal PVT keywords like [DENSITY](#__RefHeading___Toc45799_719036256), [PVTO](#__RefHeading___Toc104062_57619843), [PVDG](#__RefHeading___Toc104056_57619843) etc. are not required by OPM Flow when this model is activated, and if entered will be ignored by the simulator. Note that the CO~2~-Brine PVT properties depend on the temperature and salinity and these must therefore be entered in the [PROPS](#__RefHeading___Toc39329_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections. The reservoir temperature can be defined using, e.g., the [RTEMP](#__RefHeading___Toc111816_2939291539) keyword. Region based salinity can be provided using the [SALINITY](#__RefHeading___Toc405185_1616145207) keyword.

The [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword must be used together with either: (1) the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords (or alternatively the [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) keyword), or (2) the [GAS](#__RefHeading___Toc38607_2267116897) and [OIL](#__RefHeading___Toc97439_1778172979) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. It is recommended that the standard method option (1) is used.

The [DISGASW](#__RefHeading___Toc39767_22671168971) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section can be used with option (1) to model dissolution of CO~2~ in the Brine.

Option (1) has the advantage that it can be used with the [VAPWAT](#__RefHeading___Toc317543_3149455253) and [PRECSALT](#__RefHeading___Toc332782_3149455253) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to model the impact of both vaporization of residual water and salt precipitation in the near wellbore region on injectivity of CO~2~ injection wells.

In option (1), the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) (or [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1)) keywords declare that the gas and water phases are present in the model. When the [CO2STORE](#__RefHeading___Toc387968_1616145207) option is used the water phase represents the brine and the gas phase represents CO~2~. Note that the input and output keywords need to be consistent with this assumption, e.g., [GSF](#__RefHeading___Toc524656_3603161511) (gas saturation function) and [WSF](#__RefHeading___Toc524656_3603161511 Copy 1) (water saturation function) should be used for the CO~2~-Brine relative permeability, etc.

Although, the [DISGAS](#__RefHeading___Toc39767_2267116897) and [VAPOIL](#__RefHeading___Toc56610_2267116897) keywords can be used with option (2) to model CO~2~ dissolution and water vaporization, salt precipitation is not supported with option (2).

In option (2), the [GAS](#__RefHeading___Toc38607_2267116897) and [OIL](#__RefHeading___Toc97439_1778172979) keywords declare that the gas and oil phases are present in the model. Internally when [CO2STORE](#__RefHeading___Toc387968_1616145207) is used the oil phase refers to the brine and the gas phase to CO~2~. Again, the input and output keywords need to be consistent with this assumption, e.g., [SGOF](#__RefHeading___Toc106870_335817223) (gas-oil relative permeability) is used for the CO~2~-Brine relative permeability, FOIP (Field Oil-In-Place) shows the total amount of brine in the reservoir, etc.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Examples

The first example shows the standard usage of [CO2STORE](#__RefHeading___Toc387968_1616145207) with Option (1) the Gas-Water model ([GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1)). Here we also activate the dissolved gas in water ([DISGASW](#__RefHeading___Toc39767_22671168971)) and vaporized water in gas ([VAPWAT](#__RefHeading___Toc317543_3149455253)) options in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- FLUID TYPES AND TRACER OPTIONS

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)

\--

CO2STORE

\--

\-- ACTIVATE GAS-WATER THE MODEL (OPM FLOW KEYWORD)

\--

GASWAT

\--

\-- DISSOLVED GAS IN WATER IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

DISGASW

\--

\-- VAPORIZED WATER IN DRY/WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

VAPWAT

The second part of the example covers the data required for the [PROPS](#__RefHeading___Toc39329_784232322) section, in which the two-phase relative permeability functions are set using [GSF](#__RefHeading___Toc524656_3603161511) and [WSF](#__RefHeading___Toc524656_3603161511 Copy 1) keywords.

\-- ==============================================================================

\--

\-- PROPS SECTION

\--

\-- ==============================================================================

PROPS

\--

\-- RESERVOIR

\-- TEMPERATURE

\-- \-\-\-\-\-\-\-\-\-\--

RTEMP

80.0 / RESERVOIR TEMP

\--

\-- ROCK COMPRESSIBILITY

\--

\-- REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE

\--

\-- REF PRES CF

\-- BARSA 1/BARSA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

ROCK

200.0 5.0E-05 / ROCK COMPRESSIBILITY

\--

\-- GAS RELATIVE PERMEABILITY TABLES (OPM FLOW KEYWORD)

\--

GSF

\-- SGAS KRG PCGW

\-- FRAC PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.000 0.000 0.0

0.080 0.001 0.0

0.170 0.010 0.0

0.350 0.050 0.0

0.530 0.200 0.0

0.620 0.350 0.0

0.650 0.390 0.0

0.710 0.560 0.0

0.800 1.000 0.0 / TABLE NO. 01

\--

\-- WATER RELATIVE PERMEABILITY TABLES (OPM FLOW KEYWORD)

\--

WSF

\-- SWAT KRW

\-- FRAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.200 0.0000

0.400 0.1000

0.800 0.5000

1.000 1.0000 / TABLE NO. 01

\--

\-- SET SALINITY FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALINITY

0.7 /

No other data is required to define the fluid and rock properties in the [PROPS](#__RefHeading___Toc39329_784232322) section as the data is generated from internal analytic correlations and models by the simulator. Finally, note that units for salinity are to the 10^-3^, thus for metric units we have 10^-3^ x kg-M/kg.

The third part of the example covers initializing the model in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. Here we set the [EQUIL](#__RefHeading___Toc135617_1317547213)(EQLOPT6) parameter equal to one, to use table number one of the [RVWVD](#__RefHeading___Toc137367_13175472131) keyword, in order to set the vaporized water versus depth distribution for the model.

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- SYSTEM IS SATURATED WITH WATER

\--

\-- DATUM DATUM OWC PCOW GOC PCGO RS RV N E300 RVW

\-- DEPTH PRESS DEPTH \-\-\-- DEPTH \-\-\-- OPT OPT OPT OPT OPT

EQUIL

2000.0 200.0 1800.0 0.00 1800.0 0.00 1\* 1\* 1\* 2\* 1 /

\--

\-- WATER VAPOR RATIO VS DEPTH (OPM FLOW KEYWORD)

\--

\-- DEPTH RVW

\-- STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RVWVD

1000.0 0.000

3000.0 0.000 / RVW VS DEPTH EQUIL REGN 01

In the [SUMMARY](#__RefHeading___Toc43949_784232322) section, the simulator supports summary vectors specific to CO~2~ storage (see Section [11.1.12 Option Specific Variables - CO2STORE/H2STORE Model](#__RefHeading___Toc614364_2141070512)) including those shown below.

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT STANDARD SUMMARY VARIABLE VECTORS TO FILE

\--

ALL

\--

\-- FIELD CO2 DISOLVED IN WATER PHASE

FWCD

\--

\-- FIELD CO2 TRAPPED IN GAS PHASE

FGCDI

\--

\-- FIELD CO2 MOBILE IN GAS PHASE

FGCDM

The final part of the example covers the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The standard [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword is used to set the gas injection rate, in this case 100,000 sm^3^/day of CO~2~.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- RESTART CONTROL BASIC (LAST=1, ALL=2, YEARLY=4, MONTHLY=5, TSTEP=6)

\--

RPTRST

\'BASIC=2\' ALLPROPS TEMP RSWSAT RVWSAT /

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW OPEN CROSS PVT

\-- NAME NAME I J DEPTH FLUID AREA EQUANS SHUT FLOW TABLE

WELSPECS

INJ1 \'G1\' 25 25 1\* GAS /

/

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

INJ1 25 25 1 10 OPEN 1\* 1\* 0.3 /

/

\--

\-- WELL INJECTION CONTROLS

\--

\-- WELL FLUID OPEN/ CNTL SURF RESV BHP THP VFP

\-- NAME TYPE SHUT MODE RATE RATE PRES PRES TABLE

WCONINJE

INJ1 GAS OPEN RATE 100000 1\* 300 /

/

\--

\-- ADVANCE SIMULATION BY REPORTING TIME

\--

TSTEP

36\*30.4375

/

Note in order to get the liquid phase mole fractions of CO~2~, that is, the mole fractions of CO~2~ in the water phase (XMFCO2), and the vapor phase mole fractions (YMFWAT) to the restart file, one must use the command line parameter enable-opm-rst-file set equal to true.

The second example shows how to use [CO2STORE](#__RefHeading___Toc387968_1616145207) with the alternative option (2). The example below declares that the carbon dioxide storage model is active for the run to account for both carbon dioxide and water phase solubility using OPM Flow's CO~2~-Brine PVT model. Option (2) is used where the [OIL](#__RefHeading___Toc97439_1778172979) phase refers to the brine and the [GAS](#__RefHeading___Toc38607_2267116897) phase to CO~2~.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-- FLUID TYPES AND TRACER OPTIONS

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \--

\-- ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)

\--

CO2STORE

\--

\-- OIL PHASE IS PRESENT IN THE RUN BUT IS THE BRINE PHASE FOR CO2STORE

\--

OIL

\--

\-- GAS PHASE IS PRESENT IN THE RUN BUT IS THE CO2 PHASE FOR CO2STORE

\--

GAS

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN (CO2 IN BRINE)

\--

DISGAS

\--

\-- VAPORIZED OIL IN WET GAS IS PRESENT IN THE RUN (WATER IN CO2)

\--

VAPOIL

The second part of the example covers the data required for the [PROPS](#__RefHeading___Toc39329_784232322) section, in which the input keywords need to be consistent with the [OIL](#__RefHeading___Toc97439_1778172979) phase referring to the Brine and the [GAS](#__RefHeading___Toc38607_2267116897) to CO~2~; that is [SGOF](#__RefHeading___Toc106870_335817223) (gas-oil relative permeability) is used to define the CO~2~-Brine relative permeability table.

\-- ==============================================================================

\--

\-- PROPS SECTION

\--

\-- ==============================================================================

PROPS

\--

\-- RESERVOIR

\-- TEMPERATURE

\-- \-\-\-\-\-\-\-\-\-\--

RTEMP

90.0 / RESERVOIR TEMPERATURE

\--

\-- ROCK COMPRESSIBILITY

\--

\-- REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE

\--

\-- REF PRES CF

\-- BARSA 1/BARSA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

ROCK

200.0 5.0E-05 / ROCK COMPRESSIBILITY

\--

\-- GAS-OIL RELATIVE PERMEABILITY TABLES (SGOF) -- CO2STORE PHASES

SGOF

\-- SG KRG KROG PCOG

\-- FRAC PSIA

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.00000 0.000000 1.00000 0.0000

1.00000 1.000000 0.00000 0.0000 / TABLE No. 01

\--

\-- SET SALINITY FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALINITY

0.7 /

The third part of the example covers initializing the model in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. Here we set the [EQUIL](#__RefHeading___Toc135617_1317547213)(EQLOPT1 and EQLOPT2) parameters equal to one, to use table number one of the [RSVD](#__RefHeading___Toc137363_1317547213) and [RVVD](#__RefHeading___Toc137367_1317547213) keywords, in order to set the initial dissolved CO~2~ and vaporized water versus depth distribution for the model.

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- SYSTEM IS SATURATED WITH OIL (BRINE)

\--

\-- DATUM DATUM OWC PCOW GOC PCGO RS RV N E300 RVW

\-- DEPTH PRESS DEPTH \-\-\-- DEPTH \-\-\-- OPT OPT OPT OPT OPT

EQUIL

2000.0 200.0 2200.0 0.00 1800.0 0.00 1 1 1\* 2\* 1\* /

\--

\-- DEPTH RS

\-- MSCF/STB

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RSVD

1000.0 0.000

3000.0 0.000 /

\--

\-- DEPTH RVW

\-- STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RVVD

1000.0 0.000

3000.0 0.000 /

See also the [DRSDTCON](#__RefHeading___Toc481925_1297399298) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section for details of how to control convective dissolution of carbon dioxide into the in-situ brine.

[^1]: Tor Harald Sandve1, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.
