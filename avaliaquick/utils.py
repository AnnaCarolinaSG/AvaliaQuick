from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def enviar_link_acesso(pendente):
    pesquisador = pendente.pesquisador
    token = pesquisador.token
    link = f"127.0.0.1:8000/{reverse('enviar_arquivos', args=[pendente.id, token])}"

    assunto = "Envio de Arquivos para Avaliação Anual"
    mensagem = f"""
Olá, {pesquisador.nome},

Você foi convocado(a) para enviar seus arquivos de avaliação anual.
Por favor, acesse o link abaixo para realizar o envio de forma segura:

{link}

Se você não esperava este e-mail, ignore-o.

Atenciosamente,
Equipe de Avaliação
"""

    send_mail(
        subject=assunto,
        message=mensagem,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[pesquisador.email],
        fail_silently=False
    )
