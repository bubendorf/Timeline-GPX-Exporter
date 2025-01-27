#!/usr/bin/env python3
import os
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
from datetime import datetime

def create_gpx_file(points, output_file):
    gpx = ET.Element("gpx", version="1.1", creator="https://github.com/Makeshit/Timeline-GPX-Exporter", xmlns="http://www.topografix.com/GPX/1/1" )
    trk = ET.SubElement(gpx, "trk")
    trkseg = ET.SubElement(trk, "trkseg")

    for point in points:
        trkpt = ET.SubElement(trkseg, "trkpt", lat=str(point["lat"]), lon=str(point["lon"]))
        ET.SubElement(trkpt, "time").text = point["time"]

    # Generate pretty XML
    xml_str = xml.dom.minidom.parseString(ET.tostring(gpx)).toprettyxml(indent='\t')
#    xml_str = ET.tostring(gpx, encoding="utf-8").decode("utf-8")

    # Write the XML to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_str)

def parse_json(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    points_by_date = {}

    # Extract data points
    for segment in data.get("semanticSegments", []):
        for path_point in segment.get("timelinePath", []):
            try:
                # Extract and parse data
                raw_coords = path_point["point"].replace("°", "").strip()
                coords = raw_coords.split(", ")
                lat, lon = float(coords[0]), float(coords[1])
                time = path_point["time"].replace(".000", "")

                # Extract date for grouping
                date = datetime.fromisoformat(time).date().isoformat()

                if date >= '2025-01-01':
                  # Group by date
                  if date not in points_by_date:
                      points_by_date[date] = []
                  points_by_date[date].append({"lat": lat, "lon": lon, "time": time})
            except (KeyError, ValueError):
                continue  # Skip invalid points

    return points_by_date

def main():
    script_dir = os.getcwd()  # Directory where the script is being run
    input_file = os.path.join(script_dir, "Timeline.json")  # Input JSON file
    output_dir = os.path.join(script_dir, "GPX_Output")  # Directory for output GPX files

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        print(f"Input file 'Timeline.json' not found in {script_dir}.")
        return

    points_by_date = parse_json(input_file)

    for date, points in points_by_date.items():
        # Convert date format to dd-mm-yyyy ?
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        output_file = os.path.join(output_dir, f"{formatted_date}.gpx")
        create_gpx_file(points, output_file)
        print(f"Created: {output_file}, {len(points)} track points")

if __name__ == "__main__":
    main()
