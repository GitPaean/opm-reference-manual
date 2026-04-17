### PVTO -- Oil PVT Properties for Live Oil

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PVTO defines the oil PVT properties for live oil[^1] and the keyword should only be used if the there is both oil and gas phases in the model. This keyword should be used when the DISGAS keyword has be declared in the RUNSPEC section indicating that dissolved gas (more commonly referred to as solution gas) is present in the oil. The keyword may be used for oil-water and oil-water-gas input decks.

| 1 | RS | A real monotonically increasing down the column values that defines the saturated gas-oil ratio ("GOR") or Rs, that defines the oil formation volume factor and the oil viscosity for the tabulated corresponding pressure for stated saturated RS.<br>For a given RS the variability of the oil formation volume factor and the oil viscosity with respect to the saturated RS and pressure is optionally included as a sub table under PRSU, FVFU and VISU columns, that is it is not necessary to repeat RS for each sub table entry. However, each sub table must be terminated by a "/".<br>The under-saturated PRSU entries are optional, except for perhaps the last RS entry to define the PVT properties above the initial saturation pressure.<br>If there are no following under-saturated PRSU entries then the RS entry row should be terminated by a "/", if there are under-saturated PRSU entries then the last PRSU entry row should be terminated by a "/". | None |  |
| --- | --- | --- | --- | --- |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |  |
| 2 | PRSS | PRSU | PRSS is a real columnar vector of real monotonically increasing down the column values that defines the oil phase saturation pressure (bubble-point pressure), that defines the oil formation volume factor and the oil viscosity for the corresponding PRSS pressure for a given saturated RS.<br>PRSU is a real columnar vector of real monotonically increasing down the column values that defines the oil phase under-saturated pressure that defines the oil formation volume factor and the oil viscosity for the corresponding PRSU pressure for a given saturated RS.<br>Note that PRSU should be greater than PRSS. | None |
| psia | barsa | atma |  |  |
| 3 | FVFS | FVFU | FVFS is a columnar vector of real increasing down the column values that defines the corresponding oil phase saturated formation volume factor for a given pressure (PRSS) and for a given RS.<br>FVFU is a columnar vector of real decreasing down the column values that defines the corresponding oil phase under-saturated formation volume factor for a given pressure (PRSU) and for a given RS. | None |
| rb/stb | rm^3^/sm^3^ | rcc/scc |  |  |
| 4 | VISS | VISU | VISS a columnar vector of real increasing down the column values that defines the corresponding oil phase saturated viscosity for a given pressure (PRSS) and for a given RS. If this is the only entry for a given RS and PRSS then the record should be terminate by a "/".<br>VISU a columnar vector of real decreasing from VISS down the column values that defines the corresponding oil phase under-saturated viscosity for a given pressure (PRSU) and for a given RS. If this is the only entry for a given RS and PRSU then the record should be terminate by a "/". | None |
| cP | cP | cP |  |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows and NRPVT Rs entries as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Apart from the RS data there must be same number of entries for each column.<br>4)  Each sub table defining the under saturated oil properties must be terminated by "/".<br>5)  Each main table is terminated by a single "/" on a separate line and there is no "/" terminator for the keyword. |  |  |  |  |

Table 8.120: PVTO Keyword Description

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the second example for an illustration on how to use this feature.

#### Example

The first example defines live oil PVT tables assuming NTPVT equals two, NPPVT is greater than or equal to two, and NRPVT is greater than or equal to 18 on the TABDIMS keyword in the RUNSPEC section.

\--

\-- OIL PVT TABLE FOR LIVE OIL

\--

PVTO

\-- RS PSAT BO VISC

\-- MSCF/STB PSIA RB/STB CPOISE

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

0.0010 14.7 1.05340 1.7230 /

0.0890 500.0 1.08890 1.1670 /

0.2060 1000.0 1.13850 0.8570 /

0.3360 1500.0 1.19640 0.6840 /

0.4750 2000.0 1.26110 0.5750 /

