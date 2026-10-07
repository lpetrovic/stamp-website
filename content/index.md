---
title: Project
template: home.html
objectives_lead: >-
  The overall objective of STAMP is to develop and validate a stochastic integrated task and
  motion planning framework that enables robot arms to collaborate with humans safely,
  efficiently and robustly in dynamic and uncertain environments.
objectives:
  - id: O1
    title: Motion planning
    text: >-
      Improve efficacy of motion planning approaches for robot arms in HRC scenarios using
      continuous-time Gaussian-process trajectory optimization with a constant-jerk prior.
  - id: O2
    title: Human motion prediction
    text: >-
      Exploit contextual information for accurate human motion prediction: intention
      estimation and full-body trajectory forecasting with calibrated uncertainty.
  - id: O3
    title: Stochastic task planning
    text: >-
      Develop a stochastic task planning framework for long-term autonomy, using gradient-free
      optimization guided by deep generative priors.
  - id: O4
    title: Robust execution
    text: >-
      Optimize low-level execution with model predictive control that accounts for uncertainty
      and for forces induced by grasped objects.
  - id: O5
    title: Real-world demonstrations
    text: >-
      Demonstrate the framework in real-world, high degree-of-freedom HRC scenarios: handovers,
      collaborative box stacking and peg-in-hole insertion.
---

## About the project

The STAMP project aims to enable **safe and efficient human-robot collaboration (HRC)** in
dynamic, uncertain environments, which is a fundamental challenge in robotics. Robots perform
well in structured industrial settings, but they struggle in unstructured spaces where human
presence introduces unpredictability.

STAMP proposes a novel **stochastic integrated task and motion planning (TAMP)** framework that
explicitly models uncertainty throughout the planning hierarchy. Unlike deterministic TAMP
approaches, STAMP propagates uncertainty from task-level decisions through motion planning,
enabling risk-aware action selection. The robot maintains probabilistic beliefs about human
intentions and future states, which leads to anticipatory re-planning when predictions indicate
potential conflicts.

The project will use motion capture systems, RGB-D sensors and collaborative robot platforms.
All developed methods will be released as open-source, ROS-compatible software.
