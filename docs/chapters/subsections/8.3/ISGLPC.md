### ISGLPC -- End-Point Scaling of Grid Cell Capillary Pressure Connate Gas Saturation (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ISGLPC defines the imbibition connate gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section and the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section. The connate gas saturation is defined as the minimum gas saturation in a two-phase gas relative permeability table. The keyword only applies the scaling to the imbibition capillary pressures tables, unlike the ISGL keyword that applies the scaling to both the capillary pressure and relative permeability tables. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ISGLPC | ISGLPC is an array of real numbers assigning the connate gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>If ISGLPC is omitted from the input deck the values will be defaulted to those on the ISGL series of keywords. If the ISGL series of keywords are missing from the input deck then the values are taken from the cell allocated capillary pressure table.<br>Repeat counts may be used, for example 30\*0.03 | Taken from SGL or from the cell allocated capillary pressure table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the connate gas saturation array used with the end-point scaling option. |  |  |  |

Table 8.65: ISGLPC Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR saturation grid arrays for the saturation end-points, and the IKRG, IKRORG, IKRORW and IKRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISGLX, ISGLY and ISGLZ instead of ISGL or ISGLPC. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISGLX, ISGLX-, ISGLY, ISGLY-, ISGLZ and ISGLZ-, instead of the ISGL or ISGLPC keywords.

M*issing *Some F*unctionality - *Use with Caution.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISGLPC DATA FOR ALL CELLS

-- (NX x NY x NZ = 300)

ISGLPC

300\*0.030 /

The above example defines a constant connate gas saturation of 0.03 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
