### WELTRAJ -- Define Well Trajectory Data

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WELTRAJ keyword defines a trajectory well together with the well trajectory data (simplified directional survey data), and is used in conjunction with the COMPTRAJ keyword in the SCHEDULE section to define the well connections to the simulation grid blocks. The keyword can only be used for trajectory wells that employ the COMPTRAJ keyword to define the connections to the grid, that is, one cannot use COMPDAT keyword in the SCHEDULE section for declaring the connections to the grid for these type of wells.

Although WELTRAJ and COMPTRAJ keywords are sufficient to define the wellbore path and connections to the grid, it is still necessary to defined the general well specification parameters using the WELSPECS keyword in the SCHEDULE section. In this case, the wellhead location parameters, WELSPECS(I, J), should be defaulted with 1\*.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well trajectory data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur.<br>Secondly, the wellhead location parameters on the WELSPECS keyword, WELSPECS(I, J), should be defaulted with 1\* for trajectory wells, as the well location will be calculated by the simulator. | None |
| --- | --- | --- | --- |
| 2 | IBRANCH | A positive integer greater than or equal to one and less than or equal to MXBRAN on WSEGDIMS keyword in the RUNSPEC section that defines the branch number of a segment.<br>All segments on the main stem must have IBRANCH set to one and lateral branches should have values between two and MXSEGS on the WSEGDIMS keyword in the RUNSPEC section.<br>Only the default value of one is currently supported, that is only the main branch of a multi-segment well is supported, or a single trajectory for a conventional well. | 1 |
| 3<br>‍ | XCORD<br>| | A real positive value representing the X coordinate in three dimensional space of the well trajectory path. The Geodesy Reference System should be same as the static model used to generate the dynamic model.<br>| | None<br>| |
| feet | m | cm |  |
| 4<br>‍ | YCORD<br>| | A real positive value representing the Y coordinate in three dimensional space of the well trajectory path. Again, the Geodesy Reference System should be same as the static model used to generate the dynamic model.<br>| | None<br>| |
| feet | m | cm |  |
| 5 | TVD | A real negative or positive value that defines the True Vertical Depth along the wellbore path at XCORD and YCORD. Normally, TVD is referenced to the subsea elevation, that is TVDSS. | None |
| feet | m | cm |  |
| 6<br>‍ | MD<br>| | A real positive value that defines the equivalent measured depth along the wellbore path at TVD. Normally, MD is referenced to a reference point on the drilling rig that drilled the well, for example, Relative to Kelly Bushing, MDRKB.<br>| | None<br>| |
| feet | m | cm |  |
| Notes:<br>1)  For this keyword the Laboratory set of units are not supported.<br>2)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/".<br>3)  Note that the total number of individual wells declared by the WELSPECS cannot exceed the valued entered via the MXWELS variable on the WELLDIMS keyword in the RUNSPEC section. |  |  |  |

Table 12.94: WELTRAJ Keyword Description

Using the WELTRAJ and COMPTRAJ keywords to define wells and how they are connected to grid, offers several advantages compared to the conventional approach based on the (I, J, K) co-ordinates of the grid. The approach allows for the wells to be independent of the grid, which is particularly useful when running ensemble cases, as the well connections are no longer required to be re-calculated for each ensemble case. In addition, quality control of the model is improved by using consistent perforation data in both the static and dynamic models.

See the example on the following page.

#### Example

The following example defines two trajectory wells oil wells, OP01 and OP02, using the WELSPECS and WELTRAJ keywords, together with their perforations using the COMPTRAJ keyword.

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

Here, well OP01 has eight perforation intervals, with the intervals one to three grouped into one completion, perforation intervals four to five grouped into completion number two, and finally the bottom three perforations are grouped into completion number three. In contrast, OP02 has six perforated intervals with their completion interval defaulted to one.
