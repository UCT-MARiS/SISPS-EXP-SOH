---
author: Lawrence Stanton
date: November 2024
documentclass: article
papersize: a4
geometry:
  - top=2cm
  - bottom=2cm
  - left=3cm
  - right=3cm
  - heightrounded
---
# UCT003 Low Temperature State of Health Experiment Methodology

Lawrence Stanton  
**November 2024**

## Summary

This experiment is focused at investigating the long-term State of Health (SoH) effects of AGM sealed lead acid batteries in extreme low temperature conditions. Batteries will set to a variety of States of Charge (SoC) and then subjected to low temperature conditions for extended periods of time, while being periodically cycled at 25 °C to evaluate the SoH.

## Basic Test Parameters

| Parameter                        |           Value |
|:---------------------------------|----------------:|
| Battery                          | Asterion HR12-9 |
| Nominal Voltage                  |       12 V (6S) |
| Nominal Capacity (1.57 A rate)   |         7.85 Ah |
| Absolute Max Charge Current      |           2.7 A |
| Absolute Max Charge Voltage      |          14.4 V |
| Test Batch Battery Quantity      |              14 |
| Stages                           |               5 |
| Repetitions per Stage            |               4 |
| Discharge Cycles per Repetition  |               3 |
| Initial Preconditioning Cycles   |              42 |
| Total Discharge Cycles           |             882 |
| Total ETC Storage Time per Stage |          4 Days |
| Total ETC Storage Time           |         30 Days |

Estimated Total Test Time: **2 Months**

## Methodology

The experiment will be composed of several functional test programs:

