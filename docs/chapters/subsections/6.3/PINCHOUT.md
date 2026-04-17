### PINCHOUT -- Define Pinch-Out Layers Option (Fixed)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PINCHOUT keyword activates the generation of Non-Neighbor Connections ("NNCs") in the vertical (K) direction due to layers pinching out, using a constant threshold thickness of 0.001 for all unit systems. See also the PINCH keyword in the GRID section that allows for specifying the threshold thickness and other parameters on a layer basis, and the PINCHREG keyword that applies the pinch-out controls to various regions in the model defined by the PINCHNUM keyword.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example will create NNCs between the cells above and below any cell having vertical thickness less than 0.001 in either feet or metres.

\--

\-- SET PINCH-OUT CRITERA WITH CONSTANT THRESHOLD THICKNESS OF 0.001

\--

PINCHOUT
