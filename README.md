# Simulation of Most Permissive Boolean networks


⚠️⚠️⚠️⚠ **THIS MODULE IS DEPRECATED IN FAVOR OF [mpbn](https://github.com/bnediction/mpbn)** ⚠️⚠️⚠️

Since version 2.0, `mpbn` ships the `mpbn.simulation` module and `mpbn-sim` command line.
It is integrated in the [CoLoMoTo Docker image](https://colomoto.github.io/notebook/) since version `2022-12-01`.

## Installation

```
pip install https://github.com/bnediction/mpbn-sim/archive/refs/heads/main.zip
```

## Usage

The `mpbn_sim` command takes as input a JSON file describing the model and the
simulation parameters.
See https://github.com/bnediction/mpbn-sim/tree/main/experiments
for example of experiment files.


```
mpbn_sim experiments/file.json
```

See `mpbn_sim -h` for options.

