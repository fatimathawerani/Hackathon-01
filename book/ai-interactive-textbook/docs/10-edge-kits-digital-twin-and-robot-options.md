---
title: "Edge Kits, Digital Twin, and Robot Options"
---

import ChapterTranslator from '@site/src/components/Translation/ChapterTranslator';

<ChapterTranslator>

# Edge Kits, Digital Twin, and Robot Options


## The Concept of the Digital Twin
A Digital Twin is a virtual replica of your physical robot that runs in real-time synchronization.

## Why use a Digital Twin?
1.  **Predictive Maintenance:** Detect wear and tear before parts break.
2.  **Remote Monitoring:** Visualize what the robot "thinks" it sees vs. reality.

## Implementation with NVIDIA Isaac
We will deploy a pipeline where:
1.  The physical robot sends joint states to ROS 2.
2.  Isaac Sim subscribes to these states.
3.  The virtual robot mimics the physical robot instantly.

## Sim-to-Real Transfer
The process of training a neural network policy in the Digital Twin (Simulation) and deploying the weights to the Edge Kit (Physical Robot) without retraining. This is the "Holy Grail" of modern robotics.-->


</ChapterTranslator>