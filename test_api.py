import requests
import json

# Make a POST request to the API
response = requests.post(
    'http://127.0.0.1:5000/analyze',
    data={'company_name': 'Apple'}
)

# Get the JSON response
data = response.json()

# Format the output to match the required structure
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

# Pretty print the JSON
print(json.dumps(formatted_output, indent=4)) 