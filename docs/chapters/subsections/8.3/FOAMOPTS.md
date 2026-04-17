### FOAMOPTS -- Define Foam Model Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FOAMOPTS keyword defines the transport phase for the foam (gas, water or solvent) and how gas mobility reduction should be calculated for when the Foam option has been activated by the FOAM keyword in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FOAMOPT1 | A defined character string that specifies the transport phase for the foam, and should be set to one of the following:<br>1)  GAS: for the foam to be transport in the gas phase.,<br>2)  WATER: for the foam to be transported in the water phase, or<br>3)  SOLVENT: for the foam to be transported in the solvent phase. | GAS |
| 2 | FOAMOPT2 | A defined character string that specifies the method to be used to calculate the reduction in gas mobility, and should be set to one of the following:<br>1)  TAB: Sets the reduction in gas mobility is to be calculated based on tables using the FOAMMOB keyword as a function of foam concentration, the FOAMMOBS keyword as a function of shear, or as a function of pressure using the FOAMMOBP keyword. All keywords are in the PROPS section.<br>2)  FUNC: Sets the reduction in gas mobility to be calculated based on a function defined via the FOAMFRM, FOAMFSC, FOAMFSW, FOAMFSO, FOAMFCN, or FOAMFST keywords in the PROPS section.<br>Only the default value of TAB is currently supported by OPM Flow. | TAB |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.3.70.1: FOAMOPTS Keyword Description

#### Example

\--

\-- FOAMOPT1 FOAMOPT2

\-- PHASE MOBILITY

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

FOAMOPTS

GAS TAB / FOAM MODEL OPTIONS

The above example defines the transport phase is to be gas and the gas mobility reduction is to use a table as defined by the FOAMMOB keyword as a function of foam concentration, the FOAMMOBS keyword as a function of shear, or as a function of pressure using the FOAMMOBP keyword.
