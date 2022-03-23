from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class History(TranslatableModel):
    image = models.ImageField(_('image'),upload_to='frontend/history/', null=True, blank=True)
    date = models.DateTimeField(_('date'), null=True, blank=True)
    
    translations = TranslatedFields(
        title = models.CharField(_('title'),max_length=255, null=True, blank=True),
        description = models.TextField(_('description'), null=True, blank=True),
    )
    
    class Meta:
        verbose_name = _('history')
        verbose_name_plural = _('history')

class Speech(TranslatableModel):
    video = models.URLField(blank=False, null=False, default="https://www.youtube.com/embed/iNTj-r3Nq4Q")
    thumbnail = models.ImageField(blank=False, null=False, upload_to='frontend/speech/')
    date = models.DateTimeField(_('date'), null=True, blank=True)
    translations = TranslatedFields(
        title = models.CharField(_('title'),max_length=255, null=True, blank=True),
        leader = models.CharField(_('leader'),max_length=255, null=True, blank=True),
    )

    class Meta:
        verbose_name = _('speech')
        verbose_name_plural = _('speech')

class FAQ(TranslatableModel):
    translations = TranslatedFields(
        question = models.CharField(_('question'), max_length=1000, null=True, blank=True),
        answer = models.CharField(_('answer'), max_length=10000, null=True, blank=True),
    )

    class Meta:
        verbose_name = _('Frequently Asked Question')
        verbose_name_plural = _('Frequently Asked Questions')
    
class Member(models.Model):

    GENDER_CHOICES = (
        (_('male'), _('Male')),
        (_('female'), _('Female')),
    )
    MARRIAGE_CHOICES = (
        (_('married'), _('Married')),
        (_('unmarried'), _('Unmarried')),
    )

    name = models.CharField(_('full name'),max_length=255, null=False, blank=False)
    citizenship_district = models.CharField(_('citizenship district'),max_length=255, null=False, blank=False)
    citizenship_number = models.IntegerField(_('citizenship number'), null=False, blank=False)
    voterlist_number = models.IntegerField(_('voterlist number'), null=False, blank=False)
    gender = models.CharField(_('gender'), max_length=255, choices=GENDER_CHOICES, null=False, blank=False)
    date_of_birth = models.CharField(_('date of birth'), max_length=255, null=False, blank=False)
    permanent_address = models.CharField(_('permanent address'), max_length=255, null=False, blank=False)
    temporary_address = models.CharField(_('temporary address'), max_length=255, null=False, blank=False)
    marriage_status = models.CharField(_('marriage status'), max_length=255, choices=MARRIAGE_CHOICES, null=False, blank=False)
    number_family_members = models.IntegerField(_('number of family members'), null=False, blank=False)
    education = models.CharField(_('education'), max_length=255, null=False, blank=False)
    caste = models.CharField(_('caste'), max_length=255, null=False, blank=False)
    occupation = models.CharField(_('occupation'), max_length=255, null=False, blank=False)
    conatact_number = models.CharField(_('contact number'), max_length=10, null=False, blank=False)
    email_address = models.EmailField(_('email address'), null=False, blank=False)
    reason = models.CharField(_('reason for being member'), max_length=255, null=False, blank=False)


    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('member')

class Gallery(models.Model):
    image = models.ImageField(_('image'), upload_to='gallery/images/', blank=True)

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('gallerys')