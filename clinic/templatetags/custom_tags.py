
from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


# Note:
# Django's template language doesn't support chaining methods like you can in Python. Instead, you can use custom template tags or filters to handle such logic.

# Custom Template Tag: Define a custom template tag to handle complex logic.

# Use in Template: Load the custom tag and apply it in your template.

# By following these steps, you should be able to conditionally render menu items based on user groups without encountering parsing errors. Let me know if you need any further assistance or if there's anything else you want to discuss! 🌟

