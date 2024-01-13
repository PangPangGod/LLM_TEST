import streamlit as st
import fitz # PyMuPDF
import tempfile
import os
import fitz  # PyMuPDF

def extract_text_and_positions(pdf_path):
    doc = fitz.open(pdf_path)
    result_storage_dict = {}
    for index, page in enumerate(doc, start=1):
        text_blocks = page.get_text("dict")["blocks"]
        data = []
        for block in text_blocks:
            if block["type"] == 0:  # block type 0 denotes text
                bbox = block["bbox"]
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        text += span["text"] + " "
                data.append({"text": text.strip(), "bbox": bbox, "page": page.number})
        result_storage_dict[f"page_{index}"] = data 
        
    return result_storage_dict

if __name__ == "__main__":
    datas = extract_text_and_positions("./MS-1001_Draft.pdf")

    for key, value in datas.items():
        print(key)

        for chunk in value:
            text = chunk['text']

            print(text)
            
        print("="*60)
        