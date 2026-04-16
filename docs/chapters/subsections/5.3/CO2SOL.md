### CO2SOL -- Activate Dissolved CO2 in the Water Phase

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [CO2SOL](#REF_HEADING_KEYWORD_CO2SOL) keyword activates dissolved carbon dioxide (CO~2~) in the water phase, where CO~2~ is represented by the [SOLVENT](#__RefHeading___Toc62787_1778172979) pseudo component, using the simulator's CO~2~-Brine PVT model. This keyword is a compositional keyword in the commercial simulator but has been implemented in OPM Flow's black-oil model.

The [CO2SOL](#REF_HEADING_KEYWORD_CO2SOL) keyword can be used when modelling CO~2~ injection in depleted hydrocarbon reservoirs. See also the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section which can be used when modelling CO~2~ injection in saline aquifers.

The CO~2~-Brine PVT model computes the PVT properties such as density, viscosity, and enthalpy internally as functions of pressure, temperature, and composition by using analytic correlations and models from the literature rather than by interpolation of tabulated values in the input deck. These values are transformed to the standard black-oil equivalent PVT tables internally by the simulator. A full description of the underlying PVT models is described by Sandve et al.[^1]. Note that the CO~2~-Brine PVT properties depend on the temperature and salinity and these must therefore be entered in the [PROPS](#__RefHeading___Toc39329_784232322) section. The reservoir temperature can be defined using, e.g., the [RTEMP](#__RefHeading___Toc111816_2939291539) keyword. Region based salinity can be provided using the [SALINITY](#__RefHeading___Toc405185_1616145207) keyword.

The [CO2SOL](#REF_HEADING_KEYWORD_CO2SOL) keyword must be used together with the [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword activates the four component black-oil model: oil, water and gas, plus a solvent (in this case CO~2~).

The [DISGASW](#__RefHeading___Toc39767_22671168971) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section can be used to model dissolution of CO~2~ in the Brine. Note that hydrocarbon gas is not allowed to dissolve in the Brine (this is considered a reasonable assumption for most hydrocarbon gases).

The hydrocarbon reservoir fluid properties should be set up as normal apart from the water PVT properties, which will be defined by the simulators' CO~2~-Brine PVT model, so the water PVT keywords (e.g. [PVTW](#__RefHeading___Toc2086106_3315222525)) are not required. The CO~2~ PVT properties will also be defined by the CO~2~-Brine PVT model so the solvent PVT keywords (e.g. [SDENSITY](#__RefHeading___Toc121471_83452205), [PVTSOL](#__RefHeading___Toc414279_1093985484)) are also not required.

The oil-water and gas-water saturation functions should be set up as normal. The CO~2~ and gas miscible relative permeability tables should be defined using the [SSFN](#__RefHeading___Toc106880_335817223) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

The initial CO~2~ saturations in the model can be specified by enumeration using the [SSOL](#__RefHeading___Toc210160_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

The CO~2~ fraction in a well's injection stream can be defined using the [WSOLVENT](#__RefHeading___Toc121647_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The example shows the usage of [CO2SOL](#REF_HEADING_KEYWORD_CO2SOL) to model CO~2~ injection in a live-oil reservoir. The [RUNSPEC](#__RefHeading___Toc55591_1778172979) section includes the [CO2SOL](#REF_HEADING_KEYWORD_CO2SOL) keyword, which activates dissolved carbon dioxide (CO~2~) in the water phase. The [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword activates the solvent pseudo component, which represents CO~2~. The [DISGASW](#__RefHeading___Toc39767_22671168971) keyword has been used to activate dissolved CO~2~ in the brine.

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

\-- ACTIVATE DISSOLVED CO2 IN WATER (OPM FLOW KEYWORD)

\--

CO2SOL

\--

\-- SOLVENT PHASE IS PRESENT IN THE RUN

\--

SOLVENT

\--

\-- DISSOLVED CO2 IN WATER IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

DISGASW

The second part of the example covers the additional data required in the [PROPS](#__RefHeading___Toc39329_784232322) section, in which the CO~2~-gas miscible relative permeabilities are defined using the [SSFN](#__RefHeading___Toc106880_335817223) keyword. The initial temperature and salinity are defined using the [RTEMP](#__RefHeading___Toc111816_2939291539) and [SALINITY](#__RefHeading___Toc405185_1616145207) keywords. The oil and gas PVT properties should be defined in the normal way. No water PVT data is required.

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

\-- SET SALINITY FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALINITY

0.7 /

\--

\-- SOLVENT RELATIVE PERMEABILITY TABLES

\--

SSFN

\-- SGAS KRGT KRST

\-- FRAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0000 0.0000 0.0000

1.0000 1.0000 1.0000 /

The third part of the example covers initialising the model in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. Here the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword is used as normal to equilibrate the oil, gas and water phases, and the [SSOL](#__RefHeading___Toc210160_2884651453) keyword to specify that there is initially no CO~2~ present in the gas phase.

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DATUM DATUM OWC PCOW GOC PCGO RS RV N E300 RVW

\-- DEPTH PRESS DEPTH \-\-\-- DEPTH \-\-\-- OPT OPT OPT OPT OPT

EQUIL

2000.0 200.0 1900.0 0.00 2000.0 0.00 1\* 1\* 1\* 2\* 1\* /

\--

\-- DEFINE INITIAL EQUILIBRATION SOLVENT SAT VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SSOL

30000\*0.0 /

For the summary section, the CO~2~ storage quantity can be tracked using the solvent injection and production volumes as shown below.

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

\-- FIELD SOLVENT INJECTION RATE

FNIR

\--

\-- FIELD SOLVENT PRODUCTION RATE

FNPR

\--

\-- FIELD SOLVENT INJECTION TOTAL

FNIT

\--

\-- FIELD SOLVENT PRODUCTION TOTAL

FNPT

The final part of the example covers the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The [WSOLVENT](#__RefHeading___Toc121647_2412586160) keyword is used to specify the injected solvent fraction (in this case pure CO~2~).

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- RESTART CONTROL BASIC = 1 (LAST REPORT TIME ONLY)

\--

RPTRST

\'BASIC=1\' \'ALLPROPS\' /

\--

\-- DEFINE GAS INJECTION WELL SOLVENT FRACTION

\--

\-- WELL SOLVENT

\-- NAME FRACTION

\-- \-\-\-\-\-\-\--

WSOLVENT

GI01 1.0000 /

/

[^1]: Tor Harald Sandve1, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.
