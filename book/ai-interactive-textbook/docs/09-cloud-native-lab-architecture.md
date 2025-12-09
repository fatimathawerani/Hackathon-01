---
title: "Cloud-Native Lab Architecture"
---

# Cloud-Native Lab Architecture


## Setting Up a Physical AI Lab
A robotics lab is different from a computer lab. It requires physical safety measures and specific network topologies.

## Safety First
*   **E-Stops:** Physical emergency stop buttons are mandatory.
*   **Safety Zones:** Designated areas where robots move; humans stay out during operation.

## Network Topology
Robots are distributed systems.
*   **Router:** dedicated Wi-Fi 6 router for low latency.
*   **Master/Slave Config:** Developer laptop (Master) talks to Robot CPU (Slave).
*   **Time Sync:** NTP (Network Time Protocol) is critical. If clocks drift, sensor data becomes useless.

## Calibration Station
A flat, level surface with checkerboards specifically for calibrating cameras and IMUs. -->
