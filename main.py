import json
from operator import itemgetter


def filter_reviews(rating_order, date_order, prioritize_text, minimum_rating):
    # Reading from json file
    with open('reviews.json') as f:
        reviews = json.load(f)

    # Filtering by minimum rating
    reviews = [r for r in reviews if r['rating'] >= minimum_rating]

    # Sorting the reviews by rating and date
    if prioritize_text:
        reviews_with_text = [r for r in reviews if r['reviewText']]
        reviews_without_text = [r for r in reviews if not r['reviewText']]
        reviews_with_text = sorted(reviews_with_text, key=itemgetter('rating'), reverse=(rating_order=='newest'))
        reviews_without_text = sorted(reviews_without_text, key=itemgetter('rating'), reverse=(rating_order=='newest'))
        reviews_with_text = sorted(reviews_with_text, key=itemgetter('reviewCreatedOnDate'), reverse=(date_order=='newest'))
        reviews_without_text = sorted(reviews_without_text, key=itemgetter('reviewCreatedOnDate'), reverse=(date_order=='newest'))
        sorted_reviews = reviews_with_text + reviews_without_text
    else:
        sorted_reviews = sorted(reviews, key=itemgetter('rating'), reverse=(rating_order=='newest'))
        sorted_reviews = sorted(sorted_reviews, key=itemgetter('reviewCreatedOnDate'), reverse=(date_order=='newest'))

    # Printing the reviews
    print(f"{'Rating':<10} {'Text':<20} {'Date':<20}        {'Reviewer':<30}")
    print("-"*90)

    for r in sorted_reviews:
        rating = f"{r['rating']}-star"
        text = r['reviewText'] if r['reviewText'] else "No"
        date = r['reviewCreatedOnDate']
        reviewer = r['reviewerName']
        print(f"{rating:<10} {text:<20} {date:<20}   {reviewer:<30}")

rating_order = 'highest'  # highest/lowest
date_order = 'newest'  # newest/oldest
prioritize_text = True
minimum_rating = 3
filter_reviews(rating_order, date_order,prioritize_text,minimum_rating)