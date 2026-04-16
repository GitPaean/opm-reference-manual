### PYEND -- End the Definition of a PYINPUT Section

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [PYINPUT](#__RefHeading___Toc356358_1898124664) and [PYEND](#__RefHeading___Toc356356_1898124664) keywords are a part of OPM Flow's Python scripting facility that processes standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck. The main purpose of the facility is to script the construction of the various keywords.

[PYINPUT](#__RefHeading___Toc356358_1898124664) declares the start of a [PYINPUT](#__RefHeading___Toc356358_1898124664) Definition Section on a single separate line, which is then followed by various standard Python commands, with one command per line. A [PYINPUT](#__RefHeading___Toc356358_1898124664) Definition Section is terminated by a [PYEND](#__RefHeading___Toc356356_1898124664) keyword (this keyword) on a separate single line.

There is no data required for this keyword and there is no terminating "/" for this keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the [PYINPUT](#__RefHeading___Toc356358_1898124664) facility allows the user to implement complex functionality and the implementation is new for the 2020-04 release. Users should therefore use caution when using this facility.

See also the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section which is also part of OPM Flow's Python scripting facility, that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time.

#### Example

The example shows how to construct the [DX](#__RefHeading___Toc92905_705534506) variable in the [GRID](#__RefHeading___Toc38674_784232322) section and to add the resulting [DX](#__RefHeading___Toc92905_705534506) array as part of the input deck.

\--

\-- START OF PYINPUT SECTION

\--

PYINPUT

\#

\# Import Numpy Model

\#

import numpy as np

\#

\# Define DX and Get the Input Decks Unit Systems

\#

dx = np.array(\[100.0, 100.0, 100.0, 100.0\])

active_unit_system = context.deck.active_unit_system()

default_unit_system = context.deck.default_unit_system()

\#

\# Set DX in the Input Deck

\#

kw = context.DeckKeyword( context.parser\[\'DX\'\], dx, active_unit_system,

default_unit_system )

context.deck.add(kw)

PYEND

The active Parser objects are accessible as context.parser and the active Deck object is available as context.deck.
