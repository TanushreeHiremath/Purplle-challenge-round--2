# CHOICES.md

This document captures the major engineering decisions made during the development of the Retail Intelligence Platform.

The focus of these decisions was not simply implementing functionality, but balancing:

* real-time performance
* maintainability
* scalability
* operational reliability
* implementation complexity
* hardware feasibility

under practical development constraints.

Each section documents:

* the problem being solved
* alternatives considered
* AI-assisted recommendations
* tradeoff analysis
* final engineering rationale

---

# 1. Detection Model Selection

## Problem

The platform required a detection model capable of:

* real-time inference
* multi-camera scalability
* stable person detection
* low operational latency
* compatibility with downstream tracking systems

The system also needed to operate reliably on commodity hardware without requiring dedicated GPU infrastructure.

The primary engineering challenge was balancing:

* inference speed
* detection quality
* deployment simplicity
* ecosystem maturity

rather than optimizing purely for benchmark accuracy.

---

## Options Considered

### YOLOv8

Pros:

* mature ecosystem
* strong real-time performance
* simple OpenCV integration
* lightweight deployment
* stable inference behavior

Cons:

* slightly lower theoretical accuracy than transformer-based detectors

---

### RT-DETR

Pros:

* stronger transformer-based detection quality
* modern architecture
* improved accuracy in complex scenes

Cons:

* significantly higher inference latency
* heavier compute requirements
* reduced real-time throughput under multi-camera workloads

---

### YOLOv9

Pros:

* improved architectural refinements
* newer detection improvements

Cons:

* ecosystem maturity concerns
* less stable tooling during development

---

### MediaPipe

Pros:

* lightweight

Cons:

* unsuitable for retail-scale multi-person analytics

---

## AI-Assisted Recommendation

AI-assisted tooling initially recommended:

* RT-DETR
* transformer-based architectures
* larger detection backbones

The recommendation prioritized maximizing detection quality.

However, this recommendation did not sufficiently account for:

* end-to-end pipeline latency
* real-time responsiveness
* operational stability
* multi-camera concurrency
* hardware limitations

---

## Tradeoff Analysis

The key tradeoff was:

### Higher Detection Accuracy

vs

### Stable Real-Time Throughput

Although RT-DETR produced stronger theoretical detection quality, the increased inference latency negatively affected:

* tracking continuity
* frame throughput
* event responsiveness
* multi-camera scalability

This was considered more harmful to the overall analytics pipeline than marginal accuracy improvements.

The downstream system depended more heavily on:

* temporal consistency
* stable event generation
* predictable processing latency

than maximizing isolated detector benchmarks.

---

## Final Decision

YOLOv8 was selected because it provided the strongest:

# latency-to-reliability tradeoff

for the operational requirements of the platform.

The final decision prioritized:

* stable inference
* predictable throughput
* ecosystem maturity
* deployment simplicity
* maintainability

over maximizing theoretical detection performance.

---

# 2. Event Schema Design

## Problem

A major architectural decision involved determining how analytics data should flow through the system.

The platform needed a representation that was:

* operationally interpretable
* scalable
* analytics-friendly
* extensible
* suitable for real-time processing

The challenge was deciding whether to:

* operate directly on frame-level detections
* store raw tracking outputs
* or introduce an intermediate event abstraction layer

---

## Options Considered

### Raw Detection Logs

Pros:

* maximum information retention
* simplest perception pipeline

Cons:

* difficult operational interpretation
* tightly coupled analytics
* poor business semantics

---

### Frame-Based Analytics

Pros:

* straightforward implementation

Cons:

* difficult to scale
* weak abstraction boundaries
* analytics tightly coupled to vision pipeline

---

### Event-Driven Architecture

Pros:

* clean abstraction
* operationally meaningful
* scalable analytics model
* easier downstream consumption

Cons:

* additional schema design complexity
* extra event-generation layer

---

## AI-Assisted Recommendation

AI-assisted recommendations initially suggested:

* deeply nested metadata structures
* verbose payload schemas
* highly relational event representations

While expressive, these designs introduced:

* higher serialization overhead
* increased debugging complexity
* tighter schema coupling
* unnecessary operational complexity

for the scale of the project.

---

## Tradeoff Analysis

The primary tradeoff was:

### Rich Schema Expressiveness

vs

### Operational Simplicity & Real-Time Efficiency

Highly verbose schemas improved theoretical flexibility but negatively impacted:

