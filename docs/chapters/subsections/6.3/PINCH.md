### PINCH -- Define Pinch-Out Layer Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PINCH keyword defines the parameters used to control the generation of Non-Neighbor Connections ("NNCs") in the vertical (K) direction due to layers pinching out. This keyword is applied to all layers in the model as opposed to the PINCHREG keyword that offers more flexibility by applying the pinch-out controls to various regions in the model defined by the PINCHNUM keyword.

OPM Flow will automatically generate connections between non neighbor cells in the vertical direction based on the parameters on this keyword.

| 1 | PINCHTHK | A real number defining the pinch-out threshold thickness for any cell. NNCs are generated across inactive cells having a vertical thickness less than PINCHTHK. | Defined |
| --- | --- | --- | --- |
| ft.<br>0.001 | m<br>0.001 | cm<br>0.001 |  |
| 2 | PINCHOPT | A character string controlling the generation of pinch-outs when the MINPV keyword has been used to deactivate cells with small pore volumes. PINCHOPT can either be set to:<br>1)  GAP to allow the generation of NNCs across cells that have been made inactive with the MINPV keyword when the thickness is greater than PINCHTHK threshold.<br>2)  NOGAP to enforce the strict adherence to the PINCHTHK threshold whether or not cells have been made inactive due to the MINPV keyword. | GAP |
| 3 | PINCHGAP | A real number defining the maximum "empty" thickness allowed between grid blocks in adjacent grid layers for a non-zero transmissibility to exist between them. | Defined |
| ft.<br>1.0E20 | m<br>1.0E20 | cm<br>1.0E20 |  |
| 4 | PINCHCAL | A character string controlling the calculation of the pinch-out transmissibilities. PINCHCAL can either be set to:<br>1)  TOPBOT results in the pinch-out transmissibility being calculated from the half-cell Z-direction transmissibilities of the active cells on either side of the pinched-out layers.<br>2)  ALL results in the pinch-out transmissibility being calculated from the Z-direction transmissibilities harmonic average of all the cells between the active cells on either side of the pinched-out layers. | TOPBOT |
| 5 | PINCHMUL | A character string controlling the calculation of the pinch-out transmissibilities when adjustments have been made by the MULTZ keyword. PINCHMUL can either be set to:<br>1)  TOP results in the pinch-out transmissibility being calculated from the active cell at the top of the pinch-out.<br>2)  ALL results in the pinch-out transmissibility being calculated from the minimum value of the MULTZ of the active cell at the top of the pinch-out and all the inactive cells in the pinch-out vertical column.<br>Note if PINCHCAL has been set equal to ALL then PINCHMUL is reset to TOP, irrespective of the entered value for PINCHMUL. | TOP |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.108: PINCH Keyword Description

#### Examples

The first example below will create NNCs between the cells above and below any cell having vertical thickness less than 0.01 in either feet or metres.

\--

\-- SET PINCH-OUT PARAMETERS FOR CALCULATING PINCH-OUT PROPERTIES

\--

PINCH

\-- THRESHOLD GAP EMPTY TRANS MULTZ

\-- THICKNESS NO GAP GAP CALC CALC

0.01 1\* 1\* 1\* 1\* /

For the second example, the MINPV keyword is used to set the minimum pore volume to 500 m3 (metric units) and then the PINCH keyword is invoked with PINCHGAP set equal to GAP, as follows:

\--

\-- MINIMUM PORE VOLUME FOR ACTIVE CELLS

\--

MINPV

500.0 /

\--

\-- SET PINCH-OUT CRITERIA FOR THE MODEL

\--

PINCH

\-- THRESHOLD GAP EMPTY TRANS MULTZ

\-- THICKNESS NO GAP GAP CALC CALC

0.1 GAP 1\* 1\* 1\* /

In the above example the MINPV keyword will deactivate all cells with pore volumes less than 500 m3. These deactivated cells are inactive in the model and therefore are not included in the flow calculations; however, by default they will result in no-flow barriers but may not be thin enough for PINCH to create NNCs across them. By setting PINCHGAP equal to GAP on the PINCH keyword (the default setting), then OPM Flow generates NNCs across the cells that have been deactivated by the MINPV keyword. However, in this case there may be grid blocks in the model with a pore volume greater than MINPV but a thickness less than the pinch-out threshold. These cells will not be deactivated by the PINCH keyword.
