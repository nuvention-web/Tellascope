from django.contrib import admin

from tellascope.core.models import *

admin.site.register(UserProfile)

admin.site.register(Article)
admin.site.register(Source)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(UserArticleRelationship)



# class ArticleInline(admin.StackedInline):
#     model = UserProfile
#     fk_name = 'user'

# class UserArticleRelationshipAdmin(admin.ModelAdmin):
#     list_display = ['get_userprofile_name', 'email']
#     list_select_related = True
#     inlines = [
#         UserProfileInline,
#     ]