* maintainability
* debugging speed
* event readability
* processing simplicity

A lighter event abstraction was considered operationally superior.

---

## Final Decision

A lightweight event-driven architecture was selected.

The final schema focused on:

* business interpretability
* operational simplicity
* downstream analytics compatibility
* real-time responsiveness

rather than maximum metadata density.

Each event contains:

* event identity
* visitor identity
* timestamps
* camera source
* event semantics
* lightweight metadata

This design improved:

* observability
* analytics modularity
* future stream-processing compatibility
* debugging simplicity

while remaining extensible for future analytics evolution.

---

# 3. API Architecture Decision

## Problem

The backend architecture needed to support:

* event ingestion
* analytics retrieval
* dashboard communication
* low-latency responses
* maintainable service organization

while avoiding unnecessary infrastructure complexity.

The challenge was balancing:

* scalability
* implementation speed
* operational simplicity
* future extensibility

---

## Options Considered

### Flask

Pros:

* minimal setup
* lightweight

Cons:

* weaker async support
* less structured API tooling

---

### FastAPI

Pros:

* async-native architecture
* automatic Swagger documentation
* strong validation support
* excellent developer ergonomics

Cons:

* slightly steeper learning curve

---

### Django

Pros:

* mature ecosystem
* extensive built-in functionality

Cons:

* excessive framework overhead
* unnecessary complexity for analytics APIs

---

### Microservice-Oriented Architecture

Pros:

* strong scalability potential

Cons:

* excessive operational complexity
* deployment overhead
* unnecessary orchestration burden

---

## AI-Assisted Recommendation

AI-assisted tooling initially suggested:

* microservice decomposition
* asynchronous brokers
* distributed event orchestration
* highly decoupled service meshes

Although architecturally valid, these recommendations were rejected because they introduced:

* deployment complexity
* debugging difficulty
* operational instability
* infrastructure overhead

that was disproportionate to the project requirements.

---

## Tradeoff Analysis

The primary tradeoff was:

### Maximum Scalability

vs

### Operational Simplicity & Reliability

A distributed microservice architecture would improve theoretical scalability but significantly increase:

* infrastructure management
* debugging complexity
* local reproducibility issues
* demo instability

For the project scope, these costs outweighed the benefits.

---

## Final Decision

FastAPI was selected because it provided the strongest balance between:

* development velocity
* async capability
* maintainability
* API clarity
* operational simplicity

The backend architecture intentionally remained:

* modular
* lightweight
* service-oriented
* locally reproducible

rather than prematurely distributed.

This improved:

* developer iteration speed
* debugging efficiency
* demo stability
* system maintainability

while preserving future extensibility.

---

# 4. LLM / VLM Integration Decision

## Problem

The project explored integrating LLM/VLM systems for:

* retail insight generation
* semantic analytics
* zone interpretation
* operational summaries

The challenge was determining whether external AI APIs should become core runtime dependencies.

---

## Options Considered

### Cloud LLM APIs

Pros:

* strong semantic reasoning
* advanced natural language generation

Cons:

* quota limitations
* external dependency risk
* unpredictable latency
* demo instability

---

### Fully Rule-Based Insights

Pros:

* deterministic behavior
* offline reliability
* lightweight execution

Cons:

* less semantic richness

---

### Hybrid Architecture

Pros:

* stable local execution
* future extensibility
* optional LLM integration

Cons:

* less sophisticated semantic reasoning initially

---

## AI-Assisted Recommendation

AI-assisted tooling strongly recommended:

* direct Gemini integration
* cloud-based semantic pipelines
* LLM-generated operational reasoning

However, this introduced concerns around:

* reliability
* quota exhaustion
* offline execution
* reproducibility during evaluation

---

## Final Decision

A hybrid architecture was selected.

The final system uses:

* lightweight local semantic insights
* modular AI interfaces
* future LLM-ready integration points

rather than making external AI APIs mandatory runtime dependencies.

This improved:

* operational stability
* offline reproducibility
* demo reliability
* predictable execution behavior

while preserving future extensibility for:

* Gemini
* GPT-based systems
* local LLM deployments

---

# Final Reflection

The final engineering decisions consistently prioritized:

* operational robustness
* maintainability
* real-time responsiveness
* architectural clarity
* extensibility

over excessive complexity or purely theoretical optimization.

The resulting platform was intentionally designed as a scalable operational analytics foundation rather than a narrowly optimized computer vision prototype.
