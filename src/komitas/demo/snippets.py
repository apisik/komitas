class ExmapleCode:
    from xml.etree import ElementTree as ET

    html = ET.Element("html")
    head = ET.SubElement(html, "head")
    title = ET.SubElement(head, "title")
    title.text = "Example Page"
    body = ET.SubElement(html, "body123")
    h1 = ET.SubElement(body, "h1")
    h1.text = "Hello, World!"

    ET.tostring(html, encoding="unicode", short_empty_elements=False)