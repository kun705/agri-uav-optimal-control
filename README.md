# Agri-UAV Optimal Control

A research-oriented open-source toolkit for **point-to-point obstacle avoidance** and **optimal control** of UAVs in agricultural environments such as orchards, fields, and semi-structured low-altitude scenes.

## Features
- Point-to-point trajectory planning with obstacle avoidance
- Optimal control baseline interfaces (MPC-ready structure)
- Simple agricultural environment abstraction (orchard rows, circular obstacles, rectangular obstacles)
- Reproducible config-based experiments
- Benchmark-friendly project layout for future papers and open-source releases

## Planned roadmap
- [ ] Kinematic and dynamic UAV models
- [ ] MPC baseline
- [ ] RRT* / A* / APF baselines
- [ ] Orchard and field benchmark scenarios
- [ ] Wind disturbance and safety margin settings
- [ ] Evaluation metrics: path length, smoothness, clearance, success rate, energy proxy
- [ ] Visualization and animation scripts

## Installation
```bash
pip install -e .
```

## Quick start
```bash
python examples/run_demo.py
```

## Project structure
```text
agri-uav-optimal-control/
├── configs/                 # experiment configs
├── docs/                    # design notes and roadmap
├── examples/                # runnable demos
├── scenarios/               # benchmark scenarios
├── src/agri_uav_optimal_control/
│   ├── envs.py              # agricultural scene abstractions
│   ├── planner.py           # basic planner interface
│   ├── metrics.py           # evaluation metrics
│   └── visualization.py     # plotting utilities
└── tests/                   # unit tests
```

## Positioning
This repository is intended to grow into a reusable open-source benchmark/toolkit for agricultural UAV navigation research, especially for **safe low-altitude navigation**, **point-to-point avoidance**, and **optimal control** in cluttered environments.

## License
MIT
