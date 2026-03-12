# Splunk Alert Configuration
# AI-Augmented SOC Detection Alert

Alert Name: AI SOC - Anomaly Spike

Description:
This alert triggers when the number of anomalies detected by the Isolation Forest model exceeds a defined threshold.

Search Query:
index=ai_soc
| stats count as anomaly_count

Trigger Condition:
anomaly_count > 20

Trigger Time Window:
Last 30 minutes

Alert Action:
Send email notification to SOC analyst

Severity:
High

Purpose:
Automatically notify SOC analysts when abnormal network behavior spikes are detected by the AI detection pipeline.
