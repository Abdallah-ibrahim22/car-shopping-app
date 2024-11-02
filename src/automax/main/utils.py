def user_listing_path(instance , filename):
    return 'user_{0}/listings/{1}'.format(instance.seller.user.id-4 , filename)

    # so this fn here return string('user_{instance.user.id}/filename')
    # this fn called when we upload an image 
    # to put it on folder called (user_{instance.user.id})
    # with filename with it's filename
    # so we need to specify the main file for all media we upload in setting file