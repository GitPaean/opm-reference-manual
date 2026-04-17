### SATOPTS -- Activate Relative Permeability Assignment Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SATOPTS keyword activates OPM Flow's relative permeability assignment options. The relative permeability functions are defined using the either the:

1)  SWOF, SGOF, SLGOF series of saturation functions, or the

2)  SWFN, SGFN, SGWFN, SOF2, SOF3, SOF32D series of functions.

The allocation of the relative permeability tables to the grid cells is dependent on the options selected on this keyword (SATOPTS).

If the DIRECT option has been activated and the IRREVERS option has not been invoked on the SATOPTS keyword, then different relative permeability functions are used for the x, y, and z directions. Here the KRNUMX, KRNUMY and KRNUMZ keywords are used for Cartesian grids to allocate the relative permeability tables to the cells. For Radial grids the KRNUMR, KRNUMT and KRNUMZ keywords should be used. This results in the same relative permeability curves being used in both the xi to xi -- 1 and the xi to xi + 1 flow directions. Similarly for the y direction the same curves are used for the yi to yi -- 1 and the yi to yi + 1 flow directions. And again for the z direction, the same relative permeability function is used for flow in the zi to zi -- 1 and the zi to zi + 1 flow directions.

If the DIRECT option has been activated and the IRREVERS option has also been invoked on the SATOPTS keyword, then KRNUMX, KRNUMY and KRNUMZ keywords are used for Cartesian grids to allocate the relative permeability tables in the xi to xi + 1, yi to yi + 1, zi to zi + 1, flow directions, respectively. For Radial grids the KRNUMR, KRNUMT and KRNUMZ keywords should be used. For flow in the xi to xi -- 1 flow directions, etc., the KRNUMX-, KRNUMY- and KRNUMZ- keywords are used for Cartesian grids and the KRNUMR-, KRNUMT- and KRNUMZ- are used for radial grids.

The HYSTER option activates relative permeability hysteresis for the non-wetting phases (liquid and vapour) such that their values depend on whether the non-wetting phase saturation is increasing or decreasing. For this option the user specifies two sets of saturation functions, one for a drainage process (decreasing wetting phase saturation) and one for an imbibition process (increasing wetting phase saturation). The SATNUM and IMBNUM keywords should then be used to identify which saturation table applies to drainage and imbibition respectively. For a process starting at the maximum wetting phase saturation, on the drainage curve, with the wetting phase saturation decreasing, the drainage curve is followed. Similarly for a process starting at the minimum wetting phase saturation with the wetting phase saturation increasing, the imbibition curve is followed. If the drainage or imbibition process is reversed at some point, then the curve does not necessarily run back over its previous values. In OPM Flow the Carlson[^1] model may be used to describe relative permeability hysteresis and the Killough[^2] model may be used for relative permeability or capillary pressure. See also the EHYSTR keyword used to define the hysteresis model that is applied.

If the DIRECT option has been activated and the IRREVERS option has not been invoked on the SATOPTS keyword, then the same set of keywords as for the DIRECT only option are used to assign the drainage relative permeability curves, that is: KRNUMX, KRNUMY and KRNUMZ, plus the IMBNUMX, IMBNUMY, and IMBNUMZ, keywords for the imbibition curves. If the DIRECT option has been activated and the IRREVERS option has also been invoked on the SATOPTS keyword, then the same set are keywords as for the DIRECT and IRREVERS option are used to assign the drainage relative permeability curves, that is: KRNUMX, KRNUMX-, etc., plus the IMBNUMX, IMBNUMY, IMBNUMZ, IMBNUMX-, IMBNUMY-, IMBNUMZ- keywords for the imbibition curves. See for the various relative permeability table allocation keywords required for different combinations of the DIRECT, IRREVERS and HYSTER options.

The keyword should be followed by one or more of the following keyword options.

