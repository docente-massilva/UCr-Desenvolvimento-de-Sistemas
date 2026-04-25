from django.db import models


# Classe base para outros modelos, com campos comuns
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Não criar uma tabela para esta classe,
        # pois é apenas um modelo base
        abstract = True


class Colaborador(BaseModel):
    """
    Modelo para representar um colaborador
    """
    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"
        db_table = "colaborador"

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Nome Completo",
        db_column="nome_completo"
    )
    matricula = models.CharField(unique=True, max_length=20, null=False, blank=False)
    setor = models.CharField(max_length=50, null=False, blank=False)
    cargo = models.CharField(max_length=50, null=False, blank=False)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Adotante(models.Model):
    """
    Modelo para representar um adotante
    """
    class Meta:
        verbose_name = "Adotante"
        verbose_name_plural = "Adotantes"
        db_table = "adotante"

    id = models.AutoField(primary_key=True, db_column="idadotante")
    nome = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome
