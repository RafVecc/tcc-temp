from __future__ import annotations

from django.db import models

from aplicacao.models.modelo_docente import ModeloDocente


class ModeloTelefone(models.Model):
    numero = models.CharField(primary_key=True, max_length=14)
    docente = models.ForeignKey(ModeloDocente, on_delete=models.CASCADE)
