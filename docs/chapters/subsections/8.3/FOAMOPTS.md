### FOAMOPTS -- Define Foam Model Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FOAMOPTS](#__RefHeading___Toc224982_3519154785) keyword defines the transport phase for the foam (gas, water or solvent) and how gas mobility reduction should be calculated for when the Foam option has been activated by the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FOAMOPT1 | A defined character string that specifies the transport phase for the foam, and should be set to one of the following:<br>1)  [GAS](#__RefHeading___Toc38607_2267116897): for the foam to be transport in the gas phase.,<br>2)  [WATER](#__RefHeading___Toc38611_2267116897): for the foam to be transported in the water phase, or<br>3)  [SOLVENT](#__RefHeading___Toc62787_1778172979): for the foam to be transported in the solvent phase. | [GAS](#__RefHeading___Toc38607_2267116897) |
| 2 | FOAMOPT2 | A defined character string that specifies the method to be used to calculate the reduction in gas mobility, and should be set to one of the following:<br>1)  TAB: Sets the reduction in gas mobility is to be calculated based on tables using the [FOAMMOB](#__RefHeading___Toc224978_3519154785) keyword as a function of foam concentration, the [FOAMMOBS](#__RefHeading___Toc311837_803326780) keyword as a function of shear, or as a function of pressure using the [FOAMMOBP](#__RefHeading___Toc311835_803326780) keyword. All keywords are in the [PROPS](#__RefHeading___Toc39329_784232322) section.<br>2)  FUNC: Sets the reduction in gas mobility to be calculated based on a function defined via the [FOAMFRM](#__RefHeading___Toc301321_803326780), [FOAMFSC](#__RefHeading___Toc224976_3519154785), [FOAMFSW](#__RefHeading___Toc311829_803326780), [FOAMFSO](#__RefHeading___Toc311825_803326780), [FOAMFCN](#__RefHeading___Toc301319_803326780), or [FOAMFST](#__RefHeading___Toc311827_803326780) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.<br>Only the default value of TAB is currently supported by OPM Flow. | TAB |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.3.70.1: FOAMOPTS Keyword Description

#### Example

\--

\-- FOAMOPT1 FOAMOPT2

\-- PHASE MOBILITY

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

FOAMOPTS

GAS TAB / FOAM MODEL OPTIONS

The above example defines the transport phase is to be gas and the gas mobility reduction is to use a table as defined by the [FOAMMOB](#__RefHeading___Toc224978_3519154785) keyword as a function of foam concentration, the [FOAMMOBS](#__RefHeading___Toc311837_803326780) keyword as a function of shear, or as a function of pressure using the [FOAMMOBP](#__RefHeading___Toc311835_803326780) keyword.
