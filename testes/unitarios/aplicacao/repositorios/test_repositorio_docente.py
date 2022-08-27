from uuid import UUID

from django.test import TestCase

from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente, NomeDeDocente
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteDocente, FabricaTesteIdDeDocente
from aplicacao.models import ModeloDocente
from aplicacao.repositorios import RepositorioDocente


class TestRepositorioDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = RepositorioDocente()

    def test_trazer_QUANDO_modelos_existem_ENTAO_traz_docentes(self) -> None:
        quantidade = 2
        [FabricaTesteModeloDocente.create() for _ in range(quantidade)]

        docentes = self.repositorio_docente.trazer()

        self.assertEqual(len(docentes), quantidade)

    def test_salvar_QUANDO_docente_informado_ENTAO_salva_docente(self) -> None:
        docente = FabricaTesteDocente.build()

        self.repositorio_docente.salvar(docente)

        ModeloDocente.objects.get(pk=docente.id.valor)

    def test_trazer_por_id_QUANDO_docente_existe_ENTAO_retorna_docente(self) -> None:
        modelo: ModeloDocente = FabricaTesteModeloDocente.create()
        id_do_docente = IdDeDocente(UUID(modelo.id))

        docente_resultante = self.repositorio_docente.trazer_por_id(id_do_docente)

        docente_esperado = Docente(
            id=id_do_docente,
            nome=NomeDeDocente(modelo.nome)
        )
        self.assertEqual(docente_resultante, docente_esperado)

    def test_id_existe_QUANDO_id_existe_ENTAO_retorna_true(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        id_do_docente = IdDeDocente(modelo_docente.id)

        reultado = self.repositorio_docente.id_existe(id_do_docente)

        self.assertTrue(reultado)

    def test_id_existe_QUANDO_id_nao_existe_ENTAO_retorna_false(self) -> None:
        id_do_docente: IdDeDocente = FabricaTesteIdDeDocente.build()

        resultado = self.repositorio_docente.id_existe(id_do_docente)

        self.assertFalse(resultado)
