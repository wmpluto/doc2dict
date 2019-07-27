import pdfminer.layout
import pdfminer.high_level

  
class doc2dict():
    def __init__(self, file):
        extension = file.split('.')[-1].lower()
        if extension == 'pdf':
            self.extract_raw_text(file)
            self.text = 'tmp.txt'
        elif extension == 'txt':
            self.text = file
        else:
            pass
    
    def extract_raw_text(self, input):
        with open('tmp.txt', "wb") as op:
            laparams = pdfminer.layout.LAParams()
            setattr(laparams, "all_texts", True)
            setattr(laparams, "detect_vertical", True)
        
            with open(input, "rb") as pdffile:
                pdfminer.high_level.extract_text_to_fp(pdffile, op, laparams=laparams)  
        
    def convert2dict():
        pass

def main():
    doc2dict('test.pdf')

if __name__ == "__main__":
    main()