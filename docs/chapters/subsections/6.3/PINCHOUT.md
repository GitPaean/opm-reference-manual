### PINCHOUT -- Define Pinch-Out Layers Option (Fixed)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [PINCHOUT](#__RefHeading___Toc769617_2928331029) keyword activates the generation of Non-Neighbor Connections ("NNCs") in the vertical (K) direction due to layers pinching out, using a constant threshold thickness of 0.001 for all unit systems. See also the [PINCH](#__RefHeading___Toc74261_2479612490) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that allows for specifying the threshold thickness and other parameters on a layer basis, and the [PINCHREG](#__RefHeading___Toc74567_718313858) keyword that applies the pinch-out controls to various regions in the model defined by the [PINCHNUM](#__RefHeading___Toc74565_718313858) keyword.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example will create NNCs between the cells above and below any cell having vertical thickness less than 0.001 in either feet or metres.

\--

\-- SET PINCH-OUT CRITERA WITH CONSTANT THRESHOLD THICKNESS OF 0.001

\--

PINCHOUT
