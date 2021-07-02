from settings.models import *
from catalog.models import *
from django.utils import timezone

def load_settings(request):
    social_media_settings = SocialMediaSetting.objects.all()
    menu_setting = MenuSetting.objects.first()
    footer_contacts = FooterContacts.objects.all()
    sba = SecondBlockAbouts.objects.all()
    bs = BlocksSettings.objects.first()
    pss = PSSettings.objects.first()
    menu_url = MenuUrl.objects.all()
    categories = Category.objects.all()
    year = timezone.now().year
    pages = Page.objects.filter(show_in_menu=True).all()
    return {'SocialMediaSettings': social_media_settings, 'MenuSetting': menu_setting, 'FooterContacts': footer_contacts, 'SecondBlockAbouts': sba, 'BlocksSettings': bs, 'PSSettings': pss, 'MenuUrl': menu_url,'categories': categories,'year': year,'Pages': pages}