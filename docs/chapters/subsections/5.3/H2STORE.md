### H2STORE -- Activate the H2 Storage Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The H2STORE keyword activates the hydrogen (H~2~) storage model for the run to account for both hydrogen and water phase solubility. H2STORE is similar to CO2STORE, which activates the carbon dioxide (CO~2~) storage model.

The H~2~-Brine PVT model computes the PVT properties such as density, viscosity, and enthalpy internally as functions of pressure, temperature, and composition by using analytic correlations and models from the literature rather than by interpolation from tabulated values. These values are transformed to the standard black-oil equivalent PVT tables internally by the simulator. Dissolved hydrogen in brine is modeled using Li et al.[^1]. Hydrogen gas density was modeled using Leachman et al.[^2]. Other properties are modeled the same way as in CO2STORE but modified for hydrogen-brine (a similar approach was recently reported by Raad et al.[^3]). A full description of the underlying PVT models used by CO2STORE is described by Sandve et al.[^4]. This means that the normal PVT keywords like DENSITY, PVTO, PVDG etc. are not required by OPM Flow when this model is activated, and if entered will be ignored by the simulator. Note that the H~2~-Brine PVT properties depend on the temperature and salinity and these must therefore be entered in the PROPS or SOLUTION sections. The reservoir temperature can be defined using, e.g., the RTEMP keyword. Region based salinity can be provided using the SALINITY keyword.

The H2STORE keyword must be used with either: (1) the GAS and WATER keywords (or alternatively the GASWAT keyword), or (2) the GAS and OIL keywords in the RUNSPEC section. It is recommended that the standard option (1) is used.

The DISGASW keyword can also be used with option (1) to model dissolution of H~2~ in the Brine.

Option (1) has the advantage that it can be used with the VAPWAT and PRECSALT keywords to model the impact of both vaporization of residual water and salt precipitation in the near wellbore region on injectivity of H~2~ injection wells.

In option (1), the GAS and WATER (or GASWAT) keywords declare that the gas and water phases are present in the model. When the H2STORE option is used the water phase represents the brine and the gas phase represents H~2~. Note that the input and output keywords need to be consistent with this assumption, e.g., GSF (gas saturation function) and WSF (water saturation function) should be used for the H~2~-Brine relative permeability, etc.

Although, the DISGAS and VAPOIL keywords can be used with option (2) to model water vaporization and H~2~ dissolution, salt precipitation is not currently supported with option (2).

In option (2), the GAS and OIL keywords declare that the gas and oil phases are present in the model. Internally when H2STORE is used the oil phase refers to the brine and the gas phase to H~2~. Again, the input and output keywords need to be consistent with this assumption, e.g., SGOF (gas-oil relative permeability) is used for the H~2~-Brine relative permeability, FOIP (Field Oil-In-Place) shows the total amount of brine in the reservoir, etc.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Examples

The first example shows the standard useage of H2STORE with Option (1) the Gas-Water model (GASWAT). Here we also activate the dissolved gas in water (DISGASW) and vaporized water in gas (VAPWAT) options.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-- FLUID TYPES AND TRACER OPTIONS

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- ACTIVATE H2 STORAGE IN THE MODEL (OPM FLOW H2 STORAGE KEYWORD)

\--

H2STORE

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

The second part of the example covers the data required for the PROPS section, in which the two-phase relative permeability functions are set using GSF and WSF keywords.

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

No other data is required to define the fluid and rock properties in the PROPS section as the data is generated from internal analytic correlations and models by the simulator. Finally, note that units for salinity are to the 10^-3^, thus for metric units we have 10^-3^ x kg-M/kg.

The third part of the example covers initializing the model in the SOLUTION section. Here we use the EQUIL(EQLOPT6) parameter equal to one, to use table number one of the RVWVD keyword, in order to set the vaporized water versus depth distribution for the model.

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

