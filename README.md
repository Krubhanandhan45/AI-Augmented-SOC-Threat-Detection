# AI-Augmented SOC Threat Detection

This project demonstrates an AI-driven Security Operations Center (SOC) platform for detecting suspicious network activity using machine learning and SIEM visualization.

The system integrates Suricata IDS, a Python-based feature extraction pipeline, Isolation Forest anomaly detection, and Splunk dashboards for monitoring security events.

## Architecture

Network Traffic → Suricata IDS → Feature Extraction → Isolation Forest Model → Splunk SIEM Dashboard → Security Alerts

## Key Components

Suricata IDS  
Python Feature Extraction  
Isolation Forest Machine Learning  
Splunk SIEM Dashboard  
SOC Alerting System

## Dataset

The experiment processed approximately 5000 Suricata network events.

The Isolation Forest model detected around 250 anomalies representing suspicious network behavior.

## SOC Dashboard

The Splunk dashboard includes:

• Total anomalies detected  
• Top suspicious source IP addresses  
• Alert signature distribution  
• Destination port analysis  
• Protocol distribution  
• Anomaly trends over time  

## Technologies Used

Python  
Suricata IDS  
Splunk SIEM  
Isolation Forest  
Linux  
Cybersecurity Monitoring

## Project Screenshots

See the `screenshots/` folder for full evidence of:

• Suricata logs  
• Feature extraction  
• ML model training  
• AI anomaly detection  
• Splunk SOC dashboards  
• Automated alert triggering

## Research Paper

Full project paper available in:
