from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    access['username'] = user.username  # <-- ajout ici
    return {
        'refresh': str(refresh),
        'access': str(access),  # <-- c'est ce token que le frontend utilise
    }
