---
title: "Gazebo Simulation and Unity Visualization"
---

import ChapterTranslator from '@site/src/components/Translation/ChapterTranslator';

<ChapterTranslator>

# Gazebo Simulation and Unity Visualization


## The Importance of Simulation
Testing on hardware is slow, expensive, and dangerous. Simulation allows us to train robots in a virtual world where time can be accelerated and gravity can be tweaked.

## Gazebo Harmonic (Ignition)
We use the modern Gazebo (formerly Ignition) for high-fidelity physics simulation.

## Key Components
1.  **SDF (Simulation Description Format):** An XML format to describe objects, robots, and environments.
2.  **World Files:** Defines the global environment (lighting, gravity, terrain).
3.  **Plugins:** C++ code that hooks into the physics engine to control models programmatically.

## URDF vs. SDF
*   **URDF:** Used by ROS for kinematics and visualization.
*   **SDF:** Used by Gazebo for physics and simulation.

## Lab Exercise
We will spawn a simple 4-wheeled robot into a Gazebo "Mars Yard" environment and control it using ROS 2 teleoperation commands.---
id: gazebo-simulation
title: Gazebo Simulation
sidebar_label: 4. Gazebo Simulation
sidebar_position: 4
---

# Gazebo Simulation

## The Importance of Simulation
Testing on hardware is slow, expensive, and dangerous. Simulation allows us to train robots in a virtual world where time can be accelerated and gravity can be tweaked.

## Gazebo Harmonic (Ignition)
We use the modern Gazebo (formerly Ignition) for high-fidelity physics simulation.

## Key Components
1.  **SDF (Simulation Description Format):** An XML format to describe objects, robots, and environments.
2.  **World Files:** Defines the global environment (lighting, gravity, terrain).
3.  **Plugins:** C++ code that hooks into the physics engine to control models programmatically.

## URDF vs. SDF
*   **URDF:** Used by ROS for kinematics and visualization.
*   **SDF:** Used by Gazebo for physics and simulation.

## Lab Exercise
We will spawn a simple 4-wheeled robot into a Gazebo "Mars Yard" environment and control it using ROS 2 teleoperation commands. -->


</ChapterTranslator>