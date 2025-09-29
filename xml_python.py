import xml.etree.ElementTree as ET

xml_data = """
<user>
 <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>joth.doe@gmail.com</email>
    <age>30</age>
</user>
"""

root = ET.fromstring(xml_data)

print("user_id =", root.find('id').text)