1. [Varied Discharge](#varied-discharge)
2. [Low Temperature Storage](#low-temperature-storage) (including EMF Voltage Measurement)
3. [Full Discharge Test and EIS](#full-discharge-test-and-eis) (including Preconditioning)

Each follows sequentially, and repeated for a range of storage temperatures and durations.

```mermaid
flowchart LR

start([ ])
stage{For Each Stage}
repetition{For Each Repetition}
varied[[Varied Discharge]]
storage[[Storage]]
discharge[[EIS & Full Discharge]]
done([ ])

start --> stage
stage -->|Next| repetition
repetition -->|Next| varied
varied --> storage
storage --> discharge
discharge --> repetition
repetition -->|Done| stage

stage ----->|Done| done
```

### Full Discharge Test and EIS

The following program should always be followed to perform a full discharge and EIS test:

```mermaid
flowchart LR

start([ ])
eis[[EIS]]
cycle{n Cycles}
discharge[Discharge<br>1.57 A &rarr; 10.5 V]
wait(((Rest<br>30min)))
bulk[Bulk Recharge<br>2.0A &rarr; 14.4 V]
absorb[Absorption Recharge<br>14.2 V #rarr; 0.5 A]
float[Float<br>13.7V, 30min]
recharge[Crude Recharge<br>2.0 A #rarr; 5.0 Ah &geq; 14.4 V]
done([ ])

start --> eis
eis --> cycle 
cycle -->|Next| bulk
bulk --> absorb
absorb --> float
float --> wait
wait --> discharge
discharge --> cycle

cycle -->|Done| recharge
recharge -----> done
```

> The `Crude Recharge` step is a basic recharge to ensure the battery is not left at a low SoC while other batteries may still be cycling. This step can be skipped if the battery will immediately proceed to varied discharge, since the operations are identical.

The EIS program is the same as used in UCT002.

3 discharge cycles are preferable for accuracy (as quoted for earlier), but can be reduced to 2 if practically necessary.

Both the EIS and discharge test are always done at room temperature, preferably in or soon after being in the water bath set to 25 °C. Allow at least 12 hours in the water bath following low temperature before starting. Record the temperature periodically for temperature verification.

> For -20 °C and below, allow the batteries at least 1h to warm up in air before placing in the water bath to avoid thermal stresses.

Please monitor the discharge times and report any outliers or anomalies before proceeding to the next low temperature storage period.

**Preconditioning**

To verify the manufacturer's rated 7.85 Ah capacity at the 1.57 A (5 hour) discharge rate against the other charging parameters; at factory conditions prior to `S01` and the first varied discharge, the batteries should undergo an additional initial EIS and full discharge test. This is the additional 42 cycles mentioned in the basic test parameters. The program is otherwise identical. These few cycles should also remove any initial artifacts from the batteries' manufacturing.

### Varied Discharge

The varied discharge follows the exact same procedure as the full discharge test, except the discharge step is programmed to stop after a set discharge amount, and exits immediately following discharge (no cycling).

```mermaid
%%{init: {"flowchart": {"format": svg}} }%%
flowchart LR

start([ ])
wait(((Rest<br>30min)))
bulk[Bulk Recharge<br>2.0A &rarr; 14.4 V]
absorb[Absorption Recharge<br>14.2 V #rarr; 0.5 A]
float[Float<br>13.7V, 30min]
discharge[Discharge<br>1.57 A &rarr; n Ah &vert; &leq; 10.5 V]
done([ ])

start --> bulk
bulk --> absorb
absorb --> float
float --> wait
wait --> discharge
discharge --> done
```

> The deepest discharge batteries (`C10`-`C14`) should be done last and then immediately proceed to low temperature storage. It is acceptable to allow `C01`-`C09` to wait at their varied discharge SoC while `C10`-`C14` complete.

The following amounts should be used for each battery:

| Battery | Discharge Amount | Est. SoC |
|:-------:|:----------------:|---------:|
|  `C01`  |      0.00 Ah      |   100.% |
|  `C02`  |      0.55 Ah      |    93.% |
|  `C03`  |      1.10 Ah      |    86.% |
|  `C04`  |      1.65 Ah      |    79.% |
|  `C05`  |      2.20 Ah      |    72.% |
|  `C06`  |      2.75 Ah      |    65.% |
|  `C07`  |      3.30 Ah      |    58.% |
|  `C08`  |      3.85 Ah      |    51.% |
|  `C09`  |      4.40 Ah      |    44.% |
|  `C10`  |      4.95 Ah      |    37.% |
|  `C11`  |      5.50 Ah      |    30.% |
|  `C12`  |      6.05 Ah      |    23.% |
|  `C13`  |      6.60 Ah      |    16.% |
|  `C14`  |      7.15 Ah      |     9.% |

> `C14` will end very near to the 10.5 V cut-off voltage.  
Ensure the 10.5 V threshold is programmed as an alternate exit condition to handle this possibility.  
Proceed normally if this occurs, the SoC estimates will simply be scaled to assume `C14` is at 0% SoC.

### Low Temperature Storage

The batteries shall be repeatedly stored in open circuit in the Environmental Test Chamber (ETC) for extended periods of time. The following schedule should be followed:

| Stage | Temperature | Repetitions | Duration |
|:-----:|:-----------:|:-----------:|:--------:|
| `S01` |   -00 °C    |      3      |   24h    |
| `S02` |   -00 °C    |      1      |   72h    |
| `S03` |   -10 °C    |      3      |   24h    |
| `S04` |   -10 °C    |      1      |   72h    |
| `S05` |   -20 °C    |      3      |   24h    |
| `S06` |   -20 °C    |      1      |   72h    |
| `S07` |   -30 °C    |      3      |   24h    |
| `S08` |   -30 °C    |      1      |   72h    |
| `S09` |   -40 °C    |      3      |   24h    |
| `S10` |   -40 °C    |      1      |   72h    |

Total Storage Time: **20 Days**

Complete the schedule strictly in the above sequence from `S01` to `S10`.

The temporal accuracy of the storage periods is not critical, but should remain within ±2 hours of the scheduled duration. The duration is simply measured from the time the ETC is set to run to the time it is stopped, neglecting any time to cool or heat up.

> Unlike previous experiments, this experiment will run from warmest to coldest temperatures.  
Ensure batteries are dry after being in the water bath before placing in the ETC, and avoid water intruding into the cell's venting cap at the top of the battery.

It is acceptable to remotely turn off the ETC and wait, for a maximum of 2 days, before starting discharge tests when the scheduled end time is outside working hours.

**EMF Voltage Measurement**

The EMF voltage is an interesting metric to record for the low temperatures. At the end of any one repetition within a stage of temperature (only one measurement for each temperature), measure each battery's voltage as it is removed from the test chamber. A precise (5.5 or 6.5 digit) and calibrated multimeter should be used.

### Alarms

In addition to the above procedures, alarms should be put in place to alert if the battery experiences any of the following conditions:

1. Battery voltage drops below 10.5 V.
1. Battery voltage rises above 14.4 V.
1. Battery current exceeds 2.7 A (both charge and discharge).

Halt the test should any of these conditions occur.

## Sub-batch Grouping, Priority, Test Suspension

The batch size will require a significant amount of channels and time to perform the discharge tests. The batch may therefore be split into subgroups for the discharge tests to accommodate the number of channels. Priority should be given to the lowest SoC batteries, to minimize the known consequences of extended periods of time at low SoC on SoH. i.e. `C10`-`C14` should move to discharge testing before `C01`-`C05`, etc. The `Crude Recharge` step is also made on this consideration for batteries waiting post-discharge testing and prior to varied discharge.
Having at least 7 channels available however will greatly reduce the total experiment time.

If necessary, the entire experiment may be suspended after all batteries have completed the discharge tests, including the `Crude Recharge` step, where all batteries will be in the same state of charge.

## Deliverables

The following data should be delivered:

1. Depth of Discharge Test Records
1. Varied Discharge Test Records
1. EIS Spectra
1. Environmental Chamber Temperature Records
1. Lab notes detailing:
    1. Exact times of manual actions (moving of batteries).
    1. Any deviations from the test plan.

CSV is acceptable format, but please advise if there are other formats available from the test equipment.

Please deliver scanned lab notes periodically as they are made, this will be ok for progress tracking.

## Naming Conventions

Please comment tests with the following format for unique and uniform identification:

`UCT003-<DOD|VD|EIS>-<Battery>-<Stage>/<Repetition>-[Errata]`

- `DOD|VD|EIS` - Depth of Discharge, Varied Discharge, or EIS (type of test).
- `Battery` - Battery number (C01-C15).
- `Stage` - Stage number (S01-S10).
  - Use `S00` for initial preconditioning.
- `Repetition` - Repetition number (R01-R03).
- `[Errata]` - Any additional notes or deviations from the test plan. Make lab notes for details.

e.g. `UCT003-DOD-C01-S01/R01` for the depth of discharge test following the first repetition of the first stage on battery `C01`.

## Planned Visits

Lawrence Stanton will visit the lab for initial setup and verification of the test programs. This will be a 1-3 day visit.

More visits can be made. Otherwise, this experiment will be supervised independently by Masa.

## Materials

19 Asterion HR12-9 batteries have been in storage at uYilo and 14 of these will be used. 3 more will be available as dummies. The remaining 2 will be kept as spares, should anything unexpectedly catastrophic happen.

All batteries will be returned to UCT after this experiment, as will be arranged. No teardowns are planned.

## Possible Early Exit Criteria

Should the depth of discharge tests move to below 50% of the 7.85 Ah 5h-rated capacity, some batteries or the entire test may be terminated early as this would indicate a conclusive result, and speed up the experiment time to completion.
