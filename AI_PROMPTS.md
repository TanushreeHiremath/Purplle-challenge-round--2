# AI_PROMPTS.md

# AI-Assisted Development Prompts

This document captures representative prompts used during the development of the Retail Intelligence Platform.

AI tooling was used as:

* an engineering assistant
* debugging collaborator
* architectural brainstorming tool

rather than as a fully autonomous implementation system.

All generated outputs were manually reviewed, modified, and integrated into the final architecture.

---

# 1. Detection Pipeline Architecture

## Prompt

```text id="pr1"
Design a modular multi-camera retail analytics pipeline using YOLOv8 and ByteTrack with event-driven architecture support.
```

## AI Output Influence

The AI-assisted response helped:

* structure the detection pipeline
* separate detection/tracking responsibilities
* identify reusable abstractions

---

## Manual Changes Made

The original AI-generated design was modified to:

* introduce BaseDetector abstraction
* introduce BaseTracker abstraction
* separate analytics from perception logic
* reduce coupling between services

Additional modifications were made to improve:

* maintainability
* debugging simplicity
* future extensibility

---

# 2. Event Schema Design

## Prompt

```text id="pr2"
Generate a schema-compliant retail analytics event structure for customer movement and operational intelligence.
```

## AI Output Influence

The AI-assisted response helped:

* identify useful metadata fields
* structure event payload organization
* standardize timestamp formatting

---

## Manual Changes Made

Several AI-generated fields were removed to reduce:

* payload verbosity
* schema complexity
* debugging overhead

The final schema was simplified for:

* operational clarity
* real-time analytics compatibility
* lightweight event processing

---

# 3. Queue Analytics Logic

## Prompt

```text id="pr3"
Design queue analytics logic for detecting customer billing queues using bounding-box tracking.
```

## AI Output Influence

The AI-generated suggestions helped:

* define queue-entry heuristics
* identify dwell-based queue logic
* structure queue event generation

---

## Manual Changes Made

The implementation was simplified to improve:

* deterministic behavior
* inference speed
* debugging visibility

Several overly complex heuristics were intentionally removed.

---

# 4. Dashboard Architecture

## Prompt

```text id="pr4"
Suggest a lightweight real-time dashboard architecture for retail analytics visualization.
```

## AI Output Influence

The AI-assisted response helped:

* identify Streamlit as a viable option
* structure live analytics sections
* organize operational metrics

---

## Manual Changes Made

The dashboard implementation was simplified to:

* reduce frontend complexity
* improve demo stability
* focus on analytics visibility

Several advanced frontend recommendations were intentionally rejected in favor of operational simplicity.

---

# 5. AI Retail Insights

## Prompt

```text id="pr5"
Design an AI-powered retail insight engine capable of generating operational summaries from funnel metrics.
```

## AI Output Influence

The AI-generated ideas influenced:

* semantic insight formatting
* conversion-analysis summaries
* queue congestion interpretation

---

## Manual Changes Made

The final implementation intentionally avoided:

* mandatory cloud LLM dependencies
* unstable external API reliance
* non-deterministic inference behavior

A lightweight hybrid semantic layer was implemented instead to preserve:

* offline execution
* reproducibility
* operational stability

---

# 6. Testing Strategy

## Prompt

```text id="pr6"
Generate pytest unit tests for a modular retail analytics platform with event-driven architecture.
```

## AI Output Influence

The AI-assisted output helped:

* scaffold initial test structure
* organize validation categories
* improve test readability

---

## Manual Changes Made

The generated tests were modified to:

* include project-specific event validation
* support ST1008 store configuration
* improve backend failure handling
* reduce brittle assertions

Additional prompt headers were added to satisfy submission requirements.

---

# Engineering Reflection

AI-assisted tooling accelerated:

* ideation
* debugging
* architectural exploration
* test scaffolding

However, final engineering decisions were consistently based on:

* operational constraints
* maintainability tradeoffs
* latency considerations
* system stability
* deployment feasibility

AI suggestions were treated as:

* advisory inputs
  rather than authoritative implementation decisions.

Substantial manual refinement and engineering judgment were applied throughout development.
