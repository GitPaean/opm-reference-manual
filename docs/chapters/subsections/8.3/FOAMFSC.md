### FOAMFSC -- Define Foam Gas Mobility versus Surfactant Concentration Functions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FOAMFSC](#__RefHeading___Toc224976_3519154785) keyword defines the reduction in gas mobility as a function of the foam surfactant concentration within a grid block. The Foam option must be activated by the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. In addition, the FOAMOPT2 parameter on the [FOAMOPTS](#__RefHeading___Toc224982_3519154785) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section must be set to the character string FUNC, in order to activate the functional form of the gas mobility reduction calculations.

| 1 | FOAMCON | A real positive value that defines the foam surfactant concentration at which foam modeling becomes active in the model and a strong foam is formed.<br>FOAMCON cannot be defaulted and must be specified for the first table. Subsequent tables can be defaulted and will in this case use the previous tables' entries as the default value. | None |
| --- | --- | --- | --- |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | FOAMEXP | A real positive value that defines an exponent that determines the gradient in the change of the reduction in gas mobility due to foam (es in equation .<br>Note if e~s~ is less than one then the slope of F~s~ in equation will be infinite at C~s~ equal to zero. In this case, small surfactant concentrations have a significant effect on the mobility, especially if the reference concentration Csr is also small. If this is the case use MINSURF on this keyword to set a minimum surfactant concentration to avoid small-scale numerical errors from affecting the simulation. | Defined |
| dimensionless<br>1.0 | dimensionless<br>1.0 | dimensionless<br>1.0 |  |
| 3 | MINSURF | MINSURF is a real positive value that defines the minimum surfactant concentration for which the reduction in gas mobility will be calculated. The default value of 1 x 10-20 implies that there is no minimum | Defined |
| lb/stb<br>1 x 10^-20^ | kg/sm^3^<br>1 x 10^-20^ | gm/scc<br>1 x 10^-20^ |  |
| 4 | MINSWAT | MINSWAT is a real positive value less than 1.0 that sets the minimum water saturation below which foam has no effect. The default value of 1 x 10-6 implies that there is no minimum.<br>Note that this parameter is only used in the commercial simulator's compositional simulator and is therefore not used by OPM Flow or the commercial simulators black-oil simulator. | Defined |
| dimensionless<br>1 x 10^-6^ | dimensionless<br>1 x 10^-6^ | dimensionless<br>1 x 10^-6^ |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain just one row and one row only.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.35: FOAMFSC Keyword Description

The gas mobility reduction as a function of surfactant concentration is of the form:

Where:

Fs = the resulting gas mobility reduction factor as a function of surfactant

concentration,

Cs = surfactant concentration,

Crs = reference surfactant concentration, that is Cs \< Csr defines a weak foam and

Cs \> Csr defines a strong foam (FOAMCON), and

es = exponent that determines the gradient in the change of the reduction in

gas mobility due to foam (FAOAMEXP).

The functional form of the reduction in gas mobility factor (Mrf) is:

Where:

Mr = the reference mobility reduction factor, see the [FOAMFRM](#__RefHeading___Toc301321_803326780) keyword in the

[PROPS](#__RefHeading___Toc39329_784232322) section,

Fs = gas mobility reduction factor as a function of surfactant concentration, see

the [FOAMFSC](#__RefHeading___Toc224976_3519154785) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section,

Fw = gas mobility reduction factor as a function of water saturation, see

the [FOAMFSW](#__RefHeading___Toc311829_803326780) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section,

Fo = gas mobility reduction factor as a function of oil saturation, see

the [FOAMFSO](#__RefHeading___Toc311825_803326780) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, and

Fc = gas mobility reduction factor as a function of capillary number, see

the [FOAMFCN](#__RefHeading___Toc301319_803326780) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

See also the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the [FOAMADS](#__RefHeading___Toc224974_3519154785), [FOAMMOB](#__RefHeading___Toc224978_3519154785), [FOAMOPTS](#__RefHeading___Toc224982_3519154785) and [FOAMROCK](#__RefHeading___Toc224980_3519154785) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

\--

\-- FOAM GAS MOBILITY VERSUS SURFACTANT CONCENTRATION FUNCTIONS

\--

FOAMFSC

\-- FOAM FOAM FOAM FOAM

\-- FOAMCON FOAMEXP MINSURF MINSWAT

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.001 1.010 / TABLE NO. 01

0.002 1.000 / TABLE NO. 02

/ TABLE NO. 03 (DEFAULTED)

0.001 0.850 1.0E-10 / TABLE NO. 04

0.002 1.030 / TABLE NO. 05

0.002 1.000 / TABLE NO. 06

Here, NTSFUN equals six on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and therefore six entries are required for the [FOAMFSC](#__RefHeading___Toc224976_3519154785) keyword. Table number three is completed defaulted and will therefore use all the properties from the previous table, that is table number two.