| 1 | DIRECT | A character string that activates the directional relative permeability assignment option.<br>If the DIRECT option is specified then directional relative permeability assignment is activated and different relative permeability functions are assigned to the x, y and z directions. In this case the KRNUMX, KRNUMY and KRNUMZ keywords are used for Cartesian grids to allocate the relative permeability tables. For Radial grids the KRNUMR, KRNUMT and KRNUMZ keywords should be used. | None |
| --- | --- | --- | --- |
| 2 | IRREVERS | A character string that activates the irreversible directional relative permeability assignment option.<br>If the IRREVERS option is specified then the relative permeability assignment is set to irreversible and results in different sets of relative permeability tables being applied for flow in the xi to xi + 1 direction and the xi to the xi -- 1 direction, for all directions (x, y, z).<br>In this case the KRNUMX, KRNUMY and KRNUMZ keywords are used for Cartesian grids to allocate the relative permeability tables in the xi to xi + 1 flow directions etc. For Radial grids the KRNUMR, KRNUMT and KRNUMZ keywords should be used. For flow in the xi to xi -- 1 flow directions, etc., the KRNUMX-, KRNUMY- and KRNUMZ- keywords are used for Cartesian grids and the KRNUMR-, KRNUMT- and KRNUMZ- are used for radial grids.<br>Only the default option is supported by OPM Flow, that is irreversible permeability tables are not supported. | None |
| 3 | HYSTER | A character string that activates the hysteresis option.<br>If the HYSTER and DIRECT options have been activated and the IRREVERS has not been invoked on the SATOPTS keyword, then different relative permeability functions are used for the x, y, and z directions and for the drainage and imbibition processes. Here the drainage relative permeability curves are allocated via the KRNUMX, KRNUMY and KRNUMZ keywords for Cartesian grids and the KRNUMR, KRNUMT and KRNUMZ keywords for radial grids. The imbibition relative permeability curves are allocated via the IMBNUMX, IMBNUMY and IMBNUMZ keywords for Cartesian grids and the IMBNUMR, IMBNUMT and IMBNUMZ keywords for radial grids.<br>If the HYSTER, DIRECT and IRREVERS options have been activated, then different relative permeability functions are used for the x, y, and z directions, each flow direction and for the drainage and imbibition processes. In addition to the aforementioned relative permeability allocation keywords for the xi to xi + 1 flow direction etc., the xi to xi -- 1 flow directions keywords, KRNUMX-, KRNUMY- and KRNUMZ- are used for Cartesian grids and the KRNUMR-, KRNUMT- and KRNUMZ- are used for radial grids. The imbibition relative permeability curves are allocated via the IMBNUMX-, IMBNUMY- and IMBNUMZ- keywords for Cartesian grids and the IMBNUMR, IMBNUMT and IMBNUMZ- keywords for radial grids. | None |
| 4 | SURFTENS | A character string that activates the capillary pressure surface tension pressure dependency option.<br>Only the default option is supported by OPM Flow, that is capillary pressure surface tension pressure dependency option is not supported. | None |
| Notes:<br>1)  Note that the IRREVERS option can only been activated if the DIRECT option is activated at the same time. See for the various relative permeability table allocation keywords.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.39: SATOPTS Keyword Description

For clarity the following table outlines the keywords that should be used in allocating the relative permeability tables for the various SATOPTS options.

