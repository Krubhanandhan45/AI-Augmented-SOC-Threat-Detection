import json
import csv

# Input Suricata log file
input_file = "eve.json"

# Output feature dataset
output_file = "features.csv"

features = []

with open(input_file) as f:
    for line in f:
        data = json.loads(line)

        if data.get("event_type") == "alert":

            src_port = data.get("src_port")
            dest_port = data.get("dest_port")

            flow = data.get("flow", {})

            pkts_to_server = flow.get("pkts_toserver", 0)
            pkts_to_client = flow.get("pkts_toclient", 0)

            bytes_to_server = flow.get("bytes_toserver", 0)
            bytes_to_client = flow.get("bytes_toclient", 0)

            severity = data.get("alert", {}).get("severity", 0)

            row = [
                src_port,
                dest_port,
                pkts_to_server,
                pkts_to_client,
                bytes_to_server,
                bytes_to_client,
                severity
            ]

            features.append(row)

with open(output_file, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "src_port",
        "dest_port",
        "flow_pkts_toserver",
        "flow_pkts_toclient",
        "flow_bytes_toserver",
        "flow_bytes_toclient",
        "alert_severity"
    ])

    writer.writerows(features)

print("Feature extraction completed successfully.")