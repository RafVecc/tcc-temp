import json
from uuid import UUID
from django.test import TestCase

from testes.fabricas import FabricaTesteDocente, FabricaTesteModeloDocente, FabricaTesteModeloUnidadeSenai, \
    FabricaTesteModeloTelefone
from aplicacao.models import ModeloDocente, ModeloUnidadeSenai, ModeloTelefone
from dominio.entidades import Docente


class TestModeloDocente(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        modelo_unidade_senai: ModeloUnidadeSenai = FabricaTesteModeloUnidadeSenai.create()
        docente: Docente = FabricaTesteDocente.build(unidade_senai_id=modelo_unidade_senai.id)

        modelo_docente = ModeloDocente.de_entidade(entidade=docente)

        atributos_resultantes = [
            modelo_docente.id,
            modelo_docente.nome,
            modelo_docente.email,
            modelo_docente.unidade_senai,
            modelo_docente.tipo_de_contratacao,
            modelo_docente.ativo
        ]
        atributos_esperados = [
            docente.id.valor,
            docente.nome.valor,
            docente.email.valor,
            modelo_unidade_senai,
            docente.tipo_de_contratacao.valor.value,
            docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.build()

        docente = modelo_docente.para_entidade()

        atributos_resultantes = [
            docente.id.valor,
            docente.nome.valor,
            docente.ativo
        ]
        atributos_esperados = [
            UUID(modelo_docente.id),
            modelo_docente.nome,
            modelo_docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
