from unittest import TestCase
from mockito import mock, unstub, when

from dominio.casos_de_uso import CasoDeUsoTrazerDocentes
from testes.fabricas import FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.entidades import Docente


class TestCasoDeUsoTrazerDocentes(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = mock({
            'trazer': lambda: None,
        })
        self.caso_de_uso_trazer_docentes = CasoDeUsoTrazerDocentes(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_docentes_existem_ENTAO_retorna_otds_esperados(self) -> None:
        docentes: [Docente] = [FabricaTesteDocente.build() for _ in range(2)]
        when(self.repositorio_docente).trazer().thenReturn(docentes)

        otds_resultantes = self.caso_de_uso_trazer_docentes.executar()

        otds_esperados = [
            OTDDocente(
                id=docente.id.valor,
                nome=docente.nome.valor
            ) for docente in docentes
        ]
        self.assertEqual(otds_resultantes, otds_esperados)