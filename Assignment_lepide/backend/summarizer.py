from transformers import pipeline


summarizer = pipeline('summarization')

def summarize_text(content):
    """
    Summarizes different sections of a document.
    Assumes the document is structured with a title, description, body, and conclusion.
    """

    summary = {
        'title': '',
        'description': '',
        'story_summary': '',
        'conclusion': ''
    }

    
    lines = content.split('\n')


    summary['title'] = lines[0] if len(lines) > 0 else ''

    
    first_paragraph = ' '.join(lines[1:3]) if len(lines) > 2 else lines[1] if len(lines) > 1 else ''
    summary['description'] = summarizer(first_paragraph, max_length=50, min_length=25, do_sample=False)[0]['summary_text'] if first_paragraph else ''

    
    body = ' '.join(lines[3:-1])  
    summary['story_summary'] = summarizer(body, max_length=100, min_length=50, do_sample=False)[0]['summary_text'] if body else ''

    
    last_paragraph = lines[-1] if len(lines) > 3 else ''
    summary['conclusion'] = summarizer(last_paragraph, max_length=50, min_length=25, do_sample=False)[0]['summary_text'] if last_paragraph else ''

    return summary


