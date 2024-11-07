import PyPDF2
import os

def read_pdf():
    # Get the path to our PDF file
    pdf_path = os.path.join('data', 'Eros and Individuation.pdf')
    
    # Open the PDF file
    try:
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Successfully opened PDF. Number of pages: {num_pages}")
            
            # Read first page as a test
            first_page = pdf_reader.pages[0].extract_text()
            print("\nFirst page preview:")
            print(first_page[:500] + "...")
            
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")

if __name__ == "__main__":
    read_pdf() 
    