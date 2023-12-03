from django.db import models
from django.utils.text import slugify

# Create your models here.
class TeamMember(models.Model):
    ROLES = [
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLES, default='regular')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """
        Assigns a unique slug: the first team member with a given name will
        get that name, and all duplicates after will have an incrementing
        number added after the name.
        """
        base_slug = slugify(f"{self.first_name} {self.last_name}")
        slug = base_slug
        counter = 1

        while TeamMember.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)
