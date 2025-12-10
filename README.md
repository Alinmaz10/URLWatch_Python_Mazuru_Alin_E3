# URLWatch_Python_Mazuru_Alin_E3
URLWatch
A Python monitoring script that continuously checks website availability based on entries from sites.txt.
Each line in the file follows the format: URL IMPORTANCE, where IMPORTANCE ∈ {INFO, WARNING, CRITICAL}.
Output uses colors: green for reachable sites, blue/yellow/red for unreachable INFO/WARNING/CRITICAL, and white for any other messages.

Phase 1 – File parsing and basic site checking
Implement a Python script that loads sites.txt, parses URL–IMPORTANCE pairs, and checks accessibility in a loop with colored status output.

Parse file and validate entries
Ping URLs periodically
Display color-coded availability
Functional result: Script correctly reads inputs and shows live colored status for all sites.

Phase 2 – Filtering and configurable intervals
Add support for command-line options to filter by IMPORTANCE level and set the check interval, applying both to the continuous monitoring loop.

Add CLI arguments for interval
Add CLI filtering by IMPORTANCE
Apply settings to monitoring logic
Functional result: Script monitors only selected categories at the chosen interval.
