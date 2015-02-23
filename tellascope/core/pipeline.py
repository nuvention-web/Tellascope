from tellascope.core.models import UserProfile

def create_user_profile(backend, details, response, uid, user, social, *args, **kwargs):

    if user is None:
        return

    profile = UserProfile.objects.get_or_create(user=user)[0]

    if backend.name == 'twitter':
        profile.twitter_username = response.get('screen_name')
        profile.twitter_description = response.get('description')
        profile.twitter_profile_picture = response.get('profile_image_url')

        if profile.bio is None:
            profile.bio = profile.twitter_description

    if backend.name == 'pocket':
        print 'helloooo'

    profile.save()
