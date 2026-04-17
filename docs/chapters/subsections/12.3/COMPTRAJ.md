### COMPTRAJ -- Define Well Trajectory Connections to the Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The COMPTRAJ keyword defines how a well that has been declared as a trajectory well, using the WELTRAJ keyword in the SCHEDULE section, is connected to the reservoir model by defining or modifying existing well perforation depths. The keyword can only be used for wells defined by the WELTRAJ keyword, and WELTRAJ defined wells must use the COMPTRAJ keyword to define the connections to the grid, that is one cannot use COMPDAT for these type of wells.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | IBRANCH | A positive integer greater than or equal to one and less than or equal to MXBRAN on WSEGDIMS keyword in the RUNSPEC section that defines the branch number of a segment.<br>All segments on the main stem must have IBRANCH set to one and lateral branches should have values between two and MXSEGS on the WSEGDIMS keyword in the RUNSPEC section.<br>Only the default value of one is currently supported, that is only the main branch of a multi-segment well is supported, or a single trajectory for a conventional well. | 1 |
| 3<br>‍ | TOP<br>| | A real positive value that defines the depth of the top of the perforation interval, and should be less than the value entered for the BOT parameter (the bottom perforation depth).<br>| | None<br>| |
| feet | m | cm |  |
| 4<br>‍ | BOT<br>| | A real positive value that defines the depth of the base of the perforation interval, and should be greater than the value entered for the TOP parameter (the top perforation interval).<br>| | None<br>| |
| feet | m | cm |  |
| 5 | REF | REF is a defined character string that defines the reference depth type for TOP and BOT, and should be set to either:<br>1)  MD for the depths referencing Measured Depth, or<br>2)  TVD for depths referencing True Vertical Depth.<br>Only measured depth is currently supported, that is MD. | MD |
| 6 | ICOMP | An integer greater than or equal to one and less than or equal to MXCONS as defined on the WELLDIMS keyword in the RUNSPEC section, that defines the completion number of the currently defined perforation interval (connection interval).<br>If defaulted with 1\*, then ICOMP is set equal to one. | 1 |
| 7 | STATUS | A defined character string of length four that defines the connections' operational status within the perforation interval, STATUS should be set to one of the following character strings:<br>1)  OPEN: the connections are open to flow.<br>2)  SHUT: the connections are closed to flow (shut-in).<br>3)  AUTO: the connection are initially closed, but may be opened automatically if an economic limit is violated. Currently this option is not supported by OPM Flow. | OPEN |
| 8 | SATNUM | An integer greater than or equal to zero and less than NTSFUN as declared on the TABDIMS keyword in the RUNSPEC, that defines the saturation table number to be used for flow between the reservoir grid block and the well connections.<br>If SATNUM is set to zero or defaulted with 1\* then:<br>1)  The saturation table allocated to the grid block that the connections are located within are used.<br>2)  If the hysteresis option has been activated via the HYSTER variable on the SATOPTS keyword in the RUNSPEC section, then both the imbibition and drainage saturation tables allocated to the grid block that the connections are located within are used. The imbibition table allocation can be changed by the COMPIMB keyword in the RUNSPEC section, provided it is entered after the COMPTRAJ keyword. | 0 |
| 9 | CONFACT | A real value greater than or equal to zero that defines the transmissibility connection factor between the well bore and the reservoir grid block.<br>If set to zero or defaulted with 1\* then items (10) through (13) are used to calculate CONFACT. | Defined |
| cP.rb/day/psia<br>0 | cP.rm^3^/day/bars<br>0 | cP.rcc/hr/atm<br>0 |  |
| 10 | DW | A real positive value that defines the well bore diameter of the connections for the well.<br>DW is used in calculating a well's productivity or injectivity index; however the value will be ignored in calculating the connections CONFACT value if CONFAC has been directly entered. | None |
| feet | m | cm |  |
| 11 | KH | A real value that defines the effective KH (permeability x length) for the connections within the perforation interval.<br>If less than or equal to zero, or defaulted by 1\*, then KH is calculated from the connected grid blocks. KH is ignored if CONFACT has been directly entered. | Calculated from connected grid blocks |
| mD.ft | mD.m | mD.cm |  |
| 12 | SKIN | A real value that defines the connections dimensionless skin factor.<br>SKIN is used in calculating a well's productivity or injectivity index; however, the value will be ignored in calculating the connections CONFACT value if CONFACT has been directly entered. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 13 | DFACT | A real value that defines the non-Darcy D factor coefficient for gas wells.<br>This value should be defaulted with 1\* and the non-Darcy D factor coefficient for gas wells defined via the WDFAC keyword in the SCHEDULE section.<br>Currently this option is not supported by OPM Flow. | 1\* |
| day/Mscf | day/m^3^ | hour/sc |  |
| Notes:<br>1)  Note unlike the COMPDAT keyword, there is no direction parameter, COMPDAT(DIRECT), for COMPTRAJ, as the wellbore direction is implicit in the well trajectory defined by the WELTRAJ keyword in the SCHEDULE section.<br>2)  The keyword is followed by up to MXCONS records as declared on the WELLDIMS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.18: COMPTRAJ Keyword Description