In the SUMMARY section, the simulator supports summary vectors specific to CO~2~ storage (see Section 11.1.12 Option Specific Variables - CO2STORE/H2STORE Model) many of these can also be used for H~2~ storage including those shown below.

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

\-- FIELD H2 DISOLVED IN WATER PHASE

FWCD

\--

\-- FIELD H2 TRAPPED IN GAS PHASE

FGCDI

\--

\-- FIELD H2 MOBILE IN GAS PHASE

FGCDM

The final part of the example covers the SCHEDULE section. The standard WCONINJE keyword is then used to set the gas injection rate, in this case 100,000 sm^3^/day of H~2~.

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

\'BASIC=1\' ALLPROPS TEMP RSWSAT RVWSAT /

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

Note in order to get the liquid phase mole fractions of H~2~, that is, the mole fractions of H~2~ in the water phase (XMFH2), and the vapor phase mole fractions (YMFWAT) to the restart file, one must use the command line parameter enable-opm-rst-file set equal to true.

The second example shows how to use H2STORE with the alternative option (2). The example below declares that the hydrogen storage model is active for the run to account for both hydrogen and water phase solubility using OPM Flow's H~2~-Brine PVT model. Option (2) is used where the OIL phase refers to the brine and the GAS phase to H~2~.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-- FLUID TYPES AND TRACER OPTIONS

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \--

\-- ACTIVATE H2 STORAGE IN THE MODEL (OPM FLOW H2 STORAGE KEYWORD)

\--

H2STORE

\--

\-- OIL PHASE IS PRESENT IN THE RUN BUT IS THE BRINE PHASE FOR H2STORE

\--

OIL

\--

\-- GAS PHASE IS PRESENT IN THE RUN BUT IS THE H2 PHASE FOR H2STORE

\--

GAS

\--

\-- DISSOLVED GAS IN LIVE OIL IS PRESENT IN THE RUN (H2 IN BRINE)

\--

DISGAS

\--

\-- VAPORIZED OIL IN WET GAS IS PRESENT IN THE RUN (WATER IN H2)

\--

VAPOIL

The second part of the example covers the data required for the PROPS section, in which the input keywords need to be consistent with the OIL phase referring to the Brine and the GAS to H~2~; that is SGOF (gas-oil relative permeability) is used to define the H~2~-Brine relative permeability table.

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

\-- GAS-OIL RELATIVE PERMEABILITY TABLES (SGOF) -- H2STORE PHASES

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

The third part and final part of the example covers initializing the model in the SOLUTION section. Here we set the EQUIL(EQLOPT1 and EQLOPT2) parameters equal to one, to use table number one of the RSVD and RVVD keywords, in order to set the initial dissolved H~2~ and vaporised water versus depth distribution for the model.

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

\-- DEPTH RV

\-- STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RVVD

1000.0 0.000

3000.0 0.000 /

[^1]: Dedong Li, Christof Beyer, Sebastian Bauer, A unified phase equilibrium model for hydrogen solubility and solution density, International Journal of Hydrogen Energy, Volume 43, Issue 1, 2018, Pages 512-529.

[^2]: J. W. Leachman, R. T Jacobsen, S. G. Penoncello, E. W. Lemmon; Fundamental Equations of State for Parahydrogen, Normal Hydrogen, and Orthohydrogen. J. Phys. Chem. Ref. Data 1 September 2009; 38 (3): 721--748.

[^3]: Seyed Mostafa Jafari Raad, Ehsan Ranjbar, Hassan Hassanzadeh, Yuri Leonenko, Hydrogen-brine mixture PVT data for reservoir simulation of hydrogen storage in deep saline aquifers, International Journal of Hydrogen Energy, Volume 48, Issue 2, 2023, Pages 696-708.

[^4]: Tor Harald Sandve, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO~2~ storage simulation using the OPM Flow simulator. Submitted to TCCS 11 -- Trondheim Conference on CO~2~ Capture, Transport and Storage Trondheim, Norway -- June 21-23, 2021.
