
def get_profile_picture(strategy, details, response, uid, user, social, *args, **kwargs):
    """Attempt to get a profile image for the User"""

    if user is None:
        return

    image_url = None
    if strategy.backend.name == "twitter":
        if response['profile_image_url'] != '':
            image_url = response['profile_image_url']

    if image_url:
        try:
            result = urllib.urlretrieve(image_url)
            user.original_photo.save("{0}.jpg".format(uid), File(open(result[0])))
            user.save(update_fields=['original_photo'])
        except URLError:
            pass