Using the WELTRAJ and COMPTRAJ keywords to define wells and how they are connected to grid, offers several advantages compared to the conventional approach based on the (I, J, K) co-ordinates of the grid. The approach allows for the wells to be independent of the grid, which is particularly useful when running ensemble cases, as the well connections are no longer required to be re-calculated for each ensemble case. In addition, quality control of the model is improved by using consistent perforation data in both the static and dynamic models.

#### Example

The following example defines two trajectory wells oil wells, OP01 and OP02, using the WELTRAJ keyword, together with their perforations using the COMPTRAJ keyword.

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW OPEN CROSS PVT

\-- NAME NAME I J DEPTH FLUID AREA EQUANS SHUT FLOW TABLE

WELSPECS

OP01 PLATFORM 1\* 1\* 1\* OIL 1\* STD SHUT NO 1\* /

OP02 PLATFORM 1\* 1\* 1\* OIL 1\* STD SHUT NO 1\* /

/

\--

\-- WELL TRAJECTORY DATA

\--

\-- WELL BRAN XCORD YCORD TVDSS MD

\-- NAME NO DEPTH DEPTH

\-- \-\-\-\-- \-\-\-- \-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\--

WELTRAJ

OP01 1\* 2.805445e+06 3.602948e+06 -100.000000 0.0 /

OP01 1\* 2.805445e+06 3.602948e+06 877.0000000 977.0 /

OP01 1\* 2.805445e+06 3.602948e+06 957.9950240 1058.0 /

OP01 1\* 2.805444e+06 3.602946e+06 1051.976081 1152.0 /

.....................\... /

OP02 1\* 2.810828e+06 3.604507e+06 9371.792711 11418.0 /

OP02 1\* 2.810885e+06 3.604525e+06 9443.657000 11511.0 /

OP02 1\* 2.810952e+06 3.604546e+06 9531.966162 11624.0 /

OP02 1\* 2.810973e+06 3.604553e+06 9560.411742 11660.0 /

/

\--

\--

\-- WELL TRAJECTORY CONNECTION DATA

\--

\-- WELL BRAN \-- PERFORATION \-- COMPL OPEN SAT CONN WELL KH SKIN D

\-- NAME NO. TOP BOT REF NO. SHUT TAB FACT DIA FACT FACT FACT

COMPTRAJ

OP01 1\* 8230 8244 MD 1 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 8352 8380 MD 1 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 9070 9100 MD 1 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 9220 9250 MD 2 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 9266 9280 MD 2 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 9693 9703 MD 3 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP01 1\* 9940 9974 MD 3 SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 9979 9985 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 10173 10183 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 10190 10204 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 10327 10333 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 10339 10345 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

OP02 1\* 11528 11538 TVD 1\* SHUT 1\* 1\* 0.708 1\* 0.0 1\* /

/

Well OP01 has eight perforation intervals, with the intervals one to three grouped into one completion, perforation intervals four to five grouped into completion number two, and finally the bottom three perforations are grouped into completion number three. In contrast, OP02 has six perforated intervals with their completion interval defaulted to one.
