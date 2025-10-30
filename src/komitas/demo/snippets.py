class ExmapleCode:
    from xml.etree import ElementTree as ET
    from xml.dom import minidom

    html = ET.Element("html")
    head = ET.SubElement(html, "head")
    title = ET.SubElement(head, "title")
    title.text = "Example Page"
    body = ET.SubElement(html, "body")
    h1 = ET.SubElement(body, "h1")
    h1.text = "Hello, World!"

    # formatted pretty print
    output = minidom.parseString(ET.tostring(html, method="html")).toprettyxml("  ")


class ExampleCode2:
    from komitas.html.tags import HTML, Head, Title, Body, H1
    from xml.etree import ElementTree as ET
    from xml.dom import minidom

    html = HTML().innrs(
        Head().innrs(
            Title().innrs("Example Page"),
        ),
        Body().innrs(
            H1().innrs("Hello, World!"),
        ),
    )

    output = minidom.parseString(ET.tostring(html.build(), method="html")).toprettyxml(
        "  "
    )
