### GRAVITY -- Define the Surface Oil, Water Gas Gravities for the Fluids

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

GRAVITY defines the oil API gravity and water and gas surface specific gravities for the fluids for various regions in the model. The number of GRAVITY vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the GRAVITY data sets to different grid blocks in the model is done via the PVTNUM keyword in the REGION section. One data set consists of one record or line which is terminated by a "/".

This surface density or gravity must be entered using either the DENSITY or GRAVITY keywords irrespective of which phases are active in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | OILAPI | OILAPI is a real number defining the API gravity of the oil phase at surface conditions.<br>The American Petroleum Institute ("API") classifies oils based on an API gravity (γ~API~), or degrees API (^o^API), the relationship between relative density (γ~o~) of oil and API gravity (γ~API~) is given by: | None |
| ^o^API | ^o^API | ^o^API |  |
| 2 | WATGRAV | WATGRAV is a real number defining the specific gravity of the water phase relative to pure water at surface conditions. | Defined |
| (water =1.0)<br>0.7773 | (water =1.0)<br>0.7773 | (water =1.0)<br>0.7773 |  |
| 3 | GASGRAV | GASGRAV is a real number defining the specific gravity of the gas phase relative to air at surface conditions. | Defined |
| (air =1.0)<br>1.000 | (air =1.0)<br>1.000 | (air =1.0)<br>1.000 |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each data set is by terminated by a "/" at the end of the line and there is no "/" terminator for the keyword. |  |  |  |

Table 8.43: GRAVITY Keyword Description

According to the SPE SI standard[^1], ***Relative Density*** (γ) replaces ***Specific Gravity*** as the term used to define the ratio of the density of a known material to the density of reference material, at standard conditions of pressure and temperature. Standard conditions vary throughout the world, but for oil field units one normally uses14.7 psia and 60 ^o^F, while for SI units some areas use 101.325 kPa and 15 ^o^C.

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the third example for an illustration on how to use this feature.

See also the DENSITY keyword in the PROPS section.

#### Examples

The following shows the GRAVITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to one.

\--

\-- OIL WAT GAS

\-- GRAVITY GRAVITY GRAVITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

GRAVITY

39.0 1.012 0.650 / GRAVITY PVT DATA REGION 1

The next example shows the GRAVITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- OIL WAT GAS

\-- GRAVITY GRAVITY GRAVITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

GRAVITY

37.0 1.012 0.650 / GRAVITY PVT DATA REGION 1

38.0 1.012 0.646 / GRAVITY PVT DATA REGION 2

39.0 1.012 0.640 / GRAVITY PVT DATA REGION 3

The third and final example shows the GRAVITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to four. Here table two defaults to table one, and table four defaults to table three.

\--

\-- OIL WAT GAS

\-- GRAVITY GRAVITY GRAVITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

GRAVITY

37.0 1.012 0.650 / GRAVITY PVT DATA REGION 1

/ GRAVITY PVT DATA REGION 2

38.0 1.012 0.646 / GRAVITY PVT DATA REGION 3

/ GRAVITY PVT DATA REGION 4

Again, note that there is no terminating "/" for this keyword.

[^1]: The SI Metric System of Units and SPE Metric Standard, Adopted for Use as a Voluntary Standard by the SPE Board of Directors, June 1983, Society of Petroleum Engineers.
