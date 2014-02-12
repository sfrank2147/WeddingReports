def avg_rating(db_results):
    '''Filter to get the average rating from a query of reports'''
    rating_list = [report.rating for report in db_results]
    return sum(rating_list)/float(len(rating_list))
