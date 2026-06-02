# System Architecture — Retail Intelligence Platform

## Overview

Retail Intelligence Platform is a modular AI-powered retail analytics system designed to process multi-camera CCTV footage and generate real-time operational insights for retail environments.

The platform combines computer vision, event-driven analytics, backend APIs, and dashboard visualization into a unified intelligent retail monitoring ecosystem.

The architecture follows a layered pipeline approach:

```text
Video Streams
    ↓
Detection & Tracking
    ↓
Event Generation
    ↓
Analytics Engine
    ↓
FastAPI Backend
    ↓
Dashboard Visualization
    ↓
AI Retail Insights
```

---

# Architectural Goals

The system was designed with the following engineering objectives:

* Real-time video analytics
* Modular AI pipeline design
* Multi-camera scalability
* Event-driven architecture
* Separation of concerns
* Extensible analytics layer
* Lightweight deployment compatibility
* Dashboard-driven operational visibility

---

# High-Level System Components

| Component         | Responsibility                          |
| ----------------- | --------------------------------------- |
| Detection Service | Runs AI video analytics                 |
| Tracking Engine   | Maintains visitor identity continuity   |
| Event Engine      | Generates schema-compliant events       |
| Analytics Engine  | Computes retail intelligence metrics    |
| FastAPI Backend   | Serves APIs and event ingestion         |
| Dashboard Layer   | Visualizes live analytics               |
| AI Insight Engine | Generates semantic operational insights |

---

# 1. Detection Layer

## Purpose

The detection layer processes CCTV video streams and identifies customers within the store environment.

## Technologies Used

* YOLOv8
* OpenCV

## Responsibilities

* Person detection
* Bounding box generation
* Confidence scoring
* Frame processing
* Multi-camera ingestion

## Design Decisions

YOLOv8 was selected because:

* lightweight inference
* strong real-time performance
* reliable retail environment detection
* easy extensibility

The detection layer was intentionally designed as:

* model-agnostic
* swappable
* pipeline-independent

Future models such as:

* RT-DETR
* YOLOv9
* custom detectors

can be integrated with minimal architectural changes.

---

# 2. Tracking Layer

## Purpose

The tracking engine maintains visitor continuity across sequential frames.

## Technologies Used

* ByteTrack
* Supervision

## Responsibilities

* Persistent track IDs
* Multi-object tracking
* Visitor continuity
* Session-level movement analysis

## Tracking Flow

```text
Detections
    ↓
ByteTrack
    ↓
Persistent Visitor IDs
```

## Design Decisions

ByteTrack was selected because:

* strong performance in crowded scenes
* lightweight inference cost
* robust retail tracking behavior
* effective short-term visitor continuity

The tracking system supports:

* trajectory-based session tracking
* future Re-ID extensibility

---

# 3. Event Generation Layer

## Purpose

The event layer converts low-level tracking information into business-level retail events.

## Responsibilities

* Entry/Exit events
* Queue events
* Purchase events
* Zone interaction events
* Metadata generation

## Event Pipeline

```text
Tracking Data
    ↓
Behavior Rules
    ↓
Retail Events
```

## Event Schema

The platform generates structured schema-compliant events containing:

* event_id
* visitor_id
* camera_id
* timestamp
* zone_id
* confidence
* metadata
* session sequence information

---

# 4. Analytics Layer

## Purpose

The analytics engine transforms raw events into operational retail intelligence.

## Features

### Queue Analytics

* billing congestion estimation
* queue wait estimation

### Funnel Analytics

* entered visitors
* browsing visitors
* queued visitors
* purchased visitors

### Heatmaps

* customer movement density
* high-engagement regions

### Purchase Correlation

* queue-to-purchase conversion logic

---

# 5. FastAPI Backend

## Purpose

The backend layer acts as the central orchestration and API service.

## Technologies Used

* FastAPI
* Uvicorn

## Responsibilities

* Event ingestion
* Analytics APIs
* Funnel endpoints
* Metrics exposure
* Dashboard connectivity

## API Design

The API layer exposes endpoints such as:

```text
/stores/{store_id}/funnel
/stores/{store_id}/metrics
```

---

# 6. Database Layer

## Technologies Used

* PostgreSQL

## Responsibilities

* event persistence
* analytics storage
* session tracking
* historical analysis

The architecture supports:

* future long-term analytics
* scalable event storage
* operational reporting

---

# 7. Dashboard Layer

## Technologies Used

* Streamlit
* Plotly

## Responsibilities

* live operational visualization
* funnel visualization
* queue monitoring
* system health visibility
* AI retail insight display

## Dashboard Features

* real-time metrics
* funnel charts
* AI-generated insights
* operational monitoring
* analytics visualization

---

# 8. AI Insight Engine

## Purpose

The AI Insight Engine semantically interprets retail metrics into business-readable operational observations.

## Responsibilities

* conversion analysis
* queue analysis
* engagement interpretation
* operational anomaly summaries

## Example Insights

* “High customer engagement detected.”
* “Billing queue congestion increasing.”
* “Moderate conversion performance observed.”

## Design Philosophy

The insight engine was designed as:

* lightweight
* extensible
* LLM-ready

The architecture supports future integration with:

* Gemini
* GPT-based models
* local LLM systems

---

# Multi-Camera Architecture

The platform processes multiple specialized camera streams.

| Camera ID       | Role                           |
| --------------- | ------------------------------ |
| CAM_PRODUCT_01  | Product interaction monitoring |
| CAM_BROWSING_01 | Browsing analytics             |
| CAM_ENTRY_01    | Entry/Exit analytics           |
| CAM_AUX_01      | Auxiliary observation          |
| CAM_BILLING_01  | Queue & purchase analytics     |

This architecture enables:

* camera-specific logic
* scalable analytics
* role-oriented processing

---

# Real-Time Processing Flow

```text
Video Input
    ↓
YOLOv8 Detection
    ↓
ByteTrack Tracking
    ↓
Event Generation
    ↓
FastAPI Ingestion
    ↓
Analytics Aggregation
    ↓
Dashboard Visualization
    ↓
AI Insights
```

---

# Scalability Considerations

The architecture was intentionally designed for future scalability.

## Future Improvements

* Cross-camera Re-ID
* Kafka event streaming
* Distributed analytics
* Cloud deployment
* Edge inference optimization
* LLM-powered semantic analytics
* RT-DETR integration
* Staff/customer classification

---

# Engineering Principles Followed

* modular architecture
* separation of concerns
* service abstraction
* reusable analytics components
* model-agnostic pipelines
* event-driven processing
* maintainable folder structure

---

# Conclusion

Retail Intelligence Platform demonstrates a complete AI-driven retail analytics architecture combining:

* computer vision
* tracking systems
* event pipelines
* operational analytics
* real-time dashboards
* AI-generated insights

The system provides a scalable foundation for future intelligent retail analytics applications.
