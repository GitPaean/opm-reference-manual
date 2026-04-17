### PINCHXY -- Define Pinch-Out Areal Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PINCHXY keyword defines the x-direction and y-direction threshold thickness used to control the generation of Non-Neighbor Connections ("NNCs") in the x- and y- directions for missing cells in the areal plane.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | PINCHTHX | A real number defining the pinch-out threshold width for any cell in the x-direction. NNCs are generated across inactive cells having a width less than PINCHTHX in the x-direction. | Defined |
| --- | --- | --- | --- |
| ft.<br>0.001 | m<br>0.001 | cm<br>0.001 |  |
| 2 | PINCHTHY | A real number defining the pinch-out threshold width for any cell in the y-direction. NNCs are generated across inactive cells having a width less than PINCHTHY in the y-direction. | Defined |
| ft.<br>0.001 | m<br>0.001 | cm<br>0.001 |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.111: PINCHXY Keyword Description

#### Example

The example below will create NNCs between the cells in the areal plane having cell widths less than 0.01 in either feet or metres in both the x- and y-directions.

\--

\-- SET PINCH-OUT PARAMETERS FOR AREAL PLANE

\--

PINCHXY

\-- X-DIRC Y-DIRC

\-- THRESHOLD THRESHOLD

\--

0.01 0.01 /
