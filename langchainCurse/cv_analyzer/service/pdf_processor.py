import pypdf

def readPdf(filePdf):
  try:
    pdf = pypdf.PdfReader(filePdf)
    completText = ""

    for page in pdf.pages:
      textPage = page.extract_text()
      if textPage.strip():
        print("este es el texto de la pagina:", textPage)
        completText += textPage
    completText = completText.strip()

    if not completText:
      return "Error: El pdf esta vacio o no tiene imagenes"
    
    return completText
    
  except Exception as e:
    return f"Error: No se pudo leer el pdf: {str(e)}"