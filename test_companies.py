import requests
import json
import sys

def get_company_analysis(company_name):
    """Get analysis for a specified company"""
    print(f"\n=== Analyzing {company_name} ===\n")
    
    # Make POST request to the API
    response = requests.post(
        'http://127.0.0.1:5000/analyze',
        data={'company_name': company_name}
    )
    
    # Check if request was successful
    if response.status_code == 200:
        # Get JSON response
        data = response.json()
        
        # Format the output
        formatted_output = {
            "company_name": data["company_name"],
            "articles": [
                {
                    "title": article["title"],
                    "summary": article["summary"],
                    "sentiment": article["sentiment_category"],
                    "sentiment_score": article["sentiment_score"],
                    "topics": article["topics"],
                    "url": article["url"]
                } for article in data["articles"]
            ],
            "comparative_analysis": {
                "average_sentiment": data["comparative_analysis"]["average_sentiment"],
                "sentiment_distribution": data["comparative_analysis"]["sentiment_distribution"],
                "positive_count": data["comparative_analysis"]["positive_count"],
                "negative_count": data["comparative_analysis"]["negative_count"],
                "neutral_count": data["comparative_analysis"]["neutral_count"],
                "top_topics": data["comparative_analysis"]["top_topics"],
                "most_positive": data["comparative_analysis"]["most_positive"],
                "most_negative": data["comparative_analysis"]["most_negative"]
            },
            "hindi_summary": data["hindi_summary"],
            "audio_url": data["audio_url"]
        }
        
        # Print the formatted JSON
        print(json.dumps(formatted_output, indent=4))
        print(f"\n=== Analysis for {company_name} completed ===\n")
        return formatted_output
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    # List of companies to analyze
    companies = ["Apple", "Tesla", "Amazon", "Microsoft", "Google"]
    
    # Check if specific companies were provided as command line arguments
    if len(sys.argv) > 1:
        companies = sys.argv[1:]
    
    results = {}
    
    # Analyze each company
    for company in companies:
        results[company] = get_company_analysis(company)
    
    return results

if __name__ == "__main__":
    main() 