### PINCHREG -- Define Pinch-Out Region Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PINCHREG](#__RefHeading___Toc74567_718313858) keyword defines the parameters used to control the generation of Non-Neighbor Connections ("NNCs") in the vertical (K) direction due to layers pinching out in combination with the [PINCHNUM](#__RefHeading___Toc74565_718313858) keyword. This allows different regions in the model to use different criteria in controlling the how pinch-outs are generated. The keyword should contain NRPINC records defining the criteria for each pinch-out region defined with the [PINCHNUM](#__RefHeading___Toc74565_718313858) keyword. NRPINC is the maximum number of [PINCHNUM](#__RefHeading___Toc74565_718313858) regions defined via the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

An alternative method to set the pinch-out criteria is to use the [PINCH](#__RefHeading___Toc74261_2479612490) keyword, that applies the criteria to the whole model.

OPM Flow will automatically generate connections between non neighbor cells in the vertical direction based on the parameters on this keyword.

| 1 | PINCHTHK | A real number defining the pinch-out threshold thickness for any cell. NNCs are generated across inactive cells having a vertical thickness less than PINCHTHK. | Defined |
| --- | --- | --- | --- |
| ft.<br>0.001 | m<br>0.001 | cm<br>0.001 |  |
| 2 | PINCHOPT | A character string controlling the generation of pinch-outs when the [MINPV](#__RefHeading___Toc569208_3181922006) keyword has been used to deactivate cells with small pore volumes. PINCHOPT can either be set to:<br>1)  GAP to allow the generation of NNCs across cells that have been made inactive with the [MINPV](#__RefHeading___Toc569208_3181922006) keyword when the thickness is greater than PINCHTHK threshold.<br>2)  NOGAP to enforce the strict adherence to the PINCHTHK threshold whether or not cells have been made inactive due to the [MINPV](#__RefHeading___Toc569208_3181922006) keyword. | GAP |
| 3 | PINCHGAP | A real number defining the maximum "empty" thickness allowed between grid blocks in adjacent grid layers for a non-zero transmissibility to exist between them. | Defined |
| ft.<br>1.0E20 | m<br>1.0E20 | cm<br>1.0E20 |  |
| 4 | PINCHCAL | A character string controlling the calculation of the pinch-out transmissibilities. PINCHCAL can either be set to:<br>1)  TOPBOT results in the pinch-out transmissibility being calculated from the half-cell Z-direction transmissibilities of the active cells on either side of the pinched-out layers.<br>2)  [ALL](#__RefHeading___Toc4420_421927891) results in the pinch-out transmissibility being calculated from the Z-direction transmissibilities harmonic average of all the cells between the active cells on either side of the pinched-out layers.<br>```{=html} <!-- --> ``` 1) | TOPBOT |
| 5 | PINCHMUL | A character string controlling the calculation of the pinch-out transmissibilities when adjustments have been made by the [MULTZ](#__RefHeading___Toc80291_1778172979) keyword. PINCHMUL can either be set to:<br>1)  TOP results in the pinch-out transmissibility being calculated from the active cell at the top of the pinch-out.<br>2)  [ALL](#__RefHeading___Toc4420_421927891) results in the pinch-out transmissibility being calculated from the minimum value of the [MULTZ](#__RefHeading___Toc80291_1778172979) of the active cell at the top of the pinch-out and all the inactive cells in the pinch-out vertical column.<br>Note if PINCHCAL has been set equal to [ALL](#__RefHeading___Toc4420_421927891) then PINCHMUL is reset to TOP, irrespective of the entered value for PINCHMUL. | TOP |
| Notes:<br>1)  The keyword should contain NRPINC records defining the criteria for each pinch-out region defined with the [PINCHNUM](#__RefHeading___Toc74565_718313858) keyword. NRPINC is the maximum number of [PINCHNUM](#__RefHeading___Toc74565_718313858) regions defined via the [GRIDOPTS](#__RefHeading___Toc45741_719036256) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record must be terminated by a "/" there is no keyword terminating "/". |  |  |  |

Table 6.110: PINCHREG Keyword Description

#### Example

\--

\-- SET PINCH-OUT CRITERA VIA THE PINCHNUM REGION

\--

PINCHREG

\-- THRESHOLD GAP EMPTY TRANS

\-- THICKNESS NO GAP GAP CALC

0.1 1\* 1\* 1\* / PINCHNUM 01

1.0 1\* 10 1\* / PINCHNUM 02

1.0 NOGAP 20 1\* / PINCHNUM 03

The above example sets the default pinch-out criteria for grid blocks defined as region one via the [PINCHNUM](#__RefHeading___Toc74565_718313858) array and different values for regions two and three.
