# Agri-UAV Optimal Control

A research-oriented open-source toolkit for **point-to-point obstacle avoidance** and **optimal control** of UAVs in agricultural environments such as orchards, fields, and semi-structured low-altitude scenes.

## Features
- Point-to-point trajectory planning with obstacle avoidance
- Optimal control baseline interfaces (MPC-ready structure)
- Simple agricultural environment abstraction (orchard rows, circular obstacles, rectangular obstacles)
- Reproducible config-based experiments
- Benchmark-friendly project layout for future papers and open-source releases
- 
## Why this project matters

Autonomous UAV navigation in agricultural environments is different from navigation in generic indoor or urban scenes. Low-altitude flight in orchards, fields, and semi-structured farmland often involves narrow corridors, dense obstacles, irregular boundaries, wind disturbances, and safety-critical constraints. These characteristics make point-to-point obstacle avoidance and optimal control especially important for practical agricultural UAV deployment.

This repository is being developed as an open-source research-oriented toolkit for agricultural UAV motion planning and control. The long-term goal is to provide a reproducible and extensible codebase for benchmarking trajectory planning, obstacle avoidance, and optimal control methods in realistic agricultural scenarios.

## Current status

This project is currently in an early public development stage. The repository already includes the initial package structure, example scenarios, configuration files, evaluation utilities, and baseline interfaces for future algorithm integration. Upcoming updates will gradually add stronger baselines, richer benchmark scenarios, and more complete experiment pipelines.

## Intended users

This project is intended for:
- researchers working on UAV navigation, motion planning, and optimal control,
- students building reproducible robotics or agri-robotics experiments,
- developers interested in open-source agricultural autonomy tools.

## Open-source goals

The project aims to evolve into a practical open-source foundation for:
- agricultural UAV obstacle avoidance benchmarks,
- optimal control and trajectory planning baselines,
- reproducible evaluation in orchard and field environments,
- future integration with ROS, PX4, and simulation platforms.
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
