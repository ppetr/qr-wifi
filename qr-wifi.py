#!/usr/bin/env python

import argparse
from reportlab.graphics import renderPDF
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A5
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, Image, Paragraph, SimpleDocTemplate, Spacer

class BarCode(Flowable):
    # Based on http://stackoverflow.com/questions/18569682/use-qrcodewidget-or-plotarea-with-platypus
    def __init__(self, widget, ratio=1):
        Flowable.__init__(self)
        self.widget = widget
        self.ratio = ratio

    def wrap(self, availWidth, availHeight):
        # Make the barcode fill the width while maintaining the ratio
        self.width = availWidth
        self.height = self.ratio * availWidth
        return self.width, self.height

    def draw(self):
        # Flowable canvas
        bounds = self.widget.getBounds()
        bar_width = bounds[2] - bounds[0]
        bar_height = bounds[3] - bounds[1]
        w = float(self.width)
        h = float(self.height)
        d = Drawing(w, h, transform=[w / bar_width, 0, 0, h / bar_height, 0, 0])
        d.add(self.widget)
        renderPDF.draw(d, self.canv, 0, 0)

parser = argparse.ArgumentParser(description='Construct a PDF page with WiFi ESSID, password and QR code.')
parser.add_argument('--essid', required=True)
parser.add_argument('--password', required=True)
parser.add_argument('--output', required=True, help="Output PDF file", metavar="FILE.pdf")
parser.add_argument('--message', help="Custom message to be displayed at the bottom")
args = parser.parse_args()

essid = args.essid
password = args.password
output_pdf = args.output
message = args.message

centered = ParagraphStyle(name="centered", alignment=TA_CENTER, fontName="Times-Bold", fontSize=24, leading=30)

qr_text = "WIFI:S:{0};T:WPA2;P:{1};;".format(essid, password)

doc = SimpleDocTemplate(output_pdf, pagesize=A5)
parts = []
parts.append(Paragraph(u"ESSID: " + essid, style=centered))
parts.append(Paragraph(u"Password: " + password, style=centered))
parts.append(Spacer(width=0, height=36))
parts.append(BarCode(qr.QrCodeWidget(qr_text)))
if message:
    parts.append(Spacer(width=0, height=36))
    parts.append(Paragraph(message, style=centered))
doc.build(parts)
