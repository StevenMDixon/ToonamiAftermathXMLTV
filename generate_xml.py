import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Create root element
root = ET.Element("root")

# Add timestamp
timestamp = ET.SubElement(root, "timestamp")
timestamp.text = datetime.utcnow().isoformat() + "Z"

# Optional: add more elements
# example_element = ET.SubElement(root, "example")
# example_element.text = "Hello World"

# Write XML to file
os.makedirs("xml", exist_ok=True)
tree = ET.ElementTree(root)
tree.write("xml/data.xml", encoding="utf-8", xml_declaration=True)

print("XML file generated at xml/data.xml")