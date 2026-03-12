# Splunk SOC Dashboard Queries
# AI-Augmented SOC Threat Detection

# 1 Total AI Detected Anomalies
index=ai_soc
| stats count as total_anomalies

# 2 Top Suspicious Source IPs
index=ai_soc
| stats count by src_ip
| sort - count
| head 10

# 3 Alert Signature Distribution
index=suricata
| stats count by alert_signature
| sort - count

# 4 Destination Port Analysis
index=suricata
| stats count by dest_port
| sort - count

# 5 Protocol Distribution
index=suricata
| stats count by proto

# 6 Anomaly Trend Over Time
index=ai_soc
| timechart count
