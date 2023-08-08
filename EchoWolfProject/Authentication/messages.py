from django.conf import settings
from django.http import HttpRequest
from django.contrib import messages
from django.forms.utils import ErrorDict

from pydantic import BaseModel

from Types.main import LiteralLang

class MessagesTemplates(BaseModel):

    @staticmethod
    def unauthorized (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "No autorizado: Usuario o contraseña inválidos",
            'en': "Unauthorized: Invalid username or password",
            'fr': "Non autorisé: Nom d'utilisateur ou mot de passe invalide"
        }
        return message.get(lang, "Error: Language not supported")
    
    @staticmethod
    def signUpSuccess (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "Usuario creado correctamente",
            'en': "User created successfully",
            'fr': "Utilisateur créé avec succès"
        }
        return message.get(lang, "Error: Language not supported")

    @staticmethod
    def passIncorrect (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "Contraseña incorrecta",
            'en': "Incorrect password",
            'fr': "Mot de passe incorrect"
        }
        return message.get(lang, "Error: Language not supported")
    
    @staticmethod
    def usernameAlreadyExist (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "El nombre de usuario ya existe. Por favor, use uno diferente",
            'en': "Username already exists. Please use a different one",
            'fr': "Le nom d'utilisateur existe déjà. Veuillez en utiliser un différent"
        }
        return message.get(lang, "Error: Language not supported")
    
    @staticmethod
    def emailAlreadyExist (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "El email ya está registrado. Por favor, use uno diferente",
            'en': "Email already registered. Please use a different one",
            'fr': "L'e-mail est déjà enregistré. Veuillez en utiliser un différent"
        }
        return message.get(lang, "Error: Language not supported")

    @staticmethod
    def passConfirmationIncorrect (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "Las contraseñas no coinciden",
            'en': "Passwords do not match",
            'fr': "Les mots de passe ne correspondent pas"
        }
        return message.get(lang, "Error: Language not supported")
    
    @staticmethod
    def passNotValid (lang: LiteralLang = settings.LANGUAGE_CODE):
        message = {
            'es': "La contraseña debe tener al menos 8 caracteres y contener solo letras, dígitos y caracteres especiales (@#$%^&+=.)",
            'en': "Password must be at least 8 characters long and contain only letters, digits, and special characters (@#$%^&+=.)",
            'fr': "Le mot de passe doit comporter au moins 8 caractères et ne contenir que des lettres, des chiffres et des caractères spéciaux (@#$%^&+=.)"
        }
        return message.get(lang, "Error: Language not supported")
    
def mapValidationMessages (request: HttpRequest, errors: ErrorDict):
    """Map validation messages to Django messages"""
    for field, error in errors.items():
        if field == '__all__':
            messages.error(request, error[0])
        else:
            messages.error(request, f"{error[0]}")