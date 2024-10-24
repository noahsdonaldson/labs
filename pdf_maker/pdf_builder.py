import os
from PIL import Image
import pypdf

folder_path = "./images/940"

for filename in os.listdir(folder_path):
    if filename.endswith('.jpeg') or filename.endswith('.png'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        pdf_path = os.path.join(folder_path, filename[:-4] + '.pdf')
        img.save(pdf_path, 'PDF', resolution=100.0)

pdf_merger = pypdf.PdfMerger()
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        pdf_merger.append(pdf_path)
pdf_merger.write(os.path.join(folder_path, 'merge.pdf'))
# may change the name "merged.pdf" into anyname, and add on the extension: ".pdf"
pdf_merger.close()