<a id="__RefHeading___Toc210172_2884651453"></a>

### VAPPARS -- Oil Vaporization Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[VAPPARS](#__RefHeading___Toc210172_2884651453) defines the rate of oil vaporization in the presence of undersaturated gas and the rate at which the remaining oil gets "heavier" via the reduction in the solution gas-oil ratio ("Rs"). This keyword should only be used if the [OIL](#__RefHeading___Toc97439_1778172979), [GAS](#__RefHeading___Toc38607_2267116897), [DISGAS](#__RefHeading___Toc39767_2267116897) and [VAPOIL](#__RefHeading___Toc56610_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section have been invoked to allow oil, gas, dissolved gas and vaporized oil to be present in the model.

+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name          | > Description                                                                                                                                                                                                                                                                                                    | > Default |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric        | > Laboratory                                                                                                                                                                                                                                                                                                     |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > VAPPAR1       | > VAPPAR1 is a real positive dimensionless number that defines the rate at which oil vaporizes into the available undersaturated gas in a grid block.                                                                                                                                                            | > 0       |
|                                           |                 |                                                                                                                                                                                                                                                                                                                  |           |
|                                           |                 | > The default value of zero invokes the standard black-oil formulation in which all oil vaporizes into the available undersaturated phase in a grid cell. Increasing this parameter decreases the rate of vaporization.                                                                                          |           |
|                                           |                 |                                                                                                                                                                                                                                                                                                                  |           |
|                                           |                 | > Typical values for VAPPAR1 range from zero to five.                                                                                                                                                                                                                                                            |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                           | > dimensionless | > dimensionless                                                                                                                                                                                                                                                                                                  |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                       | > VAPPAR2       | > VAPPAR2 is a real positive dimensionless number that defines the rate at which the Rs of the remaining oil in a grid cell decreases                                                                                                                                                                            | > 0       |
|                                           |                 |                                                                                                                                                                                                                                                                                                                  |           |
|                                           |                 | > The default value of zero invokes the standard black-oil formulation in which the remaining oil's Rs does not change as the oil vaporizes into the available undersaturated gas in a grid cell. Increasing this parameter increases the difference between the remaining oil and the vaporized oil Rs values.  |           |
|                                           |                 |                                                                                                                                                                                                                                                                                                                  |           |
|                                           |                 | > Typical values for VAPPAR2 are less than one.                                                                                                                                                                                                                                                                  |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                           | > dimensionless | > dimensionless                                                                                                                                                                                                                                                                                                  |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                 |                                                                                                                                                                                                                                                                                                                  |           |
|                                           |                 |                                                                                                                                                                                                                                                                                                                  |           |
| 1)  The keyword is terminated by a "/".   |                 |                                                                                                                                                                                                                                                                                                                  |           |
+-------------------------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 10.63: VAPPARS Keyword Description

Note this keyword is normally used in history matching field performance to control the availability of the vaporized oil phase.

See also the [DRSDT](#__RefHeading___Toc117623_2179381650) and [DRVDT](#__RefHeading___Toc117625_2179381650) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that control the rate at which the solution gas-oil ratio and the vaporized oil-gas ratio increase within a grid block, respectively.

#### Examples

The first example sets the black-oil default parameters

\--

\-- OIL VAPORIZATION PARAMETERS

\--

\-- OIL-VAP RS-INCS

\-- VAPPAR1 VAPPAR2

VAPPARS

0 0 /

And the second example decreases the rate at which the oil vaporizes into the available undersaturated gas and increases the difference between the grid block oil saturation Rs and the vaporized oil Rs within a grid cell.

\--

\-- OIL VAPORIZATION PARAMETERS

\--

\-- OIL-VAP RS-INCS

\-- VAPPAR1 VAPPAR2

VAPPARS

1.5 0.150 /

Again, the keyword is normally used in history matching field performance to control the availability of the vaporized oil phase.
