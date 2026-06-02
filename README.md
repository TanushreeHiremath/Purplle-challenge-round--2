# 🛍️ Retail Intelligence Platform

## Overview

Retail Intelligence Platform is an AI-powered multi-camera retail analytics system designed to analyze customer behavior, store operations, and conversion funnels using CCTV footage and real-time computer vision pipelines.

The platform processes multiple camera feeds using object detection, tracking, event generation, and analytics services to provide operational insights such as:

* Customer entry/exit analytics
* Product browsing behavior
* Billing queue monitoring
* Purchase funnel analytics
* Heatmap generation
* AI-powered retail insights
* Real-time dashboard visualization

The system follows a modular architecture with separate detection, analytics, API, and dashboard layers, enabling scalability and future extensibility.

# Problem Statement

Traditional retail stores often lack real-time operational visibility into:

* Customer movement patterns
* Product engagement behavior
* Queue congestion
* Purchase conversion funnels
* Zone-level interaction analytics

This platform solves these challenges using AI-driven computer vision and event-based analytics pipelines.

# Key Features

## 🎯 AI Detection Pipeline

* YOLOv8-based customer detection
* Multi-camera video processing
* Real-time frame analytics
* Configurable camera roles

## 🧠 Tracking & Visitor Analytics

* ByteTrack-based multi-object tracking
* Visitor session tracking
* Entry/Exit event generation
* Customer flow analysis

## 📊 Retail Analytics

* Queue monitoring
* Purchase correlation logic
* Heatmap generation
* Funnel conversion analytics
* Zone interaction tracking

## ⚡ Real-Time Architecture

* FastAPI backend
* Live Streamlit dashboard
* Event-driven architecture
* Schema-compliant event pipeline

## 🤖 AI Insight Engine

* AI-inspired retail insight generation
* Conversion analysis
* Queue congestion analysis
* Customer engagement summaries

# System Architecture

CCTV Videos
     ↓
YOLOv8 Detection
     ↓
ByteTrack Tracking
     ↓
Event Generation Engine
     ↓
FastAPI Backend
     ↓
Analytics Engine
     ↓
Postgres / Event Storage
     ↓
Streamlit Dashboard
     ↓
AI Retail Insights

# Tech Stack

| Layer            | Technologies        |
| ---------------- | ------------------- |
| Detection        | YOLOv8, OpenCV      |
| Tracking         | ByteTrack           |
| Backend          | FastAPI             |
| Dashboard        | Streamlit           |
| Database         | PostgreSQL          |
| Analytics        | Python              |
| Visualization    | Plotly              |
| Event Processing | Custom Event Engine |

# Multi-Camera Architecture

| Camera          | Role                          |
| --------------- | ----------------------------- |
| CAM_PRODUCT_01  | Product interaction analytics |
| CAM_BROWSING_01 | Browsing analytics            |
| CAM_ENTRY_01    | Entry/Exit analytics          |
| CAM_AUX_01      | Auxiliary monitoring          |
| CAM_BILLING_01  | Queue & purchase analytics    |

# Event Schema

The platform generates schema-compliant retail analytics events.

Example:
{
  "event_id": "uuid-v4",
  "store_id": "ST1008",
  "camera_id": "CAM_ENTRY_01",
  "visitor_id": "VIS_a12bc3",
  "event_type": "ENTRY",
  "timestamp": "2026-03-03T14:22:10Z",
  "zone_id": null,
  "dwell_ms": 0,
  "is_staff": false,
  "confidence": 0.91,
  "metadata": {
    "queue_depth": null,
    "sku_zone": null,
    "session_seq": 1
  }
}

# Project Structure


store-intelligence-platform/
│
├── services/
│   ├── detection_service/
│   ├── api_service/
│   ├── analytics/
│   └── events/
│
├── dashboard/
│
├── tests/
│
├── logs/
│
├── data/
│
├── docker-compose.yml
│
└── README.md

# Real-Time Dashboard

The Streamlit dashboard provides:

* Live funnel analytics
* Queue monitoring
* Purchase analytics
* AI retail insights
* System health monitoring
* Real-time operational visibility

# Running the Project

## clone this repo

git clone <repo>

## 1. Start Backend

docker compose up --build

local url- http://localhost:8000
Swagger url- http://localhost:8000/docs

## 2. Start AI Pipeline

python -m services.detection_service.pipeline.multi_camera_pipeline

## 3. Launch Dashboard

streamlit run dashboard/app.py

dashboard url- http://localhost:8501

# Testing

Run unit tests using:

pytest tests

The project includes:

* Event schema tests
* Queue analytics tests
* API tests
* Insight engine tests

# AI Usage Disclosure

AI-assisted development tools were used for:

* code scaffolding
* architectural planning
* testing support
* debugging assistance

All generated outputs were manually reviewed, modified, and integrated into the final system.

# Future Improvements

* Cross-camera Re-ID using OSNet
* RT-DETR integration
* Staff/customer classification
* Cloud deployment
* Real-time Kafka event streaming
* LLM-powered semantic analytics
* Advanced zone intelligence
* Edge-device optimization

# Conclusion

Retail Intelligence Platform demonstrates how computer vision and event-driven analytics can transform retail operations into intelligent, data-driven systems.

The platform combines AI detection pipelines, real-time analytics, modular architecture, and operational dashboards into a unified retail intelligence ecosystem.
