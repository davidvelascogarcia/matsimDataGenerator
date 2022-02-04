# MATSim Data Generator: matsimDataGenerator (Python)

[![matsimDataGenerator Homepage](https://img.shields.io/badge/matsimDataGenerator-develop-orange.svg)](https://github.com/davidvelascogarcia/matsimDataGenerator/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/matsimDataGenerator.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/matsimDataGenerator/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/matsimDataGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimDataGenerator)

- [MATSim Data Generator: matsimDataGenerator (Python)](#matsim-data-generator-matsimdatagenerator-python)
  - [Introduction](#introduction)
  - [Running Software](#running-software)
    - [Arguments](#arguments)
  - [Requirements](#requirements)
  - [Status](#status)
  - [Related projects](#related-projects)

## Introduction

`matsimDataGenerator` is a module in `python` language that automate MATSim simulation database files generation.

Documentation available on [docs](https://davidvelascogarcia.github.io/matsimDataGenerator)

## Running Software

1. Run [matsimDataGenerator.py](./programs).

```bash
python3 matsimDataGenerator.py
```

### Arguments

Avaliable arguments allowed:

| Argument | Full  | Simple | Description  |
| -------  |  ---  |  ----  | -----------  |
|  Database  |  --database  |  -d  | Input xml database  |
|  Output  |  --output  |  -o  | Output csv adapted database  |

## Requirements

`matsimDataGenerator` requires:

[Install pip3](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)

```bash
pip3 install -r requirements.txt
```

Tested on: `windows 10`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `kubuntu 20.04`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/matsimDataGenerator.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimDataGenerator)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/matsimDataGenerator.svg?label=Issues)](https://github.com/davidvelascogarcia/matsimDataGenerator/issues)

## Related projects

* [davidvelascogarcia: matsimConfigGenerator (Python)](https://github.com/davidvelascogarcia/matsimConfigGenerator)
* [davidvelascogarcia: matsimDataAdapter (Python)](https://github.com/davidvelascogarcia/matsimDataAdapter)
* [davidvelascogarcia: matsimDataGenerator (Python)](https://github.com/davidvelascogarcia/matsimDataGenerator)
* [davidvelascogarcia: matsimNetGenerator (Python)](https://github.com/davidvelascogarcia/matsimNetGenerator)
* [davidvelascogarcia: matsimPlansGenerator (Python)](https://github.com/davidvelascogarcia/matsimPlansGenerator)
* [davidvelascogarcia: matsimVoronoiGenerator (Python)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator)
