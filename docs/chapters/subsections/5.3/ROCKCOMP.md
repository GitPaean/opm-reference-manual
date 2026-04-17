### ROCKCOMP -- Activate Rock Compaction

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKCOMP keyword activates rock compaction and defines various rock compaction options for the run. By default OPM Flow models rock compaction via pore volume compressibility as entered on the ROCK keyword in the PROPS section. This keyword enables pressure dependent pore volume and transmissibility multipliers for rock compaction that are entered in the PROPS section using the ROCKTAB keyword. Currently OPM Flow only supports the default options for rock compaction.

| 1 | ROCKOPT | A character string that defines the rock compaction option based on one of the following character strings:<br>1)  REVERS: Rock compaction is reversible with increasing pressure. The rock compaction multipliers should be entered via the ROCKTAB keyword in the PROPS section. This is the default value.<br>2)  IRREVERS: Rock compaction is irreversible, that is the rock expansion does not occur when the pressure subsequently increases.<br>3)  HYSTER: Invokes the hysteresis rock compaction option.<br>4)  BOBERG: Rock compaction hysteresis is modeled using the Boberg formulation[^1].<br>5)  REVLIMIT: Activates the reversible hysteresis rock compaction option that limits the pore volume subject to reversibility based on the minimum pressure in a grid block and the initial water saturation. This option is only intended to be used with the water induced compaction model, neither of which are currently supported by OPM Flow..<br>6)  PALM-MAN: Rock compaction hysteresis is modeled using the Palmer-Mansoori[^2] and [^3] formulation for coal bed methane reservoirs, neither of which are supported by OPM Flow.<br>7)  NONE: Deactivates rock compaction, unless the water induced compaction model has been invoked.<br>Only the REVERS and IRREVERS options are supported by OPM Flow. | REVERS |
| --- | --- | --- | --- |
| 2 | NTROCC | A positive integer that defines the number of rock compaction tables, that is the number of ROCKTAB tables to be used by OPM Flow. | 1 |
| 3 | WATINOPT | A character string that states if the water induced rock compaction option should be used (YES) or not (NO). If set to YES then either the ROCKTABW or the ROCK2D and ROCKWNOD keywords should be entered in the PROPS section. | NO |
| 4 | PORTXROP | A character string that specifies the model to be used for when transmissibility is dependent on porosity, and should be set to either:<br>1)  EXP: An exponential porosity-transmissibility relationship should be used.<br>2)  CZ: The Carmen-Kozeny[^4]^,^ [^5] and [^6] porosity-transmissibility relationship should be used.<br>This option is used in the commercial compositional simulator and is therefore ignored by OPM Flow. | 1\* |
| 5 | CARKZEXP | The exponent constant in the Carmen-Kozeny porosity-transmissibility equation for when PORTXROP has been set to CZ.<br>This option is used in the commercial compositional simulator and is therefore ignored by OPM Flow. | 0.0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.38: ROCKCOMP Keyword Description

#### Example

\--

\-- ROCK NUMBER WAT POR-TRAN

\-- OPTN TABLES INDUCE OPTION

ROCKCOMP

REVERS 5 NO 1\* /

The above example defines the default values for the ROCKCOMP keyword with five rock compaction tables.

[^1]: Beattie, C.I., Boberg, T.C., and McNab, G.S. "Reservoir Simulation of Cyclic Steam Stimulation in the Cold Lake Oil Sands," paper SPE 18752, Society of Petroleum Engineers Journal, (1991) 6, No. 2, 200-206.

[^2]: Palmer, I. and Mansoori, J. "How Permeability Depends on Stress and Pore Pressure in Coalbeds: A New Model," paper SPE 52607, SPE Reservoir Evaluation & Engineering (1998) 1, No. 6, 539-544.

[^3]: Clarkson, C.R., Pan, Z., Palmer, I. and Harpalani, S. \"Predicting Sorption-Induced Strain and Permeability Increase With Depletion for Coalbed-Methane Reservoirs\", SPE 114778-PA, SPE Journal (2010) 15, No. 1, 152--159.

[^4]: J. Kozeny, \"Ueber kapillare Leitung des Wassers im Boden.\" Sitzungsber Akad. Wiss., Wien, 136(2a): 271-306, 1927.

[^5]: P.C. Carman, \"Fluid flow through granular beds.\" Transactions, Institution of Chemical Engineers, London, 15: 150-166, 1937.

[^6]: P.C. Carman, \"Flow of gases through porous media.\" Butterworths, London, 1956
