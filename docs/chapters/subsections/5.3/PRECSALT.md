### PRECSALT -- Activate the OPM Flow Salt Precipitation Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the OPM Flow Salt Precipitation model that accounts for salt precipitating out of the water phase when the water is being vaporized into the gas phase and the dissolved salt reaches the solubility limit as the pressure in the reservoir is being depleted (see the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section). This facility is an extension to the standard Brine model, and as such the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) must also be present in the input deck. In general, if the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword has been activated in the input deck then the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword should also be activated. The keyword should only be used if both water and gas phases are active in the model.

If the keyword is present in the input deck then the [SALTSOL](#__RefHeading___Toc681417_1466963378) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section also needs to be present in the input deck to define the salt solubility. In addition, either the [SALTPVD](#__RefHeading___Toc613572_1667959253) or [SALTP](#__RefHeading___Toc486358_4287353749) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section should be used to define the initial salt precipitated saturation.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The first part of the example shows the keywords for the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

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

\-- OIL PHASE IS PRESENT IN THE RUN

\--

OIL

\--

\-- WATER PHASE IS PRESENT IN THE RUN

\--

WATER

\--

\-- GAS PHASE IS PRESENT IN THE RUN

\--

GAS

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN

\--

DISGAS

\--

\-- ACTIVATE STANDARD BRINE MODEL IN THE RUN

\--

BRINE

\--

\-- ACTIVATE THE OPM FLOW SALT PRECIPITATION MODEL (OPM FLOW KEYWORD)

\--

PRECSALT

The above example declares that the oil, water, gas, dissolved gas, and brine phases are present in the model, and activates the Brine ([BRINE](#__RefHeading___Toc162083_289573908) keyword) and Salt Precipitation ([PRECSALT](#__RefHeading___Toc332782_3149455253) keyword) models.

The second part of the example shows the additional PVT fluid keywords require for the Salt Precipitation model in the [PROPS](#__RefHeading___Toc39329_784232322) section. Note that in addition to the Salt Precipitation model specific keywords, the standard [DENSITY](#__RefHeading___Toc45799_719036256) (or [GRAVITY](#__RefHeading___Toc45801_719036256)), [PVDG](#__RefHeading___Toc104056_57619843), and [PVTO](#__RefHeading___Toc104062_57619843) keywords are required.

\-- ==============================================================================

\--

\-- PROPS SECTION

\--

\-- ==============================================================================

PROPS

\--

\-- WATER SALT PVT TABLE

\--

PVTWSALT

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.000 / REFERENCE DATA

\--

\-- SALTCONC BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.0 3.0E-6 1.0 1.0E-6

10.0 0.8 3.0E-6 1.0 1.0E-6 / SALT CONCENTRATION

\--

\-- SET SALT SOLUBILITY LIMIT FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALTSOL

\-- MAX SALT

\-- SALTSOL DENSITY

0.500 135.46867445023383 /

In addition, to the above the [PERMFACT](#__RefHeading___Toc712146_1466963378) keyword may be used to account for the reduction in porosity and permeability due to salt precipitating into the pore space. Again, in addition to the Salt Precipitation model specific keywords, the standard [ROCK](#__RefHeading___Toc45809_719036256), [SGOF](#__RefHeading___Toc106870_335817223), and [SWOF](#__RefHeading___Toc45811_7190362561) keywords are required.

\--

\-- PERMEABILITY FACTOR REDUCTION DUE TO SALT (OPM FLOW KEYWORD)

\--

PERMFACT

\-- PORO PERM

\-- FACTOR FACTOR

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 0.000

0.4 0.005

0.6 0.010

0.9 0.100

1.0 1.000 / TABLE NO. 01

/

In order to initialize the model in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, apart from the standard equilibration keywords, the following Salt Precipitation model specific keywords should be included.

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- PRECIPITATED SALT VOLUME FRACTION VERSUS DEPTH (OPM FLOW KEYWORD)

\--

\-- DEPTH SALTPSAT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

SALTPVD

8300.0 0.010

8450.0 0.010 / SALT VS DEPTH EQUIL REGN 01

\--

\-- DEPTH SALT-1 SALT-2 SALT-3

\-- SALTCON SALTCON SALTCON

\-- \-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

SALTVD

8300.0 0.500

8450.0 0.500 / SALT VS DEPTH EQUIL REGN 01

Note that OPM Flow does not support Multi-Component Brine model, thus there should only one column of salt concentrations.

Finally, in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, one may optionally one can add the injections well\'s injection salt concentrations, as shown below.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- DEFINE WATER INJECTION WELL SALT CONCENTRATIONS

\--

\-- WELL SALT-1 SALT-2 SALT-3 SALT-4

\-- NAME SALTCON SALTCON SALTCON SALTCON

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

WSALT

\'INJ\' 0.0000 /

/

Normally, with this option one would also include vaporized water via the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, as well as the [PVTGW](#__RefHeading___Toc355649_3149455253) keyword to define gas PVT properties for dry gas, or the [PVTGWO](#__RefHeading___Toc356776_4176551521) keyword that declares the gas PVT properties for wet gas. Both keywords are in the [PROPS](#__RefHeading___Toc39329_784232322) section. The [RWGSALT](#__RefHeading___Toc304264_1667959253) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, may be used to define the relationship of water vaporization versus pressure and salt concentration. Again, the keyword is in the [PROPS](#__RefHeading___Toc39329_784232322) section. Secondly, in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, the [RVW](#__RefHeading___Toc537756_4287353749) keyword can be used to set the initial equilibration vaporized water in gas ratio values for all grid cells in the model for Enumeration Initialization, or the [RVWVD](#__RefHeading___Toc137367_13175472131) keyword that declares the vaporized water-gas ratio (Rvw) versus depth tables for each equilibration region, for Equilibrium Initialization.
