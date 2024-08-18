import os
import tempfile
from  Summarizer import Summarizer  
class DocumentSummarizer:
    def __init__(self):
        
        self.summarizer = Summarizer()

    def summarize(self, file_path):
        
        with open(file_path, 'r') as file:
            content = file.read()
        summary = self.summarizer.summarize(content)  
        return summary

def summarize_document(file_path):
    summarizer = DocumentSummarizer()
    summary = summarizer.summarize(file_path)
    return summary

if __name__ == "__main__":
    
    test_file_path = "path_to_some_document.txt" 
    summary = summarize_document(test_file_path)
    print("Summary:", summary)
