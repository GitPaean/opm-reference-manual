### SCALECRS -- Define End-Point Scaling Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SCALECRS keyword sets the end-point scaling option to be either two-point or three-point scaling, for when the End-Point Scaling option has been invoked by the ENDSCALE keyword in the RUNSPEC section. This determines which end-points on the relative permeability curves are used for scaling based on the supplied end-point arrays (SGCR, SWCR, etc.).

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SCALEOPT | SCALEOPT is a character string that sets the end-point scaling option and should be set to either NO or YES:<br>1)  NO: Activates two-point end-point scaling.<br>2)  YES: Activates three-point end-point | NO |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.143: SCALECRS Keyword Description

The end-point scaled for each option and the arrays used in the end-point scaling are summarized in the following table:

| Two-Point | Water | KRW | SWCR |  | SWU |
| --- | --- | --- | --- | --- | --- |
| Gas | KRG | SGCR |  | SGU |  |
| Oil-Water | KRORW | SOWCR |  | (1.0 -- SWL - SGL) |  |
| Oil-Gas | KRORG | SOGCR |  | (1.0 -- SWL - SGL) |  |
| Three-Point | Water | KRW | SWCR | (1.0 -- SOWCR - SGL) | SWU |
| Gas | KRG | SGCR | (1.0 - SOGCR-SWL) | SGU |  |
| Oil-Water | KRORW | SOWCR | (1.0 -- SWCR - SGL) | (1.0 -- SWL - SGL) |  |
| Oil-Gas | KRORG | SOGCR | (1.0 -- SGCR - SGL) | (1.0 -- SWL - SGL) |  |
| Two Phase Gas-Water Simulations |  |  |  |  |  |
| Water | KRW | SWCR | (1.0 - SGCR) | SWU |  |
| Gas | KRG | SGCR | (1.0 -SWCR) | SGU |  |

Table 8.144: End-Point Arrays Used in the End-Point Scaling Options

See also the TZONE keyword in the PROPS section that sets the transition zone end-point scaling options for the oil, gas and water phases.

#### Example

\--

\-- TWO-POINT END-POINT SCALING IS NO THREE POINT IS YES

\--

\-- SCALEOPT

\-- \-\-\-\-\-\-\-\--

SCALECRS

YES / SCALING OPTION

The above example activates three-point end-point scaling of the relative permeability curves.
