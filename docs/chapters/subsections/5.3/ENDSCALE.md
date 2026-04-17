### ENDSCALE -- Activate Relative Permeability End-Point Scaling Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ENDSCALE keyword activates OPM Flow's relative permeability end-point scaling option. The relative permeability functions are defined using the either the:

1)  SWOF, SGOF, SLGOF series of saturation functions, or the

2)  SWFN, SGFN, SGWFN, SOF2, SOF3, SOF32D series of functions.

And are allocated to the grid cells via the SATNUM keyword.

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, and the KRG, KRORG, KRORW and KRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWLX, SWLY and SWLZ instead of SWL etc. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWLX, SWLX-, SWLY, SWLY- SWLZ and SWLZ-, instead of SWL or the SWLX, SWLY and SWLZ set of keywords.

The keyword also defines the number of saturation end-point tables that allows for the re-scaling of the saturation functions to be a function of depth as opposed to being a grid property array. This is accomplished via the ENKRVD and ENPTVD keywords in the PROPS section.

| 1 | DIRECT | A character string that activates or deactivates directional end-point scaling option.<br>If DIRECT is set to NODIR then directional end-point scaling is switched off and the same saturation function is used in the x, y and z directions (unless activated otherwise by the SATOPTS keyword in the RUNSPEC section). In this case the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR and SOGCR saturation grid arrays and the KRG, KRORG, KRORW and KRW relative permeability grid cell arrays should be used to enter the grid block end-point data.<br>If DIRECT is set to DIRECT then directional end-point scaling is switched on and different saturation functions are used in the x, y and z directions (unless activated otherwise by the SATOPTS keyword in the RUNSPEC section). Here the directional form of the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR and SOGCR saturation grid arrays and the KRG, KRORG, KRORW and KRW relative permeability grid cell arrays should be use to enter the grid block end-point data. For example SWLX, SWLY and SWLZ for SWL.<br>Only the default option is supported by OPM Flow. | NODIR |
| --- | --- | --- | --- |
| 2 | IRREVERS | A character string that activates or deactivates non-reversible end-point scaling option.<br>If IRREVERS is set to REVERS then the end-point scaling is set to reversible and results in the same set of end-point arrays being used for flow from the x~I~ to x~I\ +\ 1~ direction as for the flow from the x~I~ to the x~I\ --\ 1~ for all directions (x, y and z). Here the SWLX, SWLY and SWLZ series of keywords should be used instead of SWL type of keywords.<br>Alternatively, if IRREVERS is set to IRREVERS then the end-point scaling is set to non-reversible and results in different sets of end-point arrays being applied for flow from the x~I~ to x~I\ +\ 1~ direction and the x~I~ to the x~I\ --\ 1~ direction, for all directions (x, y, z). in this case the SWLX+, SWLX-, SWLY+, SWLY- SWLZ+ and SWLZ- series of keywords should be utilized instead of SWL or the SWLX, SWLY and SWLZ set of keywords.<br>Only the default option is supported by OPM Flow. | REVERS |
| 3 | NTENDP | A positive integer that defines the maximum number of saturation end-point depth tables. The end-point depth tables are used to re-scale the saturation tables as a function of depth as opposed to being a grid block property. NTENDP may also be specified on the TABDIMS keyword, and if specified on both here and on the TABDIMS keyword the maximum value of the two is used.<br>Only the default option is supported by OPM Flow. | 1 |
| 4 | NNODES | A positive integer the defines the maximum number entries for saturation end-point depth tables. | 20 |
| 5 | MODE | A positive integer that activates the options for temperature dependent saturation end-point scaling in the commercial compositional simulator.<br>MODE should be defaulted with either 1\* or zero, which means that scaling can only be performed by grid block end-point scaling properties or via saturation end-point depth tables. | 0 |
| Notes:<br>1)  Note that the IRREVERS option can only be set to IRREVERS if the DIRECT parameter is set equal to DIRECT.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.10: ENDSCALE Keyword Description

#### Example

\-- DIRC REVERSE MAX MAX

\-- SCALE SCALE TABLES NODES

ENDSCALE

NODIR REVERS 1\* 1\* /

The above example invokes the end-point scaling option with end-point scaling being non-directional and reversible with the default number of saturation end-point depth tables (one) with 20 entries per table.
