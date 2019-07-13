from django.core.exceptions import ValidationError

def validate_content(content):
	body == content
	if body == "":
		raise ValidationError("Post cannot be blank")
	return content