### DENSITY -- Define the Surface Oil, Water Gas Densities for the Fluids

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DENSITY defines the oil, water and gas surface densities for the fluids for various regions in the model. The number of DENSITY vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the DENSITY data sets to different grid blocks in the model is done via the PVTNUM keyword in the REGIONS section. One data set consists of one record or line which is terminated by a "/". The surface density or gravity must be entered using either the DENSITY or GRAVITY keywords irrespective of which phases are active in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | OILDEN | OILDEN is a real number defining the density of the oil phase at surface conditions. | Defined |
| lb/ft^3^<br>37.457 | kg/m^3^<br>600 | gm/cc<br>0.6 |  |
| 2 | WATDEN | WATDEN is a real number defining the density of the water phase at surface conditions. | Defined |
| lb/ft^3^<br>62.366 | kg/m^3^<br>999.014 | gm/cc<br>0.999014 |  |
| 3 | GASDEN | GASDEN is a real number defining the density of the gas phase at surface conditions. | Defined |
| lb/ft^3^<br>0.062428 | kg/m^3^<br>1.000 | gm/cc<br>0.001 |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.26: DENSITY Keyword Description

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the third example for an illustration on how to use this feature.

According to the SPE SI standard[^1], ***Relative Density*** (γ) replaces ***Specific Gravity*** as the term used to define the ratio of the density of a known material to the density of reference material, at standard conditions of pressure and temperature. Standard conditions vary throughout the world, but for oil field units one normally uses14.7 psia and 60 ^o^F, whereas for SI units some areas use 101.325 kPa and 15 ^o^C.

See also the GRAVITY keyword in the PROPS section, that can be used to enter the relative density values instead of the density numbers.

#### Examples

The following shows the DENSITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to one.

\--

\-- OIL WAT GAS

\-- DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

DENSITY

39.0 62.37 0.04520 / PVT DATA REGION 1

The next example shows the DENSITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- OIL WAT GAS

\-- DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

DENSITY

38.0 62.30 0.04500 / PVT DATA REGION 1

39.0 62.37 0.04520 / PVT DATA REGION 2

40.0 62.40 0.04800 / PVT DATA REGION 3

The third, and final, example shows the DENSITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to four. Here table two defaults to table one, and table four defaults to table three.

\--

\-- OIL WAT GAS

\-- DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

DENSITY

38.0 62.30 0.04500 / PVT DATA REGION 1

/ PVT DATA REGION 2

39.0 62.37 0.04520 / PVT DATA REGION 3

/ PVT DATA REGION 3

Again, note that there is no terminating "/" for this keyword.

[^1]: The SI Metric System of Units and SPE Metric Standard, Adopted for Use as a Voluntary Standard by the SPE Board of Directors, June 1983, Society of Petroleum Engineers.
