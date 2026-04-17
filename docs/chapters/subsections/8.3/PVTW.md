### PVTW -- Define Water Fluid Properties for Various Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PVTW defines the water properties for various regions in the model. The number of PVTW vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the PVTW tables to different grid blocks in the model is done via the PVTNUM keyword in the REGIONS section. One data set consists of one record or line which is terminated by a "/". If the water phase is active in the model, which is normally the case, then this keyword must be defined in the OPM Flow input deck.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRES | PRES is a real number defining the water reference pressure (P) for the other parameters for this data set. | None |
| psia | barsa | atma |  |
| 2 | WFVF | WFVF is a real number defining the water formation volume factor (Bw) at the water reference pressure. | Defined |
| rb/stb<br>1.0 | rm^3^/sm^3^<br>1.0 | rcc/scc<br>1.0 |  |
| 3 | WCOMP | WCOMP is a real number defining the water compressibility (Cw) at the water reference pressure and is defined as: | Defined |
| 1/psia<br>0.00004 | 1/barsa<br>0.00004 | 1/atma<br>0.00004 |  |
| 4 | WVISC | WVISC is a real number defining the water viscosity (µw) at the water reference pressure. | Defined |
| cP<br>0.50 | cP<br>0.50 | cP<br>0.50 |  |
| 5 | WVISCOMP | WVISCOMP is a real number defining the water viscosibility (µwc) at the water reference pressure, µwc(Pref) and is defined as: | Defined |
| 1/psia<br>0.0 | 1/barsa<br>0.0 | 1/atma<br>0.0 |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.122: PVTW Keyword Description

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the third example for an illustration on how to use this feature.

#### Examples

The following shows the PVTW keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to one.

\--

\-- WATER PVT TABLE

\--

PVTW

\-- REF PRES BW CW VISC VISC

\-- PSIA RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

4840.0 1.019 2.7E-6 0.370 1\* / TABLE NO. 01

The next example shows the PVTW keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- WATER PVT TABLE

\--

PVTW

\-- REF PRES BW CW VISC VISC

\-- PSIA RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

4640.0 1.008 2.5E-6 0.350 1\* / TABLE NO. 01

4840.0 1.019 2.7E-6 0.370 1\* / TABLE NO. 02

4940.0 1.030 2.8E-6 0.390 1\* / TABLE NO. 03

The above example defines three water PVT tables and assumes that NTPVT equals three on the TABDIMS keyword in the RUNSPEC section.

The third, and final example, shows the PVTW keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to four. Here table two defaults to table one, and table four defaults to table three

\--

\-- WATER PVT TABLE

\--

PVTW

\-- REF PRES BW CW VISC VISC

\-- PSIA RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

4640.0 1.008 2.5E-6 0.350 1\* / TABLE NO. 01

/ TABLE NO. 02

4940.0 1.030 2.8E-6 0.390 1\* / TABLE NO. 03

/ TABLE NO. 04

Note that there is no terminating "/" for this keyword.