| Option | Cartesian | Radial |  |  |
| --- | --- | --- | --- | --- |
| DIRECT Flow in all directions | KRNUMX<br>KRNUMY<br>KRNUMZ | KRNUMR<br>KRNUMT<br>KRNUMZ |  |  |
| DIRECT and IRREVERS<br>Flow in the i to i +1 directions.<br>Flow in the i to i -1 directions. | KRNUMX,<br>KRNUMY<br>KRNUMZ<br>KRNUMX-<br>KRNUMY-<br>KRNUMZ- | KRNUMR<br>KRNUMT<br>KRNUMZ<br>KRNUMR-<br>KRNUMT-<br>KRNUMZ- |  |  |
| DIRECT and HYSTER<br>Flow in all directions. | Drainage<br>KRNUMX<br>KRNUMY<br>KRNUMZ | Imbibition<br>IMBNUMX<br>IMBNUMY<br>IMBNUMZ | Drainage<br>KRNUMR<br>KRNUMT<br>KRNUMZ | Imbibition<br>IMBNUMR<br>IMBNUMT<br>IMBNUMZ |
| DIRECT, IRREVERS and HYSTER<br>Flow in the i to i +1 directions.<br>Flow in the i to i -1 directions. | Drainage<br>KRNUMX<br>KRNUMY<br>KRNUMZ<br>KRNUMX-,<br>KRNUMY-<br>KRNUMZ- | Imbibition<br>IMBNUMX<br>IMBNUMY<br>IMBNUMZ<br>IMBNUMX-<br>IMBNUMY-<br>IMBNUMZ- | Drainage<br>KRNUMR<br>KRNUMT<br>KRNUMZ<br>KRNUMR-<br>KRNUMT-<br>KRNUMZ- | Imbibition<br>IMBNUMR<br>IMBNUMT<br>IMBNUMZ<br>IMBNUMR-<br>IMBNUMT-<br>IMBNUMZ- |
| Notes:<br>1)  Note the drainage and imbibition classification is related to the wetting phase, that may be either oil or water; however, water is normally assumed in most cases but there are exceptions to this, especially for heavy oils.<br>2)  Keywords colored orange indicate keywords that are not currently supported in OPM Flow. |  |  |  |  |

<a id="REF_TABLE_SATOPS_RELATIVE_KEYWORDS_5_3"></a>Table 5.40: SATOPTS Relative Permeability Function Allocation Keywords

#### Examples

The first example actives the directional relative permeability assignment option only and hence the following keywords are used to allocate the relative permeability arrays for Cartesian grids: KRNUMX, KRNUMY, and KRNUMZ.

\--

\-- ACTIVATE RELATIVE PERMEABILITY ASSIGNMENT HYSTERESIS OPTIONS

\-- DIRECTTIONAL(DIRECT) IRREVERSIBLE(IRREVERS) HYSTERESIS(HYSTER)

SATOPTS

\'DIRECT\' /

The next example actives the directional and irreversible relative permeability assignment options, and hence the following keywords are used to allocate the relative permeability arrays for Cartesian grids: KRNUMX, KRNUMY, KRNUMZ, KRNUMX-, KRNUMY- and KRNUMZ-.

\--

\-- ACTIVATE RELATIVE PERMEABILITY ASSIGNMENT HYSTERESIS OPTIONS

\-- DIRECTTIONAL(DIRECT) IRREVERSIBLE(IRREVERS) HYSTERESIS(HYSTER)

SATOPTS

\'DIRECT\' \'IRREVERS\' /

Finally, the last example invokes the directional, irreversible and hysteresis assignment options.

\--

\-- ACTIVATE RELATIVE PERMEABILITY ASSIGNMENT HYSTERESIS OPTIONS

\-- DIRECTTIONAL(DIRECT) IRREVERSIBLE(IRREVERS) HYSTERESIS(HYSTER)

SATOPTS

\'DIRECT\' \'IRREVERS\' \'HYSTER\' /

In this case the drainage relative permeability curves are allocated by the KRNUMX, KRNUMY, KRNUMZ, KRNUMX-, KRNUMY-, KRNUMZ- keywords, and the imbibition relative permeability curves are allocated by the IMBNUMX, IMBNUMY, IMBNUMZ, IMBNUMX-, IMBNUMY-, IMBNUMZ- keywords.

[^1]: Carlson, F. M. (1981) SPE 10157, presented at the 56th Annual SPE Fall Meeting, San Antonio, 1981

[^2]: Killough, J. E. "Reservoir Simulation with History-dependent Saturation Functions," paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.
