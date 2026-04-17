<a id="__RefHeading___Toc210172_2884651453"></a>

### VAPPARS -- Oil Vaporization Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

VAPPARS defines the rate of oil vaporization in the presence of undersaturated gas and the rate at which the remaining oil gets "heavier" via the reduction in the solution gas-oil ratio ("Rs"). This keyword should only be used if the OIL, GAS, DISGAS and VAPOIL keywords in the RUNSPEC section have been invoked to allow oil, gas, dissolved gas and vaporized oil to be present in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | VAPPAR1 | VAPPAR1 is a real positive dimensionless number that defines the rate at which oil vaporizes into the available undersaturated gas in a grid block.<br>The default value of zero invokes the standard black-oil formulation in which all oil vaporizes into the available undersaturated phase in a grid cell. Increasing this parameter decreases the rate of vaporization.<br>Typical values for VAPPAR1 range from zero to five. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 2 | VAPPAR2 | VAPPAR2 is a real positive dimensionless number that defines the rate at which the Rs of the remaining oil in a grid cell decreases<br>The default value of zero invokes the standard black-oil formulation in which the remaining oil's Rs does not change as the oil vaporizes into the available undersaturated gas in a grid cell. Increasing this parameter increases the difference between the remaining oil and the vaporized oil Rs values.<br>Typical values for VAPPAR2 are less than one. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 10.63: VAPPARS Keyword Description

Note this keyword is normally used in history matching field performance to control the availability of the vaporized oil phase.

See also the DRSDT and DRVDT keywords in the SCHEDULE section that control the rate at which the solution gas-oil ratio and the vaporized oil-gas ratio increase within a grid block, respectively.

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
