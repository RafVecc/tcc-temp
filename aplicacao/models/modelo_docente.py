from __future__ import annotations

import json
from typing import List
from uuid import UUID, uuid4
from django.db import models

from dominio.entidades import Docente


class ModeloDocente(models.Model):
    nome = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, unique=True)
    email = models.EmailField()
    telefones = models.CharField(max_length=200)
    tipo_de_contratacao = models.CharField(max_length=200)
    #unidade_senai_id = models.ForeignKey() #TODO: continuar daqui!
    ativo = models.BooleanField()

    @classmethod
    def de_entidade(cls, entidade: Docente) -> ModeloDocente:
        return cls(
            nome=entidade.nome.valor,
            id=entidade.id.valor,
            email=entidade.email.valor,
            telefone=json.dumps([telefone.valor for telefone in entidade.telefones]),
            tipo_de_contratacao=entidade.tipo_de_contratacao.valor.value,
            #unidade_senai_id=entidade.unidade_senai_id.valor,
            ativo=entidade.ativo
        )

    def para_entidade(self) -> Docente:
        return Docente.construir(
            nome=str(self.nome),
            id_=UUID(str(self.id)),
            email=str(),
            telefones=json.loads(str(self.telefones)),
            tipo_de_contratacao=str(self.tipo_de_contratacao),
            unidade_senai_id=uuid4(),
            #unidade_senai_id=UUID(str(self.unidade_senai_id)),
            ativo=bool(self.ativo)
        )
