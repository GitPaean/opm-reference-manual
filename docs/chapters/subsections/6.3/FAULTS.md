### FAULTS -- Define Faults in the Grid Geometry

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FAULTS keyword defines the faults in the grid geometry and the keyword is normally exported with the grid geometry COORD and ZCORN data sets from static earth modeling software. Note that the FAULTS keyword is not required to describe the structural geometry as this is already accounted for in the COORD and ZCORN data sets, but instead lists the fault traces with respect to the grid. Once the fault traces have been defined with the FAULTS keyword then the fault transmissibilities can be modified by the MULTFLT keyword. Note that without the FAULTS keyword one would still get proper cross-fault transmissibilities but they would not be modifiable using MULTFLT keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FLTNAME | FLTNAME is a character string enclosed in quotes with a maximum length of eight characters, that defines the name of the fault. | None |
| 2 | I1 | The lower bound of the fault's I-direction range must be greater than or equal to one and less than or equal to I2 and NX. | None |
| 3 | I2 | The upper bound of the fault's I-direction range must be greater than or equal to II and less than or equal to NX | None |
| 4 | J1 | The lower bound of the fault's J-direction range must be greater than or equal to one and less than or equal to J2 and NY. | None |
| 5 | J2 | The upper bound of the fault's J-direction range must be greater than or equal to JI and less than or equal to NY. | None |
| 6 | K1 | The lower bound of the fault's K-direction range must be greater than or equal to one and less than or equal to K2 and NZ. | None |
| 7 | K2 | The upper bound of the fault's K-direction range must be greater than or equal to KI and less than or equal to NZ. | None |
| 8 | FLTFACE | FLTFACE is a character string enclosed in quotes with a maximum length of two characters, that classifies the fault face.<br>1)  If TRANSMULT on the GRIDOPTS keyword in the RUNSPEC section is set to NO then FLTFACE can have values of X, Y, or Z.<br>2)  Alternatively, if TRANSMULT on the GRIDOPTS keyword in the RUNSPEC section is set to YES then FLTFACE can have values of X, Y, or Z for the positive direction, or X-, Y- or Z- for the negative direction transmissibilities. | None |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  The FAULTDIM keyword in the RUNSPEC defines the maximum number of records (or segments) that can be entered with the FAULTS keyword.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.37: FAULTS Keyword Description

#### Example

The example below defines two fault traces, the first being the 'M_WEST' fault and the second the 'BC' fault trace.

\--

\-- DEFINE FAULTS IN THE GRID GEOMETRY

\--

\-- FAULT \-\-\-\-\-\-\-\-\-\-\-- FAULT TRACE \-\-\-\-\-\-\-\-\-\-\-\--

\-- NAME I1 I2 J1 J2 K1 K2 FACE

FAULTS

\'M_WEST\' 5 5 3 3 1 22 \'X\' /

\'M_WEST\' 5 5 4 4 1 22 \'X\' /

\'M_WEST\' 5 5 5 5 1 22 \'X\' /

\'M_WEST\' 5 5 6 6 1 22 \'X\' /

\'M_WEST\' 5 5 7 7 1 22 \'X\' /

\'M_WEST\' 5 5 8 8 1 22 \'X\' /

\'M_WEST\' 5 5 9 9 1 22 \'X\' /

\'M_WEST\' 5 5 10 10 1 22 \'X\' /

\'M_WEST\' 5 5 11 11 1 22 \'X\' /

.....................................................

\'BC\' 43 43 8 8 1 22 \'Y\' /

\'BC\' 42 42 9 9 1 22 \'X\' /

\'BC\' 44 44 8 8 1 22 \'Y\' /

\'BC\' 45 45 8 8 1 22 \'Y\' /

\'BC\' 46 46 8 8 1 22 \'Y\' /

\'BC\' 31 31 9 9 1 22 \'Y\' /

\'BC\' 30 30 10 10 1 22 \'X\' /

\'BC\' 32 32 9 9 1 22 \'Y\' /

\'BC\' 33 33 9 9 1 22 \'Y\' /

\'BC\' 34 34 9 9 1 22 \'Y\' /

\'BC\' 35 35 9 9 1 22 \'Y\' /

\'BC\' 36 36 9 9 1 22 \'Y\' /

\'BC\' 37 37 9 9 1 22 \'Y\' /

\'BC\' 38 38 9 9 1 22 \'Y\' /

\'BC\' 39 39 9 9 1 22 \'Y\' /

\'BC\' 40 40 9 9 1 22 \'Y\' /

.....................................................

/
