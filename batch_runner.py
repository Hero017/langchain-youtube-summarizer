from main import run_pipeline

video_links = {
    "educational": [
        "https://www.youtube.com/watch?v=5MgBikgcWnY",
        "https://www.youtube.com/watch?v=O96fE1E-rf8",
    ],
    "technical": [
        "https://www.youtube.com/watch?v=kCc8FmEb1nY",
        "https://www.youtube.com/watch?v=1BfCnjr_Vjg",
    ],
    "entertainment": [
        "https://www.youtube.com/watch?v=3Yq8bX2yVNw",
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
    ],
    "other": [
        "https://www.youtube.com/watch?v=U6P9ni0fTKc",
        "https://www.youtube.com/watch?v=8S0FDjFBj8o",
        "https://www.youtube.com/watch?v=l-gQLqv9f4o",
        "https://www.youtube.com/watch?v=ysz5S6PUM-U",
    ]
}

for category, urls in video_links.items():
    for i, url in enumerate(urls, start=1):
        print(f"\n=== Running summarizer for {category} video {i} ===")
        run_pipeline(url, category, i)
