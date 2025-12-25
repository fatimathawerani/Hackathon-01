---
title: "ROS 2 Fundamentals"
---

import ChapterTranslator from '@site/src/components/Translation/ChapterTranslator';

<ChapterTranslator>

# ROS 2 Fundamentals


## Why ROS 2?
The Robot Operating System (ROS 2) is the industry standard middleware for robotics. It provides the plumbing that allows different parts of a robot (camera, wheels, brain) to talk to each other.

## Core Concepts

### 1. Nodes
A Node is a process that performs computation. For example, one node controls a laser range-finder, one node controls the wheel motors, and one node performs path planning.

### 2. Topics (Pub/Sub)
Nodes communicate by streaming data over **Topics**.
*   **Publisher:** Sends data (e.g., Camera Node).
*   **Subscriber:** Receives data (e.g., Object Detection Node).

### 3. Services (Client/Server)
Synchronous communication. A node sends a request and waits for a reply (e.g., "Take a picture now").

### 4. DDS (Data Distribution Service)
ROS 2 is built on top of DDS, a real-time communication standard used in military and aerospace applications, ensuring reliability and low latency.

## Hands-on: Your First Node
In this chapter, we will write a simple Python publisher node using `rclpy` to simulate a heartbeat sensor.-->


</ChapterTranslator>