0.5480 2250.0 1.29570 0.5340 /

0.6220 2500.0 1.33160 0.5000 /

0.6980 2750.0 1.36890 0.4700 /

0.7750 3000.0 1.40740 0.4450 /

0.8530 3250.0 1.44710 0.4220 /

0.9330 3500.0 1.48790 0.4020 /

1.0140 3750.0 1.52980 0.3840 /

1.0960 4000.0 1.57280 0.3680 /

1.1800 4258.0 1.61760 0.3530 /

1.2630 4500.0 1.66190 0.3400 /

1.3480 4750.0 1.70780 0.3280 /

1.4340 5000.0 1.75480 0.3170 /

1.6060 5500.0 1.85020 0.2980

6242.0 1.83040 0.3186 /

/ TABLE NO. 1

\--

\--

\-- RS PSAT BO VISC

\-- MSCF/STB PSIA RB/STB CPOISE

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

0.0010 14.7 1.05340 1.7230 /

0.0390 250.0 1.06830 1.4220 /

0.0890 500.0 1.08890 1.1670 /

0.1460 750.0 1.11250 0.9850 /

0.2060 1000.0 1.13850 0.8570 /

0.2700 1250.0 1.16660 0.7590 /

0.3360 1500.0 1.19640 0.6840 /

0.4050 1750.0 1.22800 0.6240 /

0.4750 2000.0 1.26110 0.5750 /

0.5480 2250.0 1.29570 0.5340 /

0.6220 2500.0 1.33160 0.5000 /

0.6980 2750.0 1.36890 0.4700 /

0.7750 3000.0 1.40740 0.4450 /

0.8530 3250.0 1.44710 0.4220 /

0.9330 3500.0 1.48790 0.4020 /

1.0140 3750.0 1.52980 0.3840 /

1.0960 4000.0 1.57280 0.3680 /

1.1800 4258.0 1.61760 0.3530 /

1.2630 4500.0 1.66190 0.3400 /

1.3480 4750.0 1.70780 0.3280 /

1.4340 5000.0 1.75480 0.3170 /

1.6060 5500.0 1.85020 0.2980

6242.0 1.83040 0.3186 /

/ TABLE NO. 2

Notice that there must be at least two entries for the last Rs value to enable the simulator to interpolate over the undersaturated pressure region.

The second example defines live oil PVT tables assuming NTPVT equals four, NPPVT is greater than or equal to two, and NRPVT is greater than or equal to 13 on the TABDIMS keyword in the RUNSPEC section. Here, tables two to four all default to table number one.

\--

\-- OIL PVT TABLE FOR LIVE OIL

\--

PVTO

\-- RS PSAT BO VISC

\-- MSCF/STB PSIA RB/STB CPOISE

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

0.0010 14.7 1.05340 1.7230 /

0.0890 500.0 1.08890 1.1670 /

0.2060 1000.0 1.13850 0.8570 /

0.3360 1500.0 1.19640 0.6840 /

0.4750 2000.0 1.26110 0.5750 /

0.5480 2250.0 1.29570 0.5340 /

0.6220 2500.0 1.33160 0.5000 /

0.7750 3000.0 1.40740 0.4450 /

0.9330 3500.0 1.48790 0.4020 /

1.0960 4000.0 1.57280 0.3680 /

1.2630 4500.0 1.66190 0.3400 /

1.4340 5000.0 1.75480 0.3170 /

1.6060 5500.0 1.85020 0.2980

6242.0 1.83040 0.3186 /

/ TABLE NO. 1

/ TABLE NO. 2

/ TABLE NO. 3

/ TABLE NO. 4

Again, note that there is no terminating "/" for this keyword only for a table and a sub table.

[^1]: "Live" oil is oil that contains gas in solution, which is normally the case for most conventional oil reservoirs. However, for oil reservoirs classified as heavy oil reservoirs, the in situ dissolved gas may be negligible and oil would then be classified as gas-free oil which is commonly referred to as "dead" oil